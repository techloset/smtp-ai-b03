Perfect 👍
Below is a **READY-TO-TEACH, structured classroom script**.
You can **copy-paste this directly into a `.txt` file**, open it in front of the class, and **teach step-by-step without missing any point**.

I’ve written it in **teacher language**, with **clear flow**, **examples**, **questions to ask students**, and **important notes**.

---

# 📘 FILE HANDLING IN PYTHON

## Complete Classroom Teaching Script

---

## 1️⃣ INTRODUCTION (Start the Class)

**Teacher says:**

Today we are going to study **File Handling in Python**.
File handling means **working with files using a program** — reading data from files and writing data into files.

Before file handling, programs only worked while running.
Once the program ended, **all data was lost**.

File handling helps us **store data permanently**.

---

## 2️⃣ WHAT IS A FILE?

**Definition:**

A **file** is a collection of data stored on secondary storage (hard disk).

Examples:

* Text file → `.txt`
* Image file → `.jpg`, `.png`
* Video file → `.mp4`
* Program file → `.py`

---

## 3️⃣ WHY DO WE NEED FILE HANDLING?

Ask students:

> If I close a program, what happens to variables?

✔ They are deleted.

So we use files to:

* Save student records
* Store marks
* Save logs
* Read large data
* Build real applications

---

## 4️⃣ TYPES OF FILES

### 1. Text Files

* Human readable
* Example: `.txt`, `.csv`
* Store data as characters

### 2. Binary Files

* Machine readable
* Example: `.jpg`, `.mp3`, `.exe`
* Store data as bytes

Today we focus on **TEXT FILES**.

---

## 5️⃣ FILE HANDLING STEPS (VERY IMPORTANT)

Every file operation follows **4 steps**:

1️⃣ Open the file
2️⃣ Perform operation (read / write)
3️⃣ Close the file
4️⃣ Save resources

---

## 6️⃣ OPENING A FILE – `open()`

### Syntax:

```
file = open("filename", "mode")
```

### Example:

```
file = open("data.txt", "r")
```

---

## 7️⃣ FILE MODES (EXPLAIN CAREFULLY)

| Mode | Meaning           |
| ---- | ----------------- |
| r    | Read              |
| w    | Write (overwrite) |
| a    | Append            |
| x    | Create new file   |
| r+   | Read + Write      |

---

### 🔹 "r" – Read Mode

```
file = open("data.txt", "r")
print(file.read())
file.close()
```

⚠️ File must exist.

---

### 🔹 "w" – Write Mode

```
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

⚠️ Old data will be deleted.

---

### 🔹 "a" – Append Mode

```
file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()
```

✔ Old data is safe.

---

### 🔹 "x" – Create Mode

```
file = open("newfile.txt", "x")
file.write("New file created")
file.close()
```

⚠️ Error if file already exists.

---

## 8️⃣ READING FILE DATA

### `read()` – Read entire file

```
file = open("data.txt", "r")
print(file.read())
file.close()
```

---

### `read(n)` – Read limited characters

```
file = open("data.txt", "r")
print(file.read(5))
file.close()
```

---

### `readline()` – Read one line

```
file = open("data.txt", "r")
print(file.readline())
file.close()
```

---

### `readlines()` – Read all lines

```
file = open("data.txt", "r")
print(file.readlines())
file.close()
```

---

## 9️⃣ WRITING FILE DATA

### `write()`

```
file = open("data.txt", "w")
file.write("Welcome Students")
file.close()
```

---

### `writelines()`

```
file = open("data.txt", "w")
file.writelines(["Line 1\n", "Line 2\n", "Line 3"])
file.close()
```

---

## 🔟 FILE POINTER (CURSOR CONCEPT)

Explain:

> File pointer tells us where reading or writing happens.

---

### `tell()` – Current position

```
file = open("data.txt", "r")
print(file.tell())
file.read(5)
print(file.tell())
file.close()
```

---

### `seek()` – Move pointer

```
file = open("data.txt", "r")
file.seek(3)
print(file.read())
file.close()
```

---

## 1️⃣1️⃣ CLOSING FILE – `close()`

Explain:

> If we do not close a file, memory leaks may occur.

```
file.close()
```

---

## 1️⃣2️⃣ BEST PRACTICE – `with open()`

Explain:

> Python automatically closes the file.

```
with open("data.txt", "r") as file:
    print(file.read())
```

✔ Recommended method

---

## 1️⃣3️⃣ CHECK FILE EXISTENCE

```
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
```

---

## 1️⃣4️⃣ REAL-LIFE EXAMPLE (STUDENTS MARKS)

```
file = open("marks.txt", "w")
file.write("Danish: 85\nAli: 90\nSara: 88")
file.close()

file = open("marks.txt", "r")
print(file.read())
file.close()
```

---

## 1️⃣5️⃣ COMMON MISTAKES (TELL STUDENTS)

❌ Forgetting `close()`
❌ Using `w` instead of `a`
❌ Reading non-existing file
❌ Not adding `\n` for new line

---

## 1️⃣6️⃣ SUMMARY (END THE CLASS)

✔ Files store data permanently
✔ `open()` is required
✔ Modes decide operation
✔ Always close files
✔ `with open()` is best
✔ File handling is used in real projects

---

## 📌 END OF FILE HANDLING LECTURE

---

If you want, I can also:

* Convert this into **PDF**
* Create **slides outline**
* Add **student exercises**
* Add **MCQs + viva questions**

Just tell me 👨‍🏫📚
