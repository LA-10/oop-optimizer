#!/bin/bash

# ------------------------------------------------------
# Example: Plotting the pre-generated Custom benchmark results
# ------------------------------------------------------

# The CSV file was generated earlier using:
# and saved in:
#   output_sample/custom/run_custom.csv

# Plotting the convergence curve using a dotted line style
oopoa plot \
  --input examples/output_sample/custom/run_custom.csv \
  --title "Custom Convergence"
