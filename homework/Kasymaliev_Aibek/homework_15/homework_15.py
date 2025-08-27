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
cursor.execute(f'select * from students where id = {student_id}')
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
for book in books_values:
    cursor.execute('insert into books (title, taken_by_student_id) values (%s, %s)', book)
    book_id = cursor.lastrowid
    cursor.execute(f'select * from books where id = {book_id}')
    books = cursor.fetchone()
    print(
        f" Book_for_ student: id = {books['id']}, title = {books['title']},"
        f"taken_by_student_id = {books['taken_by_student_id']}"
    )

add_group = 'INSERT INTO  `groups` (title, start_date, end_date) VALUES (%s, %s, %s)'
student_values = ('Part_of_cinema', '01.01.2025', '01.01.2999')
group = cursor.execute(add_group, student_values)
group_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM `groups` WHERE id = {group_id}")
new_group = cursor.fetchone()
print(
    f"Group: id = {new_group['id']}, title = {new_group['title']},start_date = {new_group['start_date']},"
    f" end_date= {new_group['end_date']}"
)

cursor.execute(f'update students s set group_id = {group_id} where id = {student_id}')
cursor.execute(f"select * from students where id = {student_id}")
update_student_id = cursor.fetchone()
print(
    f"Student_group: id = {update_student_id['id']}, name = {update_student_id['name']},"
    f" second_name = {update_student_id['second_name']}, group_id = {update_student_id['group_id']}"
)

subject_values = [
    ('Defense Aganist the Dark Arts',),
    ('Charms',),
    ('Potions',)
]
inserted_subjects = []
for subject in subject_values:
    cursor.execute('insert into subjects (title) values (%s)', subject)
    subject_id = cursor.lastrowid
    inserted_subjects.append({
        'id': subject_id,
        'title': subject
    })
    print(f"Subjects: id = {subject_id}, title = {subject}")


def lesson_function(subject, lessons_values):
    cursor.execute("select id from subjects where title = %s", (subject,))
    subject_id = cursor.fetchone()['id']
    for lesson in lessons_values:
        add_lesson = 'INSERT into lessons (title, subject_id) VALUES (%s, %s)'
        cursor.execute(add_lesson, (lesson, subject_id))
        lesson_id = cursor.lastrowid
        cursor.execute("SELECT * FROM `lessons` WHERE id = %s", (lesson_id,))
        new_lesson = cursor.fetchone()
        print(
            f" Lessons: id = {new_lesson['id']}, title = {new_lesson['title']},"
            f"subject_id = {new_lesson['subject_id']}"
        )


lesson_function('Defense Aganist the Dark Arts', ('Defence', 'Attack',))
lesson_function('Charms', ('Field Strategy in Battle Magic', 'Wands',))
lesson_function('Potions', ('Techniques', 'Common Charms',))


def marks_function(mark, lesson, student):
    cursor = db.cursor(dictionary=True, buffered=True)
    cursor.execute("select id from lessons where title = %s", (lesson,))
    lesson_row = cursor.fetchone()
    lesson_id = lesson_row['id']
    cursor.execute('select id from students where name = %s', (student,))
    student_row = cursor.fetchone()
    student_id = student_row['id']
    add_mark = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    cursor.execute(add_mark, (mark, lesson_id, student_id))
    mark_id = cursor.lastrowid
    cursor.execute('select * from marks where id = %s', (mark_id,))
    new_mark = cursor.fetchone()
    print(f"Mark = {new_mark['value']}, student = {student}, lesson = {lesson})")


marks_function('5', 'Defence', 'Maks')
marks_function('5', 'Attack', 'Maks')
marks_function('5', 'Field Strategy in Battle Magic', 'Maks')
marks_function('4', 'Wands', 'Maks')
marks_function('3', 'Techniques', 'Maks')
marks_function('3', 'Common Charms', 'Maks')

db.commit()
db.close()
