import click
from .commands import benchmark, plot

@click.group()
def cli():
    """OOPOA CLI Tool"""
    pass

cli.add_command(benchmark)
cli.add_command(plot)
