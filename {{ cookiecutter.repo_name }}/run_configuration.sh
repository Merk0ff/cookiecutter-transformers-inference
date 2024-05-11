#!/bin/bash

# Define a function to run docker-compose commands with the specified config
run_with_config() {
    local config_alias="$1"
    shift 1 # Remove the config alias from the arguments
    local config_files=()

    # Define your configurations
    case "$config_alias" in
        "con")
            config_files+=("./compose/docker-compose.yml" "./compose/docker-compose.infra.yml")
            ;;
        "exp")
            config_files+=("./compose/docker-compose.infra.yml" "./compose/docker-compose.infra.expose.yml")
            ;;
        # Add more configurations as needed
        *)
            echo "Unknown configuration: $config_alias"
            exit 1
            ;;
    esac

    # Construct the docker-compose command
    local compose_cmd="docker-compose"
    for file in "${config_files[@]}"; do
        compose_cmd+=" -f $file"
    done

    # Append the remaining arguments as the docker-compose command
    compose_cmd+=" $@"

    # Execute the command
    echo "Running command: $compose_cmd"
    eval $compose_cmd
}

# Check if at least two arguments are provided (config alias and docker-compose command)
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 {config_alias} {docker-compose command} [additional arguments]"
    exit 1
fi

# Run the command with the specified configuration
run_with_config "$@"
