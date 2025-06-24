import click
import matplotlib.pyplot as plt
from plots.graph import graph
import pandas as pd
from pathlib import Path
import os

@click.command()
@click.option('--input', '-i', required=True, help='Path to fitness log file')
@click.option('--style', '-s', default='solid', help='Plot style')
@click.option('--title', default='Convergence Curve', help='Custom plot title')
@click.option('--grid', default=True, help='Toggle grid display')
@click.option('--save', default=False, help="Save plot to file")
@click.option('--show', default=True, help="Whether to show the plot window")
@click.option('--dpi', default=100, help="Set resolution of saved figure")

def plot(input, style, title, grid, save, show, dpi):
    """Plot convergence curve from results."""

    try:
        df = pd.read_csv(input)
    except Exception as e: 
        print(f"❌ ERROR: Cannot read file: {e}")
        exit(1)

    print(f"[Plot] Plotting {input} with style {style}")

    fig = graph(df, style, title, grid, show)

    if save:
        name = Path(input).stem
        os.makedirs("results/graphs", exist_ok=True)
        path = f"results/graphs/{name}.png"
        fig.savefig(path, dpi=dpi)
        print(f"✅ Plot saved as {path}")

    plt.close(fig)