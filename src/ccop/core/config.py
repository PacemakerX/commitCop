import os
import yaml

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", ".."))
DEFAULT_CONFIG_PATH = os.path.join(PROJECT_ROOT, "configs", "default.yaml")

def load_config():
    with open(DEFAULT_CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)
    
def save_config(config):
    with open(DEFAULT_CONFIG_PATH, "w") as f:
        yaml.dump(config, f, sort_keys=False)