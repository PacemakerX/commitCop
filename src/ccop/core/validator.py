import re

ALLOWED_TYPES = {"feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert", "init", "security"}
ALLOWED_SCOPES = {"api", "db", "auth", "docs", "cli", "ui", "core", "utils", "infra", "config", "deps", "test", "repo"}

def validate_commit_message(message):
    types = "|".join(ALLOWED_TYPES)
    scopes = "|".join(ALLOWED_SCOPES)

    # No underscore between type and (scope)
    pattern = rf"^({types})\(({scopes})\): .+"

    if not re.match(pattern, message):
        return False, "Message must match pattern: <type>(<scope>): <message>"

    return True, ""
