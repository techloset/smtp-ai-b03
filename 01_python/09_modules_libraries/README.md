
# 📘 Python Modules & Libraries – Complete Guide for Students

This guide explains **modules and libraries in Python from scratch**, using **simple language, real-world examples**, and **step-by-step concepts**.


## 📌 Why This Topic Is Important

In real software development:
- Programs are large
- Many developers work together
- Code must be reusable and organized

👉 Modules and libraries make this possible.

---

# 🔹 PART 1: WHAT IS A MODULE?

## ✅ Definition
A **module** is a **single Python file (`.py`)** that contains:
- Functions
- Variables
- Classes

📌 One file = one module

---

## 📁 Example of a Module

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
````

Using the module:

```python
import math_utils
print(math_utils.add(5, 3))
```

---

## 🔹 Why Modules Were Introduced

### ❌ Before Modules

* Everything written in one file
* Code becomes long and confusing
* Difficult to fix errors
* Code duplication

### ✅ After Modules

* Code divided into small logical parts
* Easy to understand
* Easy to reuse
* Easy teamwork

---

## 🔹 Types of Modules in Python

### 1️⃣ Built-in Modules

Already available with Python

Examples:

* `math`
* `os`
* `sys`
* `random`
* `datetime`

```python
import math
print(math.sqrt(16))
```

---

### 2️⃣ User-Defined Modules

Modules created by the programmer

```python
# mymodule.py
def greet():
    print("Hello Students")
```

```python
import mymodule
mymodule.greet()
```

---

### 3️⃣ Third-Party Modules

Created by others and installed using `pip`

Examples:

* `numpy`
* `pandas`
* `requests`

```bash
pip install requests
```

---

# 🔹 PART 2: HOW PYTHON FINDS A MODULE (IMPORTANT)

When Python sees:

```python
import mymodule
```

It searches in this order:

1️⃣ Current directory
2️⃣ PYTHONPATH
3️⃣ Standard Library
4️⃣ site-packages

If not found:

```text
ModuleNotFoundError
```

Check paths using:

```python
import sys
print(sys.path)
```

---

# 🔹 PART 3: WHAT IS A PACKAGE?

## ✅ Definition

A **package** is a **folder (directory)** that contains:

* Multiple modules
* A special file: `__init__.py`

📌 Folder of modules = package

---

## 📁 Package Example

```text
utils/
├── __init__.py
├── math_utils.py
├── file_utils.py
```

Using a package:

```python
from utils import math_utils
math_utils.add(2, 3)
```

---

# 🔹 PART 4: WHAT IS **init**.py?

## ✅ Definition

`__init__.py` is a **special Python file** that:

* Marks a folder as a package
* Runs when the package is imported

---

## ❓ Is it mandatory to add code inside it?

✔ NO
✔ An empty `__init__.py` is enough

```text
mypackage/
├── __init__.py   ← empty (OK)
├── module.py
```

---

## 🟢 When Do We Add Code in `__init__.py`?

### 1️⃣ To simplify imports

```python
# __init__.py
from .math_utils import add
```

Now:

```python
from utils import add
```

---

### 2️⃣ To run code on import (rare)

```python
print("Package Loaded")
```

---

# 🔹 PART 5: MODULE vs PACKAGE

| Feature       | Module | Package          |
| ------------- | ------ | ---------------- |
| Structure     | File   | Folder           |
| Extension     | `.py`  | Directory        |
| Contains      | Code   | Multiple modules |
| `__init__.py` | ❌      | ✅                |

---

## 🧠 Memory Trick

* Module = file
* Package = folder of files

---

# 🔹 PART 6: WHAT IS A LIBRARY?

## ✅ Definition

A **library** is a **collection of modules and packages** designed to solve a broader problem.

⚠️ “Library” is a **conceptual term**, not a Python keyword.

---

## 📦 Example: NumPy Library

```text
numpy/
├── __init__.py
├── core/
│   ├── numeric.py
│   ├── array.py
├── random/
```

---

## 🔹 Types of Libraries

### 1️⃣ Standard Library

Comes with Python

Examples:

* `math`
* `os`
* `json`
* `datetime`

---

### 2️⃣ Third-Party Libraries

Installed using pip

Examples:

* `numpy`
* `pandas`
* `matplotlib`
* `requests`

---

### 3️⃣ User-Defined Libraries

Libraries created by you for reuse

---

# 🔹 PART 7: MODULE vs LIBRARY

| Feature   | Module    | Library    |
| --------- | --------- | ---------- |
| Size      | Small     | Large      |
| Structure | One file  | Many files |
| Example   | `math.py` | `numpy`    |

---

## 🔗 Relationship

```text
Library
 └── Package
      └── Module
           └── Functions
```

---

# 🔹 PART 8: ABSOLUTE vs RELATIVE IMPORTS

## 🔹 Absolute Import

Uses full path from project root

```python
from school.students import show_students
```

✔ Recommended
✔ Clear
✔ Works everywhere

---

## 🔹 Relative Import

Uses dots (`.`)

```python
from .students import show_students
```

| Symbol | Meaning         |
| ------ | --------------- |
| `.`    | Current package |
| `..`   | Parent package  |

⚠️ Relative imports work **only inside packages**

---

# 🔹 PART 9: REAL-WORLD ANALOGIES

* Module → One book
* Package → Bookshelf
* Library → Library building

---

# 🔹 PART 10: COMMON STUDENT MISTAKES

❌ Confusing module with library
❌ Forgetting `__init__.py`
❌ Using relative import in main file
❌ Naming file same as built-in module
❌ Thinking `pip install` = `import`

---

# 🔹 PART 11: EXAM-READY DEFINITIONS

### Module:

A Python file containing code.

### Package:

A directory containing multiple modules and an `__init__.py` file.

### Library:

A collection of packages and modules providing reusable functionality.

---

# 🔹 FINAL SUMMARY (ONE PAGE REVISION)

✔ Module = file
✔ Package = folder
✔ Library = collection
✔ `__init__.py` = package identifier
✔ Absolute import = full path
✔ Relative import = dot path

---

## ✅ End of Guide

```

---

### ✅ How to Use This in Class
- Open this file
- Explain **section by section**
- Show examples live
- Ask students to create:
  - One module
  - One package
  - One simple library

