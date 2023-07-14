#!/bin/sh

# Prepare the environment for the user
prepare()
{   
    # Clean to return enviroment to original state
    clean
    # Install pre-commit hooks
    pre-commit install
    # Setup virtual enviroment for use in other commands
    python3 -m venv venv && source venv/bin/activate && python3 -m pip install -r requirements.txt && deactivate
}

# Run the backend application
run()
{
    # Enter the virtual environment and run the application
    source venv/bin/activate && python3 main.py
}

# Run formatting on the backend code
format()
{
    # Run pre-commit on all files
    pre-commit run --all-files
}

# Clean up existing virtualenv and uninstall pre-commit hooks. This is used to return
# the environment to its original state.
clean()
{
    # Uninstall any pre-commit hooks
    pre-commit uninstall
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
    run)
        run; ;;
    format)
        format; ;;
    clean)
        clean; ;;
    *)
        help; ;;
esac

# Exit with code from command used
exit $?
