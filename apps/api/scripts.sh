#!/bin/bash

# Exit scripts if command fails
set -e

# Location for venv
VENV_PATH=venv/bin/activate

# Prepare the environment for the user
prepare()
{
    # Clean to return enviroment to original state
    clean
    # Setup virtual enviroment and install dependencies
    python3 -m venv venv
    source $VENV_PATH
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    # Install pre-commit hooks
    python -m pip install pre-commit
    pre-commit install
    deactivate
}

# Run the API in dev mode
dev()
{
    # Enter the virtual environment and run the application
    source $VENV_PATH
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
    deactivate
}

# Run formatting on the API code
format()
{
    # Run pre-commit on all files
    source $VENV_PATH
    pre-commit run --all-files
    deactivate
}

# Generate openapi.json from the API app
generate()
{
    # Enter the virtual environment and run the generation script
    source $VENV_PATH
    python generate_openapi.py
    deactivate
}

# Clean up existing virtualenv and uninstall pre-commit hooks. This is used to return
# the environment to its original state.
clean()
{
    # Uninstall any pre-commit hooks
    source $VENV_PATH
    pre-commit uninstall
    deactivate
    # Remove virtual environment
    rm -rf venv/
}

# Print help message to standard out
help()
{
    echo "Usage: $0 (prepare|run|format|clean|help)"
    exit 1
}

# Run command based on user selection
case "$1" in
    prepare)
        prepare; ;;
    generate)
        generate; ;;
    dev)
        dev; ;;
    format)
        format; ;;
    clean)
        clean; ;;
    *)
        help; ;;
esac

# Exit with code from command used
exit $?
