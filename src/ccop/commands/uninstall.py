import click
from ccop.core.hooks import uninstall_hook

@click.command(name="uninstall", help="Remove Git commit-msg hook from local repo.")
def uninstall_command():
    removed = uninstall_hook()

    if removed:
        click.secho("🗑️ commit-msg hook removed successfully.", fg="green")
    else:
        click.secho("⚠️ No commit-msg hook found to remove.", fg="yellow")
