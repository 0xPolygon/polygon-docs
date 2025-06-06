#!/usr/bin/env python3
"""
Fast multi-branch docs builder *with rich logging*.
"""

from __future__ import annotations
import argparse
import json
import logging
import os
import shutil
import subprocess
import time
from functools import lru_cache
from pathlib import Path

HOSTED_SITE_DOMAIN = "docs-dev.polygon.technology"


# ────────────────────────── logging setup ──────────────────────────────────── #

def setup_logging(verbosity: int) -> None:
    """
    Configure root logger.
    -0 : WARNING,  1 : INFO (default),  2 : DEBUG,  ≥3 : NOTSET
    """
    level = max(logging.WARNING - (verbosity * 10), logging.NOTSET)
    fmt   = "%(asctime)s  %(levelname)-7s  %(message)s"
    datef = "%H:%M:%S"
    logging.basicConfig(level=level, format=fmt, datefmt=datef)

log = logging.getLogger(__name__)

# ────────────────────────── helpers ───────────────────────────────────────── #

def run(cmd: list[str] | tuple[str, ...],
        cwd: str | Path | None = None,
        capture_output: bool = False) -> subprocess.CompletedProcess[str]:
    """
    Wrapper around subprocess.run with detailed logging & timing.
    Returns CompletedProcess; raises if non-zero exit code.
    """
    cmd_display = " ".join(cmd)
    wd = str(cwd) if cwd else os.getcwd()
    log.debug("RUN  %s (cwd=%s)", cmd_display, wd)

    t0 = time.perf_counter()
    try:
        cp = subprocess.run(
            cmd,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=capture_output
        )
        elapsed = time.perf_counter() - t0
        log.debug("OK   %s (%.2fs)", cmd_display, elapsed)
        return cp
    except subprocess.CalledProcessError as exc:
        elapsed = time.perf_counter() - t0
        log.error("FAIL %s (%.2fs, exit=%s)", cmd_display, elapsed, exc.returncode)
        if exc.stdout:
            log.error("stdout:\n%s", exc.stdout.strip())
        if exc.stderr:
            log.error("stderr:\n%s", exc.stderr.strip())
        raise                        # re-raise so caller still sees the traceback

# ────────────────────────── git helpers ───────────────────────────────────── #

REPO_CACHE_DIR = Path(".repo-cache")
WORKTREES_DIR  = Path("branch")
APPS_DIR       = Path("app")
UV_ENV_DIR     = ".venv"

def prepare_repo_cache(remote_url: str) -> Path:
    if not REPO_CACHE_DIR.exists():
        log.info("Cloning %s → %s", remote_url, REPO_CACHE_DIR)
        run([
            "git", "clone",
            "--filter=blob:none",
            remote_url,
            str(REPO_CACHE_DIR),
        ])
    else:
        log.info("Fetching updates inside %s", REPO_CACHE_DIR)
        run(["git", "fetch", "--prune", "origin", "+refs/heads/*:refs/remotes/origin/*"], cwd=REPO_CACHE_DIR)
    log.debug("Available branches in %s:", REPO_CACHE_DIR)
    branches = run(["git", "branch", "-r"], cwd=REPO_CACHE_DIR, capture_output=True).stdout
    log.debug("%s", branches)
    return REPO_CACHE_DIR

def checkout_worktree(repo: Path, branch: str, dest: Path) -> None:
    dest = dest.resolve()
    if dest.exists():
        log.debug("Removing stale worktree %s", dest)
        run(["git", "worktree", "remove", "--force", str(dest)], cwd=repo)
    log.info("Creating worktree %s for branch %s", dest, branch)
    run(["git", "worktree", "add", "--force", str(dest), f"origin/{branch}"], cwd=repo)

# ────────────────────────── build helpers ─────────────────────────────────── #

@lru_cache(maxsize=None)
def ensure_uv_env(repo: Path) -> None:
    if not (repo / UV_ENV_DIR).exists():
        log.info("Creating shared uv virtual-env %s", UV_ENV_DIR)
        run(["uv", "venv", UV_ENV_DIR], cwd=repo)
    log.debug("Ensuring deps are installed in shared env")
    lock_file = repo / "uv.lock"  # Correct: repo is .repo-cache
    log.debug("Checking for uv.lock at %s", lock_file)
    if not lock_file.exists():
        log.error("uv.lock not found at %s, installing mkdocs only", lock_file)
        run(["uv", "pip", "install", "mkdocs"], cwd=repo)
    else:
        log.info("Syncing dependencies from %s", lock_file)
        run(["uv", "sync", "--frozen"], cwd=repo)

