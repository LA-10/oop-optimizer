# 🧠 How OOPOA Works – Algorithm Overview

OOPOA (Object-Oriented Programming Optimization Algorithm) is a novel population-based metaheuristic inspired by OOP concepts like encapsulation and inheritance.

This file explains the algorithm mechanics behind the CLI implementation.

---

## 🧬 Key Concepts

| Status Value | Interpretation | Action                           |
| ------------ | -------------- | -------------------------------- |
| `0`          | Public         | Use own value from parent        |
| `1`          | Protected      | Copy value from another solution |
| `2`          | Private        | Generate a new random value      |

Each solution maintains a status vector that determines how each gene is inherited during reproduction.

---

## 🔁 Algorithm Steps

1. **Initialization**

   * Randomly generate population matrix of size `N x D`
   * Randomly generate status matrix of same shape (values ∈ {0, 1, 2})

2. **Parent Generation**

   * Based on `status`, create a parent solution:

     * Public → use own value
     * Protected → pick another individual’s value
     * Private → reinitialize that gene randomly

3. **Child Generation**

   * Derived from parent + status rules

4. **Fitness Evaluation**

   * Evaluate both parent and child using selected benchmark function

5. **Selection**

   * If child fitness < parent fitness → replace in population

6. **Status Mutation**

   * With probability `MR`, mutate status value (0 ↔ 1 ↔ 2)

7. **Repeat** for `Max_Iter`

---

## 🎯 Goal

To minimize the fitness function by evolving the population under status-driven inheritance.

---

## 📌 Notes

* Status vectors act as "inheritance policies" per gene
* OOP concepts allow structured, selective re-use of genetic material
* Mutation introduces exploration and avoids local minima

---

For full math reference, see: [`docs/math.md`](math.md)

## 🧾 Citation & Credits

This implementation is based on the original research paper:

> Hosny, K.M., Khalid, A.M., Said, W., Elmezain, M., & Mirjalili, S. (2024).  
> *A novel metaheuristic based on object-oriented programming concepts for engineering optimization.*  
> Alexandria Engineering Journal. https://doi.org/10.1016/j.aej.2024.04.060

---

