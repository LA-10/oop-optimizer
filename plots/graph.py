import matplotlib.pyplot as plt

def graph(cvs_file, style, title, grid, show):
    # Extract data
    x = cvs_file['iterations']
    y = cvs_file['fitness_level']

    # Create the plot
    fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
    ax.set_title(title)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Fitness Level")
    
    try:
        ax.plot(x, y, label='Fitness', linestyle=style)
    except Exception as e:
        print("ERROR: plot_error: ", e)
        exit(1)

    ax.grid(grid)


    if show:
        plt.show()

    return fig

