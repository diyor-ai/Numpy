# 🧮 NumPy Learning Journey

Welcome to my **NumPy Learning Repository**!  
This repo is dedicated to learning and practicing **NumPy**, one of the most powerful Python libraries for numerical computing and data analysis.

---

## 📘 About NumPy

**NumPy (Numerical Python)** is an open-source Python library that makes mathematical and matrix operations fast and easy.  
It is the foundation for many data science and machine learning tools — including **Pandas, TensorFlow, and Scikit-learn**.

With NumPy, you can:
- Work with **multi-dimensional arrays (ndarrays)**.
- Perform **vectorized mathematical operations** much faster than Python loops.
- Use **powerful built-in functions** for linear algebra, statistics, and broadcasting.

---

## 🗓️ Learning Plan

### 🔹 Week 1 — Basics
- [ ] Install NumPy (`pip install numpy`)
- [ ] Create and explore arrays
- [ ] Learn array indexing and slicing
- [ ] Perform basic operations (`sum`, `mean`, `reshape`, etc.)

### 🔹 Week 2 — Intermediate
- [ ] Learn broadcasting
- [ ] Apply random and statistical functions
- [ ] Explore linear algebra operations

### 🔹 Week 3 — Projects
- [ ] Mini Project 1: Matrix operations simulator  
- [ ] Mini Project 2: Image as array (basic image manipulation)
- [ ] Mini Project 3: NumPy-based data statistics tool

---

## 💻 Example Task

```python
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Row and column sums
row_sums = arr.sum(axis=1)
col_sums = arr.sum(axis=0)

print("Array:\n", arr)
print("Row sums:", row_sums)
print("Column sums:", col_sums)
