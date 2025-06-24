#!/bin/bash

# ------------------------------------------------------
# Example: Plotting the pre-generated Rastrigin benchmark results
# ------------------------------------------------------

# The CSV file was generated earlier using:
#   oopoa benchmark -p benchmark/rastrigin.py ...
# and saved in:
#   output_sample/rastrigin/run_rastrigincsv

# Plotting the convergence curve using a dotted line style
oopoa plot \
  --input examples/output_sample/rastrigin/run_rastrigin.csv \
  --style -. \
  --title "Rastrigin Convergence"
