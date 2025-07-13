import os

def find_git_root(path=None):
    """
    Walk upward from current path until .git is found.
    """
    path = path or os.getcwd()
    while path != os.path.dirname(path):
        if os.path.isdir(os.path.join(path, ".git")):
            return path
        path = os.path.dirname(path)
    raise FileNotFoundError("No .git directory found. Are you inside a Git repository?")
