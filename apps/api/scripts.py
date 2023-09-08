import argparse
import os
import platform
import subprocess
import venv


# Parse command called from package.json
parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['dev', 'format', 'generate'])
args = parser.parse_args()

# Setup and install required packages into venv
cwd = os.getcwd()
venv_name = 'venv'
venv_dir = os.path.join(cwd, venv_name)
venv_bin = os.path.join(venv_dir, 'bin')
# On windows it appears to be in another directory
if platform.system() == 'Windows':
    venv_bin = os.path.join(venv_dir, 'Scripts')
venv_bin_pip = os.path.join(venv_bin, 'pip')
venv.create(venv_dir, with_pip=True)
subprocess.run([venv_bin_pip, 'install', '--upgrade', 'pip'], cwd=cwd)
subprocess.run(
    [
        venv_bin_pip, 'install', '-r',
        os.path.abspath('requirements.txt'),
    ], cwd=cwd,
)

if args.command == 'dev':
    # Run the API application with reloading enabled
    subprocess.run(
        [
            os.path.join(venv_bin, 'uvicorn'), 'app.main:app',
            '--host', '0.0.0.0', '--port', '8080', '--reload',
        ], cwd=cwd,
    )
elif args.command == 'format':
    # Install pre-commit and run formatting on all code in the API app
    subprocess.run([venv_bin_pip, 'install', 'pre-commit'], cwd=cwd)
    subprocess.run(
        [
            os.path.join(venv_bin, 'pre-commit'),
            'run', '--all-files',
        ], cwd=cwd,
    )
elif args.command == 'generate':
    # Generate openapi.json from the app using the generate_openapi.py script
    subprocess.run(
        [
            os.path.join(venv_bin, 'python'),
            'generate_openapi.py',
        ], cwd=cwd,
    )
