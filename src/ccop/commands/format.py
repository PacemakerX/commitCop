# src/ccop/commands/format.py

import click
from ccop.core.config import load_config

@click.command("format")
@click.option('--types', '-t', multiple=True, help="Show only specified types.")
@click.option('--scopes', '-s', multiple=True, help="Show only specified scopes.")
def format_command(types, scopes):
    """Show the valid commit message format and examples based on config."""
    config = load_config()
    format_cfg = config.get("yamlformat", {})

    all_types = format_cfg.get("types", [])
    all_scopes = format_cfg.get("scopes", [])

    # Filter types and scopes if options are provided
    shown_types = list(types) if types else all_types
    shown_scopes = list(scopes) if scopes else all_scopes

    click.echo("\n🎯 Expected commit message format:")
    click.secho(f"   type(scope): description", fg="green")

    # Print only 5-6 types and scopes side by side at the end
    click.echo("\n✅ Allowed types & scopes (showing 6):")
    max_len = min(6, max(len(shown_types), len(shown_scopes)))
    for i in range(max_len):
        t = shown_types[i] if i < len(shown_types) else ""
        s = shown_scopes[i] if i < len(shown_scopes) else ""
        click.echo(f"   - {t:<15} | {s}")

    if len(shown_types) > 6 or len(shown_scopes) > 6:
        click.echo("   ...")

    click.echo("\n🧪 Example valid commit messages:")
    for i in range(min(3, max_len)):
        t = shown_types[i] if i < len(shown_types) else "add"
        scope = shown_scopes[i % len(shown_scopes)] if shown_scopes else "general"
        click.echo(f"   {t}({scope}): Add something meaningful")

    click.echo()
