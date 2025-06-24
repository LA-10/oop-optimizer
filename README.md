# 🧠 OOPOA CLI – Object-Oriented Programming Optimization Algorithm

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/your-username/oopoa-cli.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Version](https://img.shields.io/badge/version-0.1.0-orange)
![Platform](https://img.shields.io/badge/platform-cli-lightgrey)

[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI - Coming Soon](https://img.shields.io/badge/pypi-coming%20soon-yellow)](https://pypi.org/)


**OOPOA CLI** is a research-grade command-line tool that fully implements the **Object-Oriented Programming Optimization Algorithm (OOPOA)** — a novel metaheuristic introduced in 2024.

The original paper presented only **high-level pseudocode and performance graphs**. This CLI bridges that gap by offering:

- 📌 A **complete implementation** of the algorithm logic
- 🔬 **Reproducible benchmarking** across standard test functions
- 📊 **Exportable logs** and **convergence plots**
- 🧠 **Clear math documentation** and **customizable settings**

> Ideal for students, researchers, and developers working in optimization and metaheuristics.

---

## 📖 Original Paper Reference

> Hosny, K.M., Khalid, A.M., Said, W., Elmezain, M., & Mirjalili, S. (2024).  
> *A novel metaheuristic based on object-oriented programming concepts for engineering optimization.*  
> *Alexandria Engineering Journal.* [DOI: 10.1016/j.aej.2024.04.060](https://doi.org/10.1016/j.aej.2024.04.060)

---

## 🚀 Features

- 🔧 Run OOPOA on standard benchmark functions (Sphere, Ackley, Rastrigin, etc.)
- 📉 Plot convergence graphs and export them to `.png`
- 🧮 Log results per iteration in `.csv` for reproducible analysis
- 🖋 Customizable: population size, mutation rate, bounds, and more
- 🧱 Modular codebase for easy extension (custom functions, batch runs, etc.)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/oopoa-cli.git
cd oopoa-cli
pip install -e .
```

Then run the tool:

```bash
oopoa --help
```

---

## 📁 Project Structure

```bash
oopoa-cli/
├── cli/               # Command-line interface (Click)
├── core/              # Algorithm logic and solution objects
├── benchmark/         # Standard benchmark functions
├── plots/             # Plotting utilities
├── examples/          # CLI usage examples
├── results/           # Auto-generated fitness logs and plots
├── docs/              # Math notes, roadmap, and usage docs
└── tests/             # (planned) unit tests
```

---

## 🧪 Examples

```bash
    examples/run_sphere.sh
```


More CLI examples can be found in the [`examples/`](./examples) folder.

---

## 🧠 Mathematical Basis

OOPOA simulates OOP principles during optimization:

| Status      | Meaning                                |
|-------------|----------------------------------------|
| 0 (public)  | Use individual’s own value             |
| 1 (protected) | Inherit value from another solution   |
| 2 (private) | Generate new random value              |

See [`docs/math.md`](./docs/math.md) for full derivation and update rules.

---

## 🧾 Citation & Credits

This implementation is based on:

> Hosny, K.M., Khalid, A.M., Said, W., Elmezain, M., & Mirjalili, S. (2024).  
> *A novel metaheuristic based on object-oriented programming concepts for engineering optimization.*  
> Alexandria Engineering Journal. [DOI](https://doi.org/10.1016/j.aej.2024.04.060)

Please cite the paper if this tool supports your work.
This implementation was independently developed based on the pseudocode and descriptions in the paper.

---

## 🛣 Roadmap

Planned additions (see `docs/roadmap.md`):

- 📊 Plotting multiple runs
- 🧾 Config-based runs (`.json`, `.yaml`)
- 📈 Summary tables for performance across runs
- 🔁 Comparison with other metaheuristics

---

## 💬 Feedback & Contributions

If you've used this tool, found a bug, or want to improve it—open an issue or submit a pull request. Contributions welcome!

---

## 📄 License

Licensed under the **MIT License**. See [`LICENSE`](./LICENSE) for details.
