import click
from ccop.core.validator import validate_commit_message

@click.command(name="validate", help="Manually validate a commit message.")
@click.argument("commit_msg_file", required=False)
@click.option("-m", "--message", help="Commit message to validate.")
def validate_command(commit_msg_file, message):
    # Read commit message from file if passed via hook
    if commit_msg_file:
        with open(commit_msg_file, "r") as f:
            message = f.read().strip()

    if not message:
        click.secho("❌ Error: No commit message provided.", fg="red")
        exit(1)

    is_valid, error = validate_commit_message(message)

    if is_valid:
        click.secho("✅ Commit message is valid!", fg="green")
        exit(0)
    else:
        click.secho("❌ Invalid commit message:", fg="red")
        click.secho(error, fg="yellow")
        exit(1)
