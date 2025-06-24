# 📟 OOPOA CLI – Command Documentation

This document describes the available commands and options in the `oopoa` CLI tool.

---

## 🔧 `benchmark` – Run Optimization

Run the OOPOA algorithm on a selected benchmark function and generate a `.csv` file with the fitness values over iterations.

```bash
oopoa benchmark [OPTIONS]
```

### 📅 Options

| Option                    | Description                                               | Default  |
| ------------------------- | --------------------------------------------------------- | -------- |
| `--function`, `-f`        | Name of the benchmark function (`sphere`, `ackley`, etc.) | `sphere` |
| `--max-iter`, `-i`        | Maximum number of iterations                              | `100`    |
| `--population-size`, `-N` | Number of solutions in the population                     | `30`     |
| `--dimension`, `-D`       | Number of variables per solution                          | `10`     |
| `--mutation-rate`, `-MR`  | Mutation rate (`0.1` to `0.99`)                           | `0.9`    |
| `--lower-bound`, `-lb`    | Lower bound for each variable                             | `-10`    |
| `--upper-bound`, `-ub`    | Upper bound for each variable                             | `10`     |

### 📝 Output

* CSV file saved to `results/csv/run_<function>_<date>_<hour>-<minute>-<second>.csv` containing:

  * `iterations`: iteration number
  * `fitness_level`: best fitness at that iteration

### 📌 Example

```bash
oopoa benchmark -f benchmark/ackley.py -i 200 -N 50 -D 20 -MR 0.8 -lb -32 -ub 32
```

---

## 📈 `plot` – Visualize Convergence Curve

Plots the fitness log (from a `.csv`) and optionally saves it as a `.png`.

```bash
oopoa plot [OPTIONS]
```

### 📅 Options

| Option          | Description                                             | Default                |
| --------------- | ------------------------------------------------------- | ---------------------- |
| `--input`, `-i` | Path to the fitness `.csv` file                         | *(required)*           |
| `--style`, `-s` | Matplotlib style (e.g. `ggplot`, `seaborn`)             | `ggplot`               |
| `--title`       | Title of the plot                                       | `"Convergence Curve"`  |
| `--grid`        | Enable grid lines  (e.g. True/False)                    | `True`                 |
| `--save`        | Save plot to file path (e.g. True/False)                | `True`                 |
| `--show`        | Show the plot in a window                               | `True`                 |
| `--dpi`         | Resolution of the saved plot (dots per inch)            | `100`                  |

### 📌 Example

```bash
oopoa plot -i results/csv/sphere.csv --style solid --title "Sphere Fitness" --save True
```

---

## ℹ️ Notes

* Function names must match implemented files in the `benchmark/` directory
* Custom benchmark functions can be supported in future versions
* Plots rely on `matplotlib` and `pandas`

---

## 🛠 Future Commands (Planned)

| Command   | Description                                 |
| --------- | ------------------------------------------- |
| `export`  | Export summary of multiple runs (v0.2)      |
| `compare` | Plot multiple convergence graphs together   |
| `config`  | Load run parameters from `.json` or `.yaml` |

See [`roadmap.md`](../roadmap.md) for development progress.

---
