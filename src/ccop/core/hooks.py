import os
import shutil

def find_git_root():
    current = os.getcwd()
    while current != os.path.dirname(current):
        if os.path.isdir(os.path.join(current, ".git")):
            return current
        current = os.path.dirname(current)
    return None

def install_local_commit_hook():
    git_root = find_git_root()
    if not git_root:
        raise Exception("Not inside a Git repository")

    hook_dst = os.path.join(git_root, ".git", "hooks", "commit-msg")
    hook_src = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../templates/commit-msg.py")
    )

    shutil.copyfile(hook_src, hook_dst)
    os.chmod(hook_dst, 0o775)
