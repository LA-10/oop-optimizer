import click
import matplotlib.pyplot as plt
from ..plots.graph import graph
import pandas as pd
from pathlib import Path
import os
from colorama import Fore


@click.command()
@click.argument('inputs', nargs=-1)

@click.option('--style', '-s', default='solid', help='Plot style')
@click.option('--title', default='Convergence Curve', help='Custom plot title')
@click.option('--grid', default=True, help='Toggle grid display') # Same as Show
@click.option('--save', default=False, help="Save plot to file") # Same as show
@click.option('--show', default=True, help="Whether to show the plot window") #Change to --show/--no-show
@click.option('--dpi', default=100, help="Set resolution of saved figure")

def plot(inputs, style, title, grid, save, show, dpi):
    """Plot convergence curve from results."""
    def validate_input(inputs):
        """check if input supplied correct"""
        if len(inputs) == 0:
            print(f"{Fore.RED}ERROR: no input supplied")
            exit(1)
        else:
            valid_input = []

            for input in inputs:
                if os.path.isfile(input):
                    valid_input.append(input)
                else:
                    print(f"{Fore.YELLOW}WARNING: ignoring '{input}' as it is invalid")

            if len(valid_input) == 0:
                print(f"{Fore.RED}ERROR: no valid input supplied")
                exit(1)
            
            return valid_input
    inputs = validate_input(inputs)

    fig = graph(inputs, style, title, grid, show)

    if save:
        name = Path(input).stem
        os.makedirs("results/graphs", exist_ok=True)
        path = f"results/graphs/{name}.png"

        fig.savefig(path, dpi=dpi)
        print(f"{Fore.GREEN}Plot saved as {path}")

    plt.close()
