import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
        )
''')
conn.commit()

students_data = [
    ('Alice', 20, 'A'),
    ('Bob', 22, 'B'),
    ('Charlie', 21, 'C')
]
cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_data)
conn.commit()

def get_student_by_name(name):
    cursor.execute('SELECT name, age, grade FROM students WHERE name = ?', (name,))
    return cursor.fetchone()

def update_student_grade(name, new_grade):
    cursor.execute('UPDATE students SET grade = ? WHERE name = ?', (new_grade, name))
    conn.commit()

def delete_student(name):
    cursor.execute('DELETE FROM students WHERE name = ?', (name,))
    conn.commit()

print('Информация о студенте Алиса:', get_student_by_name('Alice'))
update_student_grade('Alice', 'A+')
print('Обновленная информация о студенте Алиса:', get_student_by_name('Alice'))
delete_student('Bob')
print('Информация о студенте Боб после удаления:', get_student_by_name('Bob'))

conn.close()

