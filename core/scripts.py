import argparse
import os
import platform
import subprocess
import venv


# Parse command called.
parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['format'])
args = parser.parse_args()


# Setup the initial venv.
venv_dir = os.path.join(os.getcwd(), 'venv')
venv.create(venv_dir, with_pip=True)


# Get path to bins in the venv.
venv_bin_dir = 'Scripts' if platform.system() == 'Windows' else 'bin'
venv_bin = os.path.join(venv_dir, venv_bin_dir)


# Run a command with passed args in the venv.
def venv_run(
    command: str, args: list[str],
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [
            os.path.join(venv_bin, command),
            *args,
        ], cwd=os.getcwd(),
    )


# Install project dependencies.
venv_run('pip', ['install', '--upgrade', 'pip'])
# venv_run('pip', ['install', '.'])


if args.command == 'format':
    # Run pre-commit hooks on the api code.
    venv_run('pip', ['install', 'pre-commit'])
    venv_run('pre-commit', ['run', '--all-files'])
