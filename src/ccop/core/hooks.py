import os
import shutil
from ccop.core.git_helper import find_git_root



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

def uninstall_hook():
    git_root = find_git_root()
    hook_path = os.path.join(git_root, ".git", "hooks", "commit-msg")

    if os.path.exists(hook_path):
        os.remove(hook_path)
        return True
    return False

