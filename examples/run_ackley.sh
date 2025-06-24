#!/bin/bash

# ------------------------------------------------------
# Example: Plotting the pre-generated Ackley benchmark results
# ------------------------------------------------------

# The CSV file was generated earlier using:
#   oopoa benchmark -p benchmark/ackley.py ...
# and saved in:
#   output_sample/ackley/run_acklet.csv

# Plotting the convergence curve using a dotted line style
oopoa plot \
  --input examples/output_sample/ackley/run_ackley.csv \
  --style - \
  --title "Ackley Convergence"
