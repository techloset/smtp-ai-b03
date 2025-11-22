# 08 – File Handling

This folder teaches you how to **read from and write to files** using Python.

## Key ideas

- **Opening files**  
  Use `open("filename.txt", "r")` for reading, `"w"` for writing, `"a"` for appending.

- **Reading data**  
  `read()`, `readline()`, and `readlines()` to get data from files.

- **Writing data**  
  Use `write()` or `writelines()` to save text to a file.

- **Using with (context manager)**  
  `with open(...) as f:` automatically closes the file, even if errors happen.

- **Working with paths**  
  Understand relative vs absolute paths and where your script is running.

## Why this matters

File handling lets your programs **save data permanently**, such as logs, user settings, or exported reports.

## Practice exercises

1. **Write a note**  
   Ask the user to type a short note and save it to a file called `note.txt`.

2. **Read and display**  
   Read the contents of `note.txt` and print them to the screen.

3. **Line counter**  
   Given a text file, write a program that counts how many lines it has and prints the result.

