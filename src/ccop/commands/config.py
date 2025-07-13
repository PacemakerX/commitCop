import click
from ccop.core.config import load_config, save_config

@click.group()
def config_command():
    """Modify types or scopes in default.yaml."""
    pass

@config_command.command("add")
@click.argument("field", type=click.Choice(["type", "scope"]))
@click.argument("value")
def add_value(field, value):
    """Add a type or scope."""
    config = load_config()
    section = "types" if field == "type" else "scopes"
    values = config["yamlformat"].get(section, [])

    if value in values:
        click.secho(f"⚠️ {field} '{value}' already exists.", fg="yellow")
        return

    values.append(value)
    config["yamlformat"][section] = sorted(values)
    save_config(config)
    click.secho(f"✅ Added {field}: {value}", fg="green")

@config_command.command("remove")
@click.argument("field", type=click.Choice(["type", "scope"]))
@click.argument("value")
def remove_value(field, value):
    """Remove a type or scope."""
    config = load_config()
    section = "types" if field == "type" else "scopes"
    values = config["yamlformat"].get(section, [])

    if value not in values:
        click.secho(f"⚠️ {field} '{value}' not found.", fg="yellow")
        return

    values.remove(value)
    config["yamlformat"][section] = sorted(values)
    save_config(config)
    click.secho(f"✅ Removed {field}: {value}", fg="green")

@config_command.command("list")
def list_values():
    """List current commit types and scopes."""
    config = load_config()
    types = config["yamlformat"].get("types", [])
    scopes = config["yamlformat"].get("scopes", [])
    click.echo()
    click.secho("🛠️  Allowed commit types:", fg="cyan", bold=True)
    if types:
        click.echo("  " + " | ".join(types))
    else:
        click.echo("  (none)")

    click.echo()
    click.secho("📦 Allowed commit scopes:", fg="cyan", bold=True)
    if scopes:
        click.echo("  " + " | ".join(scopes))
    else:
        click.echo("  (none)")
    click.echo()
