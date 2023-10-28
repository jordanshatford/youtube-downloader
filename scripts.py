"""
Script for managing and interacting with Python venvs. This is used in various
package.json to provide an easy script to perform actions like formating,
generating, and running dev server. This script supports all platforms. This
will create a single venv in the project root to be used for various apps and
packages. These should not have conflicts dependencies.
"""
import argparse
import os
import platform
import subprocess
import venv


# Parse command line args
parser = argparse.ArgumentParser(
    'venv management scripts (internal use)', add_help=False
)
subparsers = parser.add_subparsers(dest='command', required=True)
# Run command in generic and will allow runing anything from within the venv
run = subparsers.add_parser('run', add_help=False)
# Pre-commit currently has custom commands to allow use to specific git tracked files of CWD
pre_commit = subparsers.add_parser('pre-commit', add_help=False)
pre_commit.add_argument('script', choices=['run', 'autoupdate'])
args, rest = parser.parse_known_args()


# Run subprocess and get output as string
def run_subprocess(
    args: list[str],
    *,
    bin_path: str | None = None,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    # When path for bin is passed ensure we are running that
    if bin_path is not None:
        args = [os.path.join(bin_path, args[0]), *args[1:]]
    return subprocess.run(
        args,
        cwd=os.getcwd(),
        check=True,
        capture_output=capture_output,
        text=True,
    )


# Get root directory of git repository. Create venv in root of git repository
result = run_subprocess(
    ['git', 'rev-parse', '--show-toplevel'], capture_output=True
)
workspace_dir =result.stdout.splitlines()[0]

# Create venv if not already there
venv_dir_path = os.path.join(workspace_dir, 'venv')
venv.create(venv_dir_path, with_pip=True)

# Get path to bins in the venv (different location on windows)
venv_bin_path = os.path.join(
    venv_dir_path,
    'Scripts' if platform.system() == 'Windows' else 'bin'
)


try:
    # Ensure pip is up to date and install any requirements
    run_subprocess(
        ['pip', 'install', '--upgrade', 'pip'], bin_path=venv_bin_path
    )
    if os.path.exists('requirements.txt'):
        run_subprocess(
            ['pip', 'install', '-r', 'requirements.txt'],
            bin_path=venv_bin_path
        )

    if args.command == 'pre-commit':
        # Ensure pre-commit is installed
        run_subprocess(['pip', 'install', 'pre-commit'], bin_path=venv_bin_path)
        if args.script == 'autoupdate':
            run_subprocess(['pre-commit', 'autoupdate'], bin_path=venv_bin_path)
        elif args.script == 'run':
            # Get a git tracked files in CWD to run pre-commit on
            result = run_subprocess(
                ['git', 'ls-files'], capture_output=True
            )
            files = result.stdout.splitlines()
            run_subprocess(
                ['pre-commit', 'run', '--files'] + files, bin_path=venv_bin_path
            )
    elif args.command == 'run':
        run_subprocess(rest, bin_path=venv_bin_path)
except subprocess.CalledProcessError as e:
    raise SystemExit(1)
