from db import get_connection


def add_student(name, roll_number, math, science, english):
    conn = get_connection()
    conn.execute(
        "INSERT INTO students (name, roll_number, marks_math, marks_science, marks_english) VALUES (?, ?, ?, ?, ?)",
        (name, roll_number, math, science, english)
    )
    conn.commit()
    conn.close()


def list_students():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows


def find_student(roll_number):
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number,))
    row = cursor.fetchone()
    conn.close()
    return row


def delete_student(roll_number):
    conn = get_connection()
    conn.execute("DELETE FROM students WHERE roll_number = ?", (roll_number,))
    conn.commit()
    conn.close()


def get_average(math, science, english):
    return (math + science + english) / 3