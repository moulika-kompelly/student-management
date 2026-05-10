import sqlite3

# Add Student
def add_student():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (name, age, course)
    )

    conn.commit()

    print("Student added successfully!")

    conn.close()


# View Students
def view_students():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent Records\n")

    for student in students:
        print(
            f"ID: {student[0]}, "
            f"Name: {student[1]}, "
            f"Age: {student[2]}, "
            f"Course: {student[3]}"
        )

    conn.close()
    