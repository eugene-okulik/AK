import mysql.connector as mysql
import os
import dotenv
import csv


dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_DATABASE')
)
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')


with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
        cursor = db.cursor(dictionary=True)
        info_from_database_about_student = """
        SELECT s.name as name, s.second_name as second_name, g.title as group_title, b.title as book_title,
        s2.title as subject_title, l.title as lesson_title, m.value as mark_value
        FROM students s
        JOIN `groups` g ON g.id = s.group_id
        JOIN books b ON b.taken_by_student_id = s.id
        JOIN marks m ON m.student_id = s.id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjects s2 ON s2.id = l.subject_id
        WHERE s.name = %s and s.second_name = %s and g.title = %s and b.title = %s and s2.title = %s and l.title = %s
        and m.value = %s
        """
        cursor.execute(info_from_database_about_student, (row['name'], row['second_name'], row['group_title'],
                                                          row['book_title'], row['subject_title'],
                                                          row['lesson_title'], row['mark_value']))
        match_info = cursor.fetchall()

        if not match_info:
            print('В БД не найдены:', row)
