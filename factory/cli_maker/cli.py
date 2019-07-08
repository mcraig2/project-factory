""" The {NAME} command line tool """

__version__ = '0.0.1'

import click

from .command1 import run_no_arg
from .command2 import run_list_args
from .command3 import run_kwargs


@click.group()
@click.option('--debug', default=False)
def main(debug):
    """ This is the main entry point to the CLI """
    click.echo('Debug mode is {{}}'.format(debug))


@main.command()
def no_arg():
    """ This is an example of a no-argument entry """
    run_no_arg()


@main.command()
@click.argument('args', nargs=-1)
def list_args(args):
    """ This is an example of a list of args """
    run_list_args(args)


@main.command()
@click.option('--kwargs', prompt='Enter kwarg', help='The kwarg to pass')
def kwargs(kwargs):
    """ This is an example of a keyword argument """
    run_kwargs(kwargs)
