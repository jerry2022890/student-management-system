students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = {"roll": roll, "name": name, "marks": marks}
    students.append(student)
    print("Student Added Successfully")

def view_students():
    if not students:
        print("No students found")
        return
    for s in students:
        print(s)

def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student Not Found")

def delete_student():
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Deleted")
            return
    print("Student Not Found")

while True:
    print("\n1 Add\n2 View\n3 Search\n4 Delete\n5 Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Bye 👋")
        break
    else:
        print("Invalid choice")
