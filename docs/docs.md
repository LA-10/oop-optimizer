# 🛠 Developer Guide – OOPOA CLI

This document outlines the internal structure, key modules, and extension points of the OOPOA CLI.

---

## 🧱 Project Architecture

```bash
oopoa-cli/
├── core/              # Main algorithm and fitness logic
│   ├── optimizer.py   # Optimization loop (entry: optimizer_code)
│   └── population.py  # Parent/child generation, fitness evaluation
├── benchmark/         # Predefined benchmark functions
├── cli/               # Click CLI structure
│   ├── main.py        # Entry group for CLI
│   └── commands/      # Subcommands: benchmark, plot
│       └── __init__.py# Command registration
├── plots/             # Plot styling and saving utilities
├── results/           # Auto-generated CSVs and images
├── examples/          # Sample outputs and run scripts
└── tests/             # (Planned) test coverage
```

---

## 🔍 Core Components

### `optimizer_code`

Located in `core/optimizer.py`

* Executes the full OOPOA optimization loop
* Accepts objective function, iteration count, population size, mutation rate, and bounds
* Maintains best fitness record and updates the population accordingly

### `evaluate_fitness`

Located in `core/population.py`

* Evaluates a single solution using the provided benchmark function
* Wraps the result as a float to ensure compatibility

### `create_parent` / `create_child`

Located in `core/population.py`

* Construct new individuals from existing population using OOPOA rules:

  * Public → use own gene
  * Protected → borrow from another solution
  * Private → reinitialize gene randomly

### `mutation`

Randomizes part of the status vector using mutation rate (MR), affecting next-generation strategy.

---

## 🔌 Extending the Tool

### ➕ Adding a New Benchmark Function

1. Create a file in `benchmark/` (e.g. `levy.py`)
2. Define a function named identically to the file name (e.g. `def levy(solution):`)
3. Ensure it returns a scalar (float)
4. Run it using: `oopoa benchmark -p benchmark/levy.py`

### ✳️ Adding a New CLI Command

1. Create a new file in `cli/commands/`
2. Register the command in `cli/commands/__init__.py`
3. Add it to `cli/main.py` using `cli.add_command()`
4. Follow existing examples (`@click.command()`)

---

## 🧪 Development Tips

* Benchmark functions **must return float**, not NumPy arrays
* For CLI messages, use `click.echo()` instead of `print()`
* Use `Path` and `importlib.util` for importing custom functions
* If results are inconsistent, inspect `status_vector` and fitness comparisons in `optimizer.py`

---

## 📥 Contribution Path

For contribution guidelines, see [`CONTRIBUTING.md`](../CONTRIBUTING.md)

For algorithm design, see [`docs/how_it_works.md`](how_it_works.md)

---
