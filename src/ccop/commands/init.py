import click
from ccop.core import hooks

@click.command(name="init", help="Install Git commit-msg hook")
def init_command():
    """
    Initializes and installs the Git commit-msg hook in the local repository.

    This command attempts to install a commit-msg hook using the `hooks.install_local_commit_hook()` function.
    On successful installation, a success message is displayed in green.
    If installation fails, an error message is displayed in red with the exception details.

    Raises:
        Exception: If the hook installation fails.
    """
    try:
        hooks.install_local_commit_hook()
        click.secho("✅ commit-msg hook installed successfully.", fg="green")
    except Exception as e:
        click.secho(f"❌ Failed to install hook: {e}", fg="red")
