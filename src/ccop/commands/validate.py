import click
from ccop.core import validator

@click.command(name="validate", help="Validate a commit message manually or from hook")
@click.argument("commit_msg_file", type=click.Path(exists=True))
def validate_command(commit_msg_file):
    with open(commit_msg_file, "r") as f:
        message = f.read().strip()

    is_valid, error_msg = validator.validate_commit_message(message)

    if is_valid:
        click.secho("✅ Commit message is valid!", fg="green")
    else:
        click.secho(f"❌ Invalid commit message:\n{error_msg}", fg="red")
        raise click.Abort()
