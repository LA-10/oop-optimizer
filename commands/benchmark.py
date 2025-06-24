import click
import importlib
import sys
import csv
from pathlib import Path
from datetime import datetime
from core.optimizer import optimizer_code


@click.command()
@click.option('--path', '-p', default='benchmark/sphere.py', help='file path to the function file')
@click.option('--max-iter', '-i', default=100, help='Maximum iterations')
@click.option('--population-size', '-N', default=30, help='Number of solutions')
@click.option('--dimension', '-D', default = 10, help='Number of variables in each solution')
@click.option('--lower-bound', '-lb', default=0, help='Lower bound of each variable')
@click.option('--upper-bound', '-ub', default=10, help='Upper bound of each variable')
@click.option('--mutation-rate', '-MR', default = 0.5, help='Mutation probability in range [0.1, 0.99]')

def benchmark(max_iter, population_size, dimension, lower_bound, upper_bound, mutation_rate, path):
    """Run OOPOA on a selected benchmark function."""
    def import_path(name=None):
        if name is None:
                try:
                    name = Path(path).stem
                except Exception as e:
                    print("ERROR (parsing name from path):", e)
                    exit(1)

        try:
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
        except Exception as e:
            print("ERROR (importing module):", e)
            exit(1)

        if not hasattr(module, name):
            print(f"ERROR: No function named '{name}' in '{path}'")
            exit(1)

        return  getattr(module, name)

    func = import_path()
    print(f"Successfully imported: {func.__name__}")

    if max_iter < 1 or population_size < 1 or dimension< 1 or upper_bound < lower_bound or not(mutation_rate >= 0.1 and mutation_rate <= 0.99):
        print("ERROR: invalid argument(s)")
        exit(1)
    
    fitness_level = optimizer_code(
        max_iter, population_size, dimension, lower_bound, upper_bound, mutation_rate, func
    )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"results/cvs/run_{func.__name__}_{timestamp}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fitness_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fitness_writer.writerow(['iterations', 'fitness_level'])

        for i in range(len(fitness_level)):
            fitness_writer.writerow([i] + [f"{fitness_level[i]}"])
    
    print(f"Successfully benchmarked: {filename}")
    




