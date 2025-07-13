from ccop.core.config import load_config
import re

def validate_commit_message(message):
    config = load_config()
    pattern = config["yamlformat"]["pattern"]
    types = config["yamlformat"]["types"]
    scopes = config["yamlformat"]["scopes"]

    match = re.match(pattern, message)
    if not match:
        return False, "Message must follow the format: type(scope): description"

    msg_type = match.group(1)
    msg_scope = match.group(2)

    if msg_type not in types:
        return False, f"Invalid type: '{msg_type}'. Allowed: {', '.join(types)}"
    if msg_scope not in scopes:
        return False, f"Invalid scope: '{msg_scope}'. Allowed: {', '.join(scopes)}"

    return True, ""
