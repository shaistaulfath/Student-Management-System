import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")
conn.commit()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
                   (name, age, course, marks))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nID  Name  Age  Course  Marks")
    print("-" * 30)
    for row in rows:
        print(row)

def search_student():
    sid = int(input("Enter student ID: "))
    cursor.execute("SELECT * FROM students WHERE id=?", (sid,))
    row = cursor.fetchone()
    if row:
        print("Student found:", row)
    else:
        print("Student not found")

def update_student():
    sid = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = float(input("Enter new marks: "))

    cursor.execute("UPDATE students SET name=?, age=?, course=?, marks=? WHERE id=?",
                   (name, age, course, marks, sid))
    conn.commit()
    print("Student updated successfully!")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    print("Student deleted successfully!")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

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
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

conn.close()