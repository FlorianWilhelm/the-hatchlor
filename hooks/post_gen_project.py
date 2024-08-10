import subprocess

try:
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_repo }}'])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print("Makre sure to manually set up a git repository which is necessary for `hatch-vcs`")
