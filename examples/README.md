# 🧪 Examples – OOPOA CLI

This directory contains example benchmark runs using the OOPOA CLI tool, along with pre-generated outputs and plotting commands.

---

## 📂 Structure

```bash
examples/
├── output_sample/
│   ├── ackley/        # Pre-generated CSV + PNG from Ackley function
│   ├── custom/        # Pre-generated output from user-defined custom function
│   ├── griewank/      # Pre-generated output from Griewank function
│   ├── rastrigin/     # Pre-generated output from Rastrigin function
│   └── sphere/        # Pre-generated output from Sphere function
├── run_ackley.sh      # Script to plot existing ackley.csv
├── run_custom.sh      # Script to plot existing custom.csv
├── run_griewank.sh    # Script to plot existing griewank.csv
├── run_rastrigin.sh   # Script to plot existing rastrigin.csv
└── run_sphere.sh      # Script to plot existing sphere.csv
```

---

## ▶️ How to Use

All `.sh` scripts plot **pre-generated** fitness `.csv` files stored under `output_sample/`. These scripts do not run the benchmark step.

Example:

```bash
bash run_sphere.sh
```

This will plot `output_sample/sphere/run_sphere.csv` using the CLI:

```bash
oopoa plot \
  --input output_sample/sphere/run_sphere.csv \
  --style dotted \
  --title "Sphere Convergence"
```

---

## 🔁 To Regenerate Output Files (Optional)

If you'd like to regenerate the `.csv` for a function:

```bash
oopoa benchmark -f benchmark/sphere.py -i 100 -N 30 -D 10 -lb -10 -ub 10
```

Then move the result to the appropriate `output_sample/<function>/` folder for consistency.

---

## 💡 Tip

Make sure your custom benchmark function returns a scalar (float), not a NumPy array, to ensure compatibility with the fitness logic.

---