def build_site(root: Path) -> None:
    ensure_uv_env(root.parent)           # repo is parent of worktree
    log.info("Building MkDocs site in %s", root)
    run(["uv", "run", "mkdocs", "build", "-q"], cwd=root)

# ────────────────────────── misc helpers ──────────────────────────────────── #

def copy_site(src: Path, dst: Path) -> None:
    log.info("Copy site %s → %s", src, dst)
    dst.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def delete_tree(path: Path) -> None:
    log.debug("Checking if path %s exists", path)
    if path.exists():
        log.debug("Deleting %s", path)
        shutil.rmtree(path, ignore_errors=True)
    else:
        log.debug("Path %s does not exist, skipping deletion", path)

# ────────────────────────── PR helpers ────────────────────────────────────── #

def update_pr_description(pr_number: str) -> None:
    hosted_url = f"https://{HOSTED_SITE_DOMAIN}/{pr_number}"
    body = run(
        ["gh", "pr", "view", pr_number, "--json", "body", "--jq", ".body"],
        capture_output=True
    ).stdout
    if hosted_url not in body:
        log.info("Updating PR #%s description with hosted URL", pr_number)
        new_body = f"Hosted url: [{hosted_url}]({hosted_url})\n{body}"
        run(["gh", "pr", "edit", pr_number, "--body", new_body])

# ────────────────────────── main workflow ─────────────────────────────────── #

def branch_exists(repo: Path, branch: str) -> bool:
    """Check if a branch exists in the repository."""
    try:
        run(["git", "rev-parse", "--verify", f"origin/{branch}"], cwd=repo, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def process_environment(env: str) -> list[str]:
    delete_tree(WORKTREES_DIR)
    delete_tree(APPS_DIR)
    remote_url = run(["git", "remote", "get-url", "origin"], capture_output=True).stdout.strip()
    repo = prepare_repo_cache(remote_url)  # repo is .repo-cache
    main_branch = "main" if env in {"staging", "prod"} else env
    if env == "dev" and not branch_exists(repo, main_branch):
        log.warning("Branch 'dev' does not exist, falling back to 'main'")
        main_branch = "main"
    main_wt = (WORKTREES_DIR / env).resolve()
    checkout_worktree(repo, main_branch, main_wt)
    ensure_uv_env(repo)  # Pass repo (.repo-cache), not main_wt.parent
    build_site(main_wt)
    copy_site(main_wt / "site", APPS_DIR / env)

    pr_numbers: list[str] = []
    if env == "dev":
        prs_json = run(
            ["gh", "pr", "list", "--json", "number,headRefName"],
            capture_output=True
        ).stdout
        for pr in json.loads(prs_json):
            if not pr["headRefName"].startswith("hosted/"):
                continue
            num = str(pr["number"])
            if not branch_exists(repo, pr["headRefName"]):
                log.warning("Skipping PR #%s: branch %s does not exist", num, pr["headRefName"])
                continue
            pr_numbers.append(num)
            wt = (WORKTREES_DIR / num).resolve()
            checkout_worktree(repo, pr["headRefName"], wt)
            build_site(wt)
            copy_site(wt / "site", APPS_DIR / num)
            update_pr_description(num)

    return pr_numbers

def update_nginx_config(pr_numbers: list[str], env: str) -> None:
    blocks = "\n".join(
        f"""location /{n} {{
    alias /app/{n};
    try_files $uri $uri/ =404;
    error_page 404 /404.html;
}}""" for n in pr_numbers)
    conf_template = Path("nginx_template")
    conf = Path("nginx.conf")
    content = conf_template.read_text(encoding="utf-8")
    content = content.replace("#REPLACE_APPS", blocks).replace("#environment", env)
    conf.write_text(content, encoding="utf-8")
    log.info("NGINX configuration updated with %d blocks", len(pr_numbers))
    log.info("Generated nginx.conf content:\n%s", conf.read_text(encoding="utf-8"))

# ────────────────────────── CLI ───────────────────────────────────────────── #

def parse_args() -> tuple[str, int]:
    p = argparse.ArgumentParser()
    p.add_argument("-env", "--environment", default="dev",
                   help="dev (default) | staging | prod")
    p.add_argument("-v", "--verbose", action="count", default=1,
                   help="-v INFO (default), -vv DEBUG, -vvv NOTSET")
    args = p.parse_args()
    return args.environment.strip(), args.verbose

# ────────────────────────── entry point ───────────────────────────────────── #

if __name__ == "__main__":
    env, verbosity = parse_args()
    setup_logging(verbosity)
    log.info("Start build for environment=%s", env)
    prs = process_environment(env)
    update_nginx_config(prs, env)
    log.info("All done. Hosted PRs: %s", ", ".join(prs) or "none")
