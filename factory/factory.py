""" The command line project factory tool """

__version__ = '0.0.1'

import click

from .cli import make_cli
from .project import make_project


@click.group()
@click.option('--debug', default=False)
def main(debug):
    """ This is the main command line tool """
    click.echo('Debug mode is {}'.format(debug))


@main.command()
def cli():
    """ This command makes a CLI """
    make_cli()


@main.command()
def project():
    """ This command makes a barebones project """
    make_project()
