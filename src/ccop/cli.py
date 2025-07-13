import click
from ccop.commands.init import init_command
from ccop.commands.validate import validate_command

@click.group(help="🐶 ccop: Git commit message enforcer")
@click.version_option("0.1.0", prog_name="ccop")
def cli():
    pass

cli.add_command(init_command)
cli.add_command(validate_command)
