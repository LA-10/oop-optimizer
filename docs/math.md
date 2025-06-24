# 📘 Mathematical Description of the OOPOA Algorithm

This document explains the mathematical foundations and concepts behind the **Object-Oriented Programming Optimization Algorithm (OOPOA)** as implemented in this project.

OOPOA was introduced in the paper:

> Hosny, K.M., Khalid, A.M., Said, W., Elmezain, M., & Mirjalili, S. (2024).  
> *A novel metaheuristic based on object-oriented programming concepts for engineering optimization.*  
> Alexandria Engineering Journal. https://doi.org/10.1016/j.aej.2024.04.060

---

## 🧠 Core Concepts

OOPOA mimics **access control concepts from object-oriented programming (OOP)** to define how solutions (individuals) access values in a population.

Each solution has a **status vector** `s` indicating access type:

| Status Value | Access Type | Meaning |
|--------------|-------------|---------|
| `0`          | Public      | Use the individual’s own value |
| `1`          | Protected   | Use a value from a related solution (same generation) |
| `2`          | Private     | Generate a new random value in bounds |

---

## 🔣 Notation

| Symbol           | Meaning                             |
|------------------|--------------------------------------|
| `N`              | Number of individuals in the population |
| `D`              | Dimension of each solution           |
| `x_i`            | The `i`-th individual in the population |
| `s_i`            | Status vector of `x_i` (length `D`)  |
| `f(x_i)`         | Fitness of solution `x_i`            |
| `MR`             | Mutation rate (usually [0.1, 0.99])  |

---

## 🛠 Initialization

- Randomly generate an initial population of `N` individuals:  
  \[
  x_i = [x_{i1}, x_{i2}, \dots, x_{iD}]
  \]
  with each `x_{ij} ∈ [lower\_bound, upper\_bound]`

- Randomly initialize a status matrix `s_i` for each `x_i`, where:
  \[
  s_{ij} ∈ \{0, 1, 2\}
  \]

---

## 👪 Parent Selection

For each solution `x_i`, a **parent solution** `p_i` is created based on `s_i`:

\[
p_{ij} =
\begin{cases}
x_{ij} & \text{if } s_{ij} = 0 \quad \text{(public)}\\
x_{kj} & \text{if } s_{ij} = 1 \quad \text{(protected)}\\
rand(lb_j, ub_j) & \text{if } s_{ij} = 2 \quad \text{(private)}
\end{cases}
\]

Where `k` is a randomly chosen other solution in the population.

---

## 👶 Child Generation

- A **child** is created from the parent by directly copying values where `s = 0 or 1`, and randomly mutating values where `s = 2`.

---

## 🎲 Mutation Operator

With probability `MR`, each entry of the status vector is randomly mutated:

\[
s_{ij}' =
\begin{cases}
randint(0, 2) & \text{if } rand(0,1) < MR \\
s_{ij} & \text{otherwise}
\end{cases}
\]

---

## 🎯 Fitness Evaluation

Each solution `x` is evaluated using a benchmark function:

- **Sphere**:  
  \[
  f(x) = \sum_{j=1}^D x_j^2
  \]

- Others include: Rastrigin, Ackley, Rosenbrock, etc.

The algorithm **aims to minimize** `f(x)`.

---

## 🔁 Selection Rule

If the child solution `c_i` has **better fitness** than the parent `p_i`, it replaces it:

\[
\text{if } f(c_i) < f(p_i), \quad x_i := c_i, \quad s_i := s_i'
\]

---

## 🔄 Loop

Repeat the steps above for `Max_Iter` iterations. Track the best fitness at each iteration for convergence analysis.

---

## 📈 Convergence

The final result is typically visualized as:

- `x-axis`: Iteration
- `y-axis`: Best fitness value found so far

Use `oopoa plot` to generate this curve.

---

## 🧾 Citation & Credits

This implementation is based on the original research paper:

> Hosny, K.M., Khalid, A.M., Said, W., Elmezain, M., & Mirjalili, S. (2024).  
> *A novel metaheuristic based on object-oriented programming concepts for engineering optimization.*  
> Alexandria Engineering Journal. https://doi.org/10.1016/j.aej.2024.04.060

Please cite the paper if this tool contributes to your research or applications.

---

