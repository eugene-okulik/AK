SELECT * from students s where id = '20853' and s.group_id = '5462';
SELECT * from `groups` g where id = '5462';
SELECT * from subjects s where title like '%Potions%';
select * from marks where marks.student_id = '20853';
SELECT * from lessons l where id in ('11624', '11625', '11626', '11627', '11628', '11629')

insert into students (name, second_name) VALUES ('Maks', 'Mad');
SELECT * from students s where s.name = 'Maks';
insert into books (title, taken_by_student_id) values ('Harry Potter', '20853'),
											          ('Plaxa', '20853'),
											          ('1984', '20853'),
											          ('Three Comrades','20853');
INSERT INTO  `groups` (title, start_date, end_date) VALUES ('Part_of_cinema', '01.01.2025', '01.01.2999');
select * from `groups` g where g.title = 'Part_of_cinema';
update students s set group_id = '5462' where id = '20853';
INSERT into subjects (title) VALUES ('Defense Aganist the Dark Arts'),
							        ('Charms'),
							 		('Potions');
SELECT * from subjects s where s.title  in ('Defense Aganist the Dark Arts', 'Charms', 'Potions');
INSERT into lessons (title, subject_id) VALUES ('Defence', '11588'), ('Attack', '11588'),
											   ('Field Strategy in Battle Magic', '11596'), ('Wands','11596'),
											   ('Techniques', '11590'), ('Common Charms', '11590');
SELECT * from lessons l
where l.title in ('Defence', 'Attack', 'Field Strategy in Battle Magic', 'Wands', 'Techniques', 'Common Charms');
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', '11624', '20853'),
														('4', '11625', '20853'),
														('4', '11626', '20853'),
														('5', '11626', '20853'),
														('5', '11627', '20853'),
														('4', '11628', '20853'),
														('3', '11629', '20853');
SELECT * from students s join marks m on m.student_id = s.id where s.id = '20853';
SELECT * FROM students s join books b on s.id = b.taken_by_student_id where s.id = '20853';
SELECT * from students s join `groups` g on g.id = s.group_id
						 JOIN  books b on  b.taken_by_student_id = s.id
						 JOIN marks m on s.id = m.student_id
						 JOIN lessons l on m.lesson_id = l.id
						 JOIN subjects s2 on s2.id = l.subject_id
WHERE s.id = '20853'

