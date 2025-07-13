#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    msg_file = sys.argv[1]
    
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath("src")  # Make sure it's absolute

    result = subprocess.run(["python", "-m", "ccop", "validate", msg_file], env=env)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
