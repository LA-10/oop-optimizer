#!/bin/bash

# ------------------------------------------------------
# Example: Plotting the pre-generated Griewank benchmark results
# ------------------------------------------------------

# The CSV file was generated earlier using:
#   oopoa benchmark -p benchmark/griewank.py ...
# and saved in:
#   output_sample/griewank/run_griewank.csv

# Plotting the convergence curve using a dotted line style
oopoa plot \
  --input examples/output_sample/griewank/run_griewank.csv \
  --style -- \
  --title "Griewank Convergence"
