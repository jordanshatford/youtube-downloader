#!/bin/sh

# Exit scripts if command fails
set -e

# Run the API application with reloading enabled
dev()
{
    python3 -m venv venv
    . venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
    deactivate
}

# Run formatting on all code in the API app
format()
{
    python3 -m venv venv
    . venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install pre-commit
    python -m pip install -r requirements.txt
    pre-commit run --all-files
}

# Generate openapi.json from the app using the generate_openapi.py script
generate()
{
    python3 -m venv venv
    . venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    python generate_openapi.py
    deactivate
}

# Print help message to standard out
help()
{
    echo "Usage: $0 (dev|format|generate)"
    exit 1
}

# Run command based on user selection
case "$1" in
    dev)
        dev; ;;
    format)
        format; ;;
    generate)
        generate; ;;
    *)
        help; ;;
esac

# Exit with code from command used
exit $?
