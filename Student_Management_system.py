# Student Management System
# Author: Egenti Michael Chinedu
# Matric Number: 24/14118
# Language: Python 3

students = []

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course Name: ")

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    for student in students:
        print(student)
    print()

def search_student():
    student_id = int(input("Enter Student ID to search: "))
    for student in students:
        if student["student_id"] == student_id:
            print(student)
            print()
            return
    print("Student not found.\n")

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    for student in students:
        if student["student_id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["course"] = input("Enter new course: ")
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

def main_menu():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")


main_menu() 

