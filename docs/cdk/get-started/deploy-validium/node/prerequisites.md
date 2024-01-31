!!! important
    - You have already followed the [deploy contracts section](../contracts/prerequisites.md).
    - Make sure you have at least `~0.3 Sepolia ETH` for deploying more contracts and various contract calls.

## Software requirements

!!! important
    These are the minimum versions.

| Software | Version | Installation link |
| --- | --- | --- |
| `git` | 2.18.0 | https://git-scm.com/book/en/v2/Getting-Started-Installing-Git |
| `node` | 16.0.0 | https://nodejs.org/en/download |
| `npm` | 6.0.0 | https://docs.npmjs.com/downloading-and-installing-node-js-and-npm |
| `golang` | 1.18.0 | https://go.dev/doc/install |
| `cast` | 0.2.0 | https://book.getfoundry.sh/getting-started/installation |
| `jq` | 1.0 | https://jqlang.github.io/jq/download/ |
| `tomlq` | 3.0.0 | https://kislyuk.github.io/yq/#installation |
| `postgres` | 15 | https://www.postgresql.org/download/ |
| `psql` | 15.0 | https://www.postgresql.org/download/ |
| `make` | 3.80.0 | https://www.gnu.org/software/make/ |
| `docker` | 24.0.0 | https://docs.docker.com/engine/install/ |
| `pip3` | 20.0.0 | https://pip.pypa.io/en/stable/installation/ |
| `python3` | 3.8.0 | https://www.python.org/downloads/ |
| [For testing] `polycli` | 0.1.39 | https://github.com/maticnetwork/polygon-cli/tree/main |

1. Create a `version-check.sh` file and copy and paste the script below. 

   ```bash
    #!/bin/bash
    
    declare -A commands
    commands["git"]="2.18.0"
    commands["node"]="16.0.0"
    commands["npm"]="6.0.0"
    commands["go"]="1.18.0"
    commands["cast"]="0.2.0"
    commands["jq"]="1.0"
    commands["tomlq"]="3.0.0"
    commands["psql"]="15.0"
    commands["make"]="3.80.0"
    commands["docker"]="24.0.0"
    commands["pip3"]="20.0.2"
    commands["python3"]="3.8.0"
    commands["polycli"]="0.1.39"
    
    # Function to check command version
    check_version() {
        local command=$1
        local min_version=$2
        local version
        local status
    
        if ! command -v "$command" &> /dev/null; then
            printf "| %-15s | %-20s | %-20s |\n" "$command" "Not Found" "$min_version"
            return
        fi
    
        case "$command" in
            git) version=$(git --version | awk '{print $3}') ;;
            node) version=$(node --version | cut -d v -f 2) ;;
            npm) version=$(npm --version) ;;
            go) version=$(go version | awk '{print $3}' | cut -d 'o' -f 2) ;;
            cast) version=$(cast --version | awk '{print $2}') ;;
            jq) version=$(jq --version | cut -d '-' -f 2) ;;
            tomlq) version=$(tomlq --version | awk '{print $2}') ;;
            psql) version=$(psql --version | awk '{print $3}') ;;
            make) version=$(make --version | head -n 1 | awk '{print $3}') ;;
            docker) version=$(docker --version | awk '{print $3}' | cut -d ',' -f 1) ;;
            pip3) version=$(pip3 --version | awk '{print $2}') ;;
            python3) version=$(python3 --version | awk '{print $2}') ;;
            polycli) version=$(polycli version | awk '{print $4}' | cut -d '-' -f 1 | sed 's/v//') ;;
            *) version="Found" ;;
        esac
    
        printf "| %-15s | %-20s | %-20s |\n" "$command" "$version" "$min_version"
    }
    
    echo "+-----------------+----------------------+----------------------+"
    printf "| %-15s | %-20s | %-20s |\n" "CLI Command" "Found Version" "Minimum Version"
    echo "+-----------------+----------------------+----------------------+"
    
    for cmd in "${!commands[@]}"; do
        check_version "$cmd" "${commands[$cmd]}"
        echo "+-----------------+----------------------+----------------------+"
    done
    ```
    
2. Run the script to see what you have already and what is missing from your set up.
    
    ```bash
    chmod +x version-check.sh
    ./version-check.sh
    ```

3. Install any missing or out-of-date software.