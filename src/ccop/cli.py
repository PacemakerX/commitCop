import click
from ccop.commands.init import init_command
from ccop.commands.validate import validate_command
from ccop.commands.uninstall import uninstall_command
from ccop.commands.format import format_command
from ccop.commands.config import config_command

@click.group(help="🐶 ccop: Git commit message enforcer")
@click.version_option("0.1.0", prog_name="ccop")
def cli():
    pass

cli.add_command(init_command)
cli.add_command(validate_command)
cli.add_command(uninstall_command)
cli.add_command(format_command)
cli.add_command(config_command, name="config")