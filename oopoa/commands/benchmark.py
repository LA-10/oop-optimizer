import click
import importlib
import sys
import csv
from pathlib import Path
from datetime import datetime
from colorama import Fore
from ..core.optimizer import optimizer_code

benchmark_dict = {'sphere': 'benchmark/sphere.py', 'ackley':'benchmark/ackley.py', 'griewank': 'benchmark/griewank.py', 'ratrigin': 'benchmark/rastrigin.py'}

@click.command()
@click.option('--func', '-f', type=click.Choice(benchmark_dict, case_sensitive=False), default = 'sphere', help='choose a default function')
@click.option('--custom', '-c', default = 'None', help='file path to the custom function file')
@click.option('--max-iter', '-i', default=100, help='Maximum iterations')
@click.option('--population-size', '-N', default=30, help='Number of solutions')
@click.option('--dimension', '-D', default = 10, help='Number of variables in each solution')
@click.option('--lower-bound', '-lb', default=0, help='Lower bound of each variable')
@click.option('--upper-bound', '-ub', default=10, help='Upper bound of each variable')
@click.option('--mutation-rate', '-MR', default = 0.5, help='Mutation probability in range [0.1, 0.99]')


def benchmark(max_iter, population_size, dimension, lower_bound, upper_bound, mutation_rate, func, custom):
    """Run OOPOA on a selected benchmark function."""
    def import_path(path, name=None):
        if name is None:
                try:     
                    name = Path(path).stem
                except Exception as e:
                    print(f"{Fore.RED}ERROR (parsing name from path):", e)
                    exit(1)
        try:
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"{Fore.RED}ERROR (importing module):", e)
            exit(1)

        if not hasattr(module, name):
            print(f"{Fore.RED}ERROR: No function named '{name}' in '{path}'")
            exit(1)

        return  getattr(module, name)
    def arguments_check():
        if max_iter < 1:
            print(f"{Fore.RED}ARGUMENT ERROR: max_iter (-i) should be >1")
        elif population_size < 1:
            print(f"{Fore.RED}ARGUMENT ERROR: --population-size (-N) should be > 1")
        elif dimension < 1:
            print(f"{Fore.RED}ARGUMENT ERROR: --dimention (-D) should be >1")
        elif upper_bound < lower_bound:
            print(f"{Fore.RED}ARGUMENT ERROR: --upper-bound (-ub) should be less than --lower-bound (-lb)")
        elif not(0.1 <= mutation_rate <= 0.9):
            print(f"{Fore.RED}ARGUMENT ERROR: --mutation_rate (-MR) should be between [0.1, 0.9]")
        else:
            return 
        
        exit(1)

    if custom != 'None':
        func = import_path(path=custom)
    else:
        func = benchmark_dict.get(func)
        func = import_path(path=func)

    print(f"{Fore.GREEN}Successfully imported: {func.__name__}")

    arguments_check()

    fitness_level = optimizer_code(
        max_iter, population_size, dimension, lower_bound, upper_bound, mutation_rate, func
    )

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"results/cvs/run_{func.__name__}_{timestamp}.csv"
    try:
        with open(filename, 'w', newline='') as csvfile:
            fitness_writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fitness_writer.writerow(['iterations', 'fitness_level'])

            for i in range(len(fitness_level)):
                fitness_writer.writerow([i] + [f"{fitness_level[i]}"])
        
        print(f"{Fore.GREEN}Successfully benchmarked: {filename}")
    except Exception as e:
        print(f"{Fore.RED}ERROR: (cvs_file_error): ", e)




