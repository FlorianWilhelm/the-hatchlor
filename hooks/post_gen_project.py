import subprocess

try:
    subprocess.call(['git', 'init', '--initial-branch', 'main'])
    subprocess.call(['git', 'commit', '--allow-empty', '-m', 'Root commit'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit from Cookiecutter template'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_repo }}'])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print("Make sure to manually set up a git repository which is necessary for `hatch-vcs`")
