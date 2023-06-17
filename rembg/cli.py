import click

from . import _version
from .commands import command_functions


@click.group()
@click.version_option(version=_version.get_versions()["version"])
def main() -> None:
    pass


for command in command_functions:
    main.add_command(command)
