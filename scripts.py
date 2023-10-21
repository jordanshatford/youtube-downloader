"""
Script for managing and interacting with Python venvs. This is used in various
package.json to provide an easy script to perform actions like formating,
generating, and running dev server. This script supports all platforms.
"""
import argparse
import os
import platform
import subprocess
import venv

parser = argparse.ArgumentParser('venv scripts')
parser.add_argument(
    '--cwd',
    nargs='?',
    default=os.getcwd(),
    help="The CWD relative to this script. Default: DIR script is called from."
)
subparsers = parser.add_subparsers(dest='command', required=True)
run = subparsers.add_parser(
    'run', help='Run a command in the venv.'
)
run.add_argument('input', nargs='+')
pre_commit = subparsers.add_parser(
    'pre-commit', help='Run a pre-commit command in the venv.'
)
pre_commit.add_argument('script', choices=['run', 'autoupdate'])
args = parser.parse_args()

cwd = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    args.cwd
)

# Ensure initial venv is setup
venv_dir_path = os.path.join(cwd, 'venv')
venv.create(venv_dir_path, with_pip=True)

# Get path to bins in the venv
venv_bin_path = os.path.join(
    venv_dir_path,
    'Scripts' if platform.system() == 'Windows' else 'bin'
)

# Helper function to run a command with args in the venv
def venv_run(
    command: str, args: list[str],
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [
            os.path.join(venv_bin_path, command),
            *args,
        ], cwd=cwd,
    )

# Install dependencies if they exist in a requirements.txt file
venv_run('pip', ['install', '--upgrade', 'pip'])
if os.path.exists('requirements.txt'):
    venv_run('pip', ['install', '-r', 'requirements.txt'])

if args.command == 'pre-commit':
    # Ensure pre-commit is installed
    venv_run('pip', ['install', 'pre-commit'])
    if args.script == 'autoupdate':
        venv_run('pre-commit', ['autoupdate'])
    elif args.script == 'run':
        # Get a git tracked files in CWD to run pre-commit on.
        r = subprocess.run(
            ['git', 'ls-files'],
            capture_output=True,
            text=True,
            cwd=cwd
        )
        files = r.stdout.splitlines()
        venv_run('pre-commit', ['run', '--files'] + files)
elif args.command == 'run':
    venv_run(args.input[0], args.input[1:])
