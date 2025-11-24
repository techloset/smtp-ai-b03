"""Nested loops (loop inside a loop)

We use nested loops when we need to combine every item in one group
with every item in another group.

Examples:
- Create a multiplication table
- Compare each student with each subject
"""

print("Simple multiplication table (1 to 3):")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---- end of row ----")

print("--------------------------------")

students = ["Ali", "Sara"]
courses = ["Math", "Science"]

print("Assigning students to courses:")

for student in students:
    for course in courses:
        print(f"{student} is enrolled in {course}")


