from db import create_table
from models import add_student, list_students, find_student, delete_student, get_average


def show_all():
    students = list_students()
    if len(students) == 0:
        print("No students yet.")
    for s in students:
        print(s)


def show_one(roll_number):
    student = find_student(roll_number)
    if student is None:
        print("No student with that roll number.")
        return
    name = student[1]
    math = student[3]
    science = student[4]
    english = student[5]
    avg = get_average(math, science, english)
    print(f"Name: {name}")
    print(f"Math: {math}, Science: {science}, English: {english}")
    print(f"Average: {avg}")


def menu():
    create_table()

    while True:
        print("\n1. Add Student")
        print("2. Show All Students")
        print("3. Find Student by Roll Number")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            roll = input("Roll number: ")
            math = int(input("Math marks: "))
            science = int(input("Science marks: "))
            english = int(input("English marks: "))
            add_student(name, roll, math, science, english)
            print("Student added.")

        elif choice == "2":
            show_all()

        elif choice == "3":
            roll = input("Roll number: ")
            show_one(roll)

        elif choice == "4":
            roll = input("Roll number to delete: ")
            delete_student(roll)
            print("Deleted.")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()