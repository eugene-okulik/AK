import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
add_student = 'insert into students (name, second_name) VALUES (%s, %s)'
student_values = ('Maks', 'Pain')
student = cursor.execute(add_student, student_values)
student_id = cursor.lastrowid
cursor.execute('select * from students where id = %s', (student_id,))
new_student = cursor.fetchone()
print(
    f"Student: id = {new_student['id']}, name = {new_student['name']}, second_name = {new_student['second_name']}, "
    f"group_id = {new_student['group_id']}"
)


books_values = [
    ('Harry Potter', student_id),
    ('Plaxa', student_id),
    ('1984', student_id),
    ('Three Comrades', student_id)
]

add_books = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(add_books, books_values)


add_group = 'INSERT INTO  `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
student_values = ('Part_of_cinema', '01.01.2025', '01.01.2999')
group = cursor.execute(add_group, student_values)
group_id = cursor.lastrowid
cursor.execute("SELECT * FROM `groups` WHERE id = %s", (group_id,))
new_group = cursor.fetchone()
print(
    f"Group: id = {new_group['id']}, title = {new_group['title']},start_date = {new_group['start_date']},"
    f" end_date= {new_group['end_date']}"
)

cursor.execute('update students s set group_id = %s where id = %s', (group_id, student_id,))
cursor.execute("select * from students where id = %s", (student_id,))
update_student_id = cursor.fetchone()
print(
    f"Student_group: id = {update_student_id['id']}, name = {update_student_id['name']},"
    f" second_name = {update_student_id['second_name']}, group_id = {update_student_id['group_id']}"
)

subject_values = [
    'Defense Aganist the Dark Arts',
    'Charms',
    'Potions'
]
inserted_subjects = []
for subject in subject_values:
    cursor.execute('insert into subjects (title) values (%s)', (subject,))
    subject_id = cursor.lastrowid
    inserted_subjects.append({
        'id': subject_id,
        'title': subject
    })
    print(f"Subjects: id = {subject_id}, title = {subject}")


inserted_lesson = []


def lesson_function(subject, lessons_values):
    for subject_in_dictionary in inserted_subjects:
        if subject == subject_in_dictionary['title']:
            subject_id = subject_in_dictionary['id']
    for lesson in lessons_values:
        add_lesson = 'INSERT into lessons (title, subject_id) VALUES (%s, %s)'
        cursor.execute(add_lesson, (lesson, subject_id))
        lesson_id = cursor.lastrowid
        inserted_lesson.append({
            'id': lesson_id,
            'title': lesson,
            'subject_id': subject_id
        })
        print(
            f" Lessons: id = {lesson_id}, title = {lesson},"
            f"subject_id = {subject_id}"
        )


lesson_function('Defense Aganist the Dark Arts', ('Defence', 'Attack',))
lesson_function('Charms', ('Field Strategy in Battle Magic', 'Wands',))
lesson_function('Potions', ('Techniques', 'Common Charms',))


def marks_function(mark, lesson):
    for lesson_in_dictionary in inserted_lesson:
        if lesson_in_dictionary['title'] == lesson:
            lesson_id = lesson_in_dictionary['id']

    add_mark = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    cursor.execute(add_mark, (mark, lesson_id, student_id))
    mark_id = cursor.lastrowid
    cursor.execute('select * from marks where id = %s', (mark_id,))
    new_mark = cursor.fetchone()
    print(f"Mark = {new_mark['value']}, student = {student}, lesson = {lesson})")


marks_function('5', 'Defence')
marks_function('5', 'Attack')
marks_function('5', 'Field Strategy in Battle Magic')
marks_function('4', 'Wands')
marks_function('3', 'Techniques')
marks_function('3', 'Common Charms')


cursor.execute("""SELECT s.name as student_name, m.value as mark
from students s join marks m on m.student_id = s.id where s.id= %s""", (student_id,))
marks = cursor.fetchall()
for student_marks in marks:
    print(f"student name = {student_marks['student_name']} - mark = {student_marks['mark']}")

cursor.execute("""SELECT s.name as student_name,
                                  b.title as book_title
                           FROM students s join books b on s.id = b.taken_by_student_id where s.id = %s""",
               (student_id,))
books = cursor.fetchall()
for taken_books_by_student in books:
    print(f"student name = {taken_books_by_student['student_name']} book = {taken_books_by_student['book_title']}")

info_from_database_about_student = query = """
SELECT s.id AS student_id,
       s.name AS student_name,
       g.title AS group_title,
       b.title AS book_title,
       m.value AS mark,
       l.title AS lesson_title,
       s2.title AS subject_title
FROM students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE g.id = %s AND s.id = %s
"""
cursor.execute(query, (group_id, student_id))
all_info_about_student = cursor.fetchall()
student_info = {
    "student_name": None,
    "student_group": None,
    "books": set(),
    "marks": [],
    "lesson": [],
    "subjects": []
}
for info_about_student in all_info_about_student:
    student_info['student_name'] = info_about_student['student_name']
    student_info['student_group'] = info_about_student['group_title']
    student_info['books'].add(info_about_student['book_title'])
    student_info['marks'].append(info_about_student['mark'])
    student_info['lesson'].append(info_about_student['lesson_title'])
    student_info['subjects'].append(info_about_student['subject_title'])

for key, value in student_info.items():
    print(f"{key}: {value}")


db.commit()
db.close()
