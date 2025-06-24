#!/bin/bash

# ------------------------------------------------------
# Example: Plotting the pre-generated Sphere benchmark results
# ------------------------------------------------------

# The CSV file was generated earlier using:
#   oopoa benchmark -p benchmark/sphere.py ...
# and saved in:
#   output_sample/sphere/run_sphere.csv

# Plotting the convergence curve using a dotted line style
oopoa plot \
  --input examples/output_sample/sphere/run_sphere.csv \
  --style dotted \
  --title "Sphere Convergence"
