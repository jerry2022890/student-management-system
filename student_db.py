import sqlite3

# DATABASE CONNECT
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# TABLE CREATE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll INTEGER PRIMARY KEY,
    name TEXT,
    marks REAL
)
""")
conn.commit()

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (roll, name, marks)
    )
    conn.commit()
    print("Student Added")

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if not data:
        print("No students found")
        return

    for s in data:
        print(s)

while True:
    print("\n1 Add\n2 View\n3 Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Bye 👋")
        break
    else:
        print("Invalid choice")
