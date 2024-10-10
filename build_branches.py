"""
Handles dynamic environment building and hosting through dynamically
updated nginx.conf
"""
import argparse
import ast
import os
import shutil
import subprocess
import sys


HOSTED_SITE_DOMAIN = "docs-dev.polygon.technology"


def parse_args():
    """
    Parses arguments passed from command line
    """
    parser = argparse.ArgumentParser(description="Parser to read arguments for build")
    parser.add_argument("-env", "--environment", type=str,
        help="Environment to handle build", default="dev"
    )
    args = parser.parse_args(sys.argv[1:])
    parsed_env = args.environment.strip()
    return parsed_env


def install_mkdocs_with_pipenv():
    """
    Builds a particular branch site.
    Having a varying set of requirements can be handled by having each branch
    build their dependencies and then running mkdocs build.
    """
    folder = os.getcwd()
    subprocess.run(["pipenv", "install", "--site-packages"], cwd=folder, check=True)
    subprocess.run(["pipenv", "install", "-r", "requirements.txt"], cwd=folder, check=True)
    subprocess.run(["pipenv", "run", "mkdocs", "build"], cwd=folder, check=True)

def copy_folder(source_dir, target_dir):
    """
    Copies contents from source directory to target directory
    :param source_dir: Source directory from which contents are to be copied
    :param target_dir: Target Directory where the contents are copied to.
    """
    os.makedirs(target_dir, exist_ok=True)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)

        if os.path.isdir(source_path):
            shutil.copytree(source_path, target_path, dirs_exist_ok=True)
        else:
            if os.path.exists(target_path):
                os.remove(target_path)
            shutil.copy2(source_path, target_path)

def delete_folders(folder_paths):
    """
    Cleans existing folders for app and branches before executing the builds
    :param folder_paths: List of folders to be deleted under the current working directory
    """
    for folder_path in folder_paths:
        try:
            shutil.rmtree(folder_path)
            print(f"Folder {folder_path} deletion successful.")
        except OSError as e:
            print(f"Error deleting folder: {e}")

def clone_data_to_branch_folder(branch_name, remote_url, parent_dir, pr_number=None):
    """
    Clones data to branch folder in branch/<PR Number> or branch/dev folder
    :param branch_name: Branch to clone and build
    :param remote_url: Remote url for the git repository
    :param parent_dir: Parent directory to get context of where data is stored
    :param pr_number: PR number for the branch to host data into the folder or 
        environment name staging/prod
    """
    common_dir = "branch"
    target_path = os.path.join(common_dir, pr_number)
    os.makedirs(target_path, exist_ok=True)
    os.chdir(target_path)
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
    print(f"Checking out branch {branch_name}")
    subprocess.run(["git", "fetch", "--depth", "1", "origin", branch_name], check=True)
    subprocess.run([
        "git", "checkout", "-b", branch_name, "--track",
        f"origin/{branch_name}"
    ], check=True)
    install_mkdocs_with_pipenv()
    source_dir = os.path.join(os.getcwd(), "site")
    copy_folder(source_dir, os.path.join(parent_dir, "app", pr_number))
    os.chdir(parent_dir)


def update_pr_description(pr_number:str):
    """
    Updates PR description by adding the url to access the hosted environment under dev
    if it does not already exist in the definition
    :param pr_number: PR number for the branch hosting website
    """
    command = ["gh", "pr", "view", pr_number, "--json", "body", "--jq", ".body"]
    pr_description = subprocess.run(command, capture_output=True, text=True,
                                    check=True).stdout.strip()
    hosted_url = f"{HOSTED_SITE_DOMAIN}/{pr_number}"
    if hosted_url not in pr_description:
        new_pr_description = f"Hosted url: [{hosted_url}](https://{hosted_url})\n" + pr_description
        command = ["gh", "pr", "edit", pr_number, "--body", new_pr_description]
        subprocess.run(command, check=True)


def process_branch_folders(parsed_env: str):
    """
    Clones the branch specific code to hosted/<branch-name> folder.
    It then executes the build command and copy the built site to apps folder
    under the same branch name
    :param parsed_env: Environment which is used to build.
    :return: PR numbers in str list where the site data is copied to
    """
    delete_folders(["branch", "app"])

    command = ["gh", "pr", "list", "--json", "number,headRefName"]
    command_run_result = subprocess.run(command, capture_output=True, text=True,
                                        check=True).stdout.strip()
    branches_data = ast.literal_eval(command_run_result)
    remote_url = subprocess.run(["git", "remote", "get-url", "origin"],
                                capture_output=True,
                                text=True, check=True).stdout.strip()
    parent_dir = os.getcwd()
    branch_name = parsed_env
    if parsed_env in ["staging", "prod"]:
        branch_name = "main"
    clone_data_to_branch_folder(branch_name, remote_url, parent_dir, parsed_env)
    pr_numbers = []
    if parsed_env == "dev":
        for branch_data in branches_data:
            if not branch_data["headRefName"].startswith("hosted/") or \
                    not branch_data.get("number"):
                continue
            pr_number = str(branch_data["number"])
            clone_data_to_branch_folder(branch_data["headRefName"], remote_url,
                                        parent_dir, pr_number)
            update_pr_description(pr_number)
            pr_numbers.append(pr_number)

    return pr_numbers

def update_nginx_config(pr_numbers, parsed_env):
    """
    Updates nginx.conf file with branches built information to host multiple versions
    of software at the same time.
    :param pr_numbers: pr numbers a str list of open pr numbers to be hosted
    :param parsed_env: Environment which is used to build.
    """
    config_file = os.path.join(os.getcwd(), "nginx.conf")
    nginx_location_blocks = ""

    for pr_number in pr_numbers:
        location_block = f"""location /{pr_number} {{
            alias /app/{pr_number};
            try_files $uri $uri/ /index.html;
            error_page 404 /404.html;
        }}
        """
        nginx_location_blocks += location_block
        print(f"Hosted site: https://{HOSTED_SITE_DOMAIN}/{pr_number}")

    content = ""
    with open(config_file, "r+", encoding="utf-8") as f:
        content = f.read()
        content = content.replace("#REPLACE_APPS", nginx_location_blocks)
        content = content.replace("#environment", parsed_env)
        f.seek(0)
        f.write(content)
        f.truncate()

    print(f"NGINX configuration updated successfully! content: \n{content}")

if __name__ == "__main__":
    environment = parse_args()
    open_prs = process_branch_folders(environment)
    update_nginx_config(open_prs, environment)
