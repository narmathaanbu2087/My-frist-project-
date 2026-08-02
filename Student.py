
Student Management System (student.py)

import json
 import os

FILE_NAME = "students.json"

Load students

def load_students(): if os.path.exists(FILE_NAME): with open(FILE_NAME, "r") as f: return json.load(f) return []

Save students

def save_students(students): with open(FILE_NAME, "w") as f: json.dump(students, f, indent=4)

Add student

def add_student(students): name = input("Enter student name: ") roll = input("Enter roll number: ") dept = input("Enter department: ")

student = {
    "name": name,
    "roll": roll,
    "department": dept
}

students.append(student)
save_students(students)
print("Student added successfully!\n")

View students

def view_students(students): if not students: print("No student records found!\n") return

print("\n--- Student List ---")
for i, stu in enumerate(students, start=1):
    print(f"{i}. Name: {stu['name']} | Roll: {stu['roll']} | Dept: {stu['department']}")
print()

Search student

def search_student(students): roll = input("Enter roll number to search: ") found = False

for stu in students:
    if stu['roll'] == roll:
        print(f"Found: {stu['name']} | Dept: {stu['department']}\n")
        found = True
        break

if not found:
    print("Student not found!\n")

Delete student

def delete_student(students): roll = input("Enter roll number to delete: ")

for stu in students:
    if stu['roll'] == roll:
        students.remove(stu)
        save_students(students)
        print("Student deleted successfully!\n")
        return

print("Student not found!\n")

Main menu

def main(): students = load_students()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        search_student(students)
    elif choice == '4':
        delete_student(students)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")

if name == "main": main()Student Management System (student.py)

import json import os

FILE_NAME = "students.json"

Load students

def load_students(): if os.path.exists(FILE_NAME): with open(FILE_NAME, "r") as f: return json.load(f) return []

Save students

def save_students(students): with open(FILE_NAME, "w") as f: json.dump(students, f, indent=4)

Add student

def add_student(students): name = input("Enter student name: ") roll = input("Enter roll number: ") dept = input("Enter department: ")

student = {
    "name": name,
    "roll": roll,
    "department": dept
}

students.append(student)
save_students(students)
print("Student added successfully!\n")

View students

def view_students(students): if not students: print("No student records found!\n") return

print("\n--- Student List ---")
for i, stu in enumerate(students, start=1):
    print(f"{i}. Name: {stu['name']} | Roll: {stu['roll']} | Dept: {stu['department']}")
print()

Search student

def search_student(students): roll = input("Enter roll number to search: ") found = False

for stu in students:
    if stu['roll'] == roll:
        print(f"Found: {stu['name']} | Dept: {stu['department']}\n")
        found = True
        break

if not found:
    print("Student not found!\n")

Delete student

def delete_student(students): roll = input("Enter roll number to delete: ")

for stu in students:
    if stu['roll'] == roll:
        students.remove(stu)
        save_students(students)
        print("Student deleted successfully!\n")
        return

print("Student not found!\n")

Main menu

def main(): students = load_students()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        search_student(students)
    elif choice == '4':
        delete_student(students)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")

if name == "main": main()
