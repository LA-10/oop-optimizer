import matplotlib.pyplot as plt
from colorama import Fore
import pandas as pd 
import string

def graph(inputs, style, title, grid, show):
    # Extract data
    
    cvs_file = []
    for input in inputs:
        try:
            df = pd.read_csv(input)

            cvs_file.append(df)
        except Exception as e: 
            print(f"{Fore.YELLOW}WARNING: Cannot read csv file '{input}")
            inputs.remove(input)

            

    if len(cvs_file) == 0:
        print(f"{Fore.RED}ERROR: Cannot read file")
        exit(1)

    fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
    ax.set_title(title)

    # Create the plot
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Fitness Level")

    for i in range(len(cvs_file)):
        print(f"{Fore.GREEN}[Plot] Plotting {inputs[i]} with style {style}")

        x = cvs_file[i]['iterations']
        y = cvs_file[i]['fitness_level']
        

        try:
            ax.plot(x, y, label=inputs[i].split('_')[1], linestyle=style)
        except Exception as e:
            print("ERROR: plot_error: ", e)
            exit(1)

        ax.grid(grid)

    if len(inputs) > 1:
        fig.legend()


    if show:
        plt.show()

    return fig

