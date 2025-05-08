class Book:
    page_material = 'Бумага'
    text_available = True

    def __init__(self, book_title, autor, page_count, isbn, flag_reserved):
        self.book_title = book_title
        self.autor = autor
        self.page_count = page_count
        self.isbn = isbn
        self.flag_reserved = flag_reserved

    def __str__(self):
        if self.flag_reserved is True:
            return (f'{self.book_title}, {self.autor}, страниц: {self.page_count}, материал: {self.page_material},'
                    f' зарезервирована')
        else:
            return (f'{self.book_title}, {self.autor}, страниц: {self.page_count}, материал: {self.page_material}')


class FictionBook(Book):
    pass


class TheCountOfCristo(FictionBook):
    pass


class WarAndPeace(FictionBook):
    pass


class TheAdventuresOfTomSawye(FictionBook):
    pass


class TheIdiot(FictionBook):
    pass


class TheScaffold(FictionBook):
    pass


class SchoolBook(Book):

    def __init__(self, book_title, autor, page_count, subject, grade, available):
        self.book_title = book_title
        self.autor = autor
        self.page_count = page_count
        self.subject = subject
        self.grade = grade
        self.available = available

    def __str__(self):
        if self.available is True:
            return (f'{self.book_title}, {self.autor}, страниц:{self.page_count}, предмет:{self.subject}, '
                    f'класс:{self.grade}, зарезервирована')
        else:
            return (f'{self.book_title}, {self.autor}, страниц: {self.page_count}, предмет: {self.subject}, '
                    f'класс:{self.grade}')


class Mathematics(SchoolBook):
    pass


class History(SchoolBook):
    pass


class Literature(SchoolBook):
    pass


class Biology(SchoolBook):
    pass


class Geography(SchoolBook):
    pass


book_of_mathematics = Mathematics('Алгебра', 'Иванов', 150, 'Математика', '5',
                                  True)
book_of_history = History('История России', 'Савин', 250, 'История', '9',
                          False)
book_of_literature = Literature('Литература', 'Сачко', 250, 'Литература', '10',
                                False)
book_of_biology = Biology('Биология', 'Сычильников', 120, 'Литература', '8',
                          False)
book_of_geography = Geography('География мира', 'Петров', 250, 'География', '7',
                              False)


the_count_of_monte_cristo = TheCountOfCristo('Граф Монте-Кристо', 'Александр Дюма', 1225,
                                             '978-1234567890', True)
war_and_peace = WarAndPeace('Война и мир', 'Лев Толстой', 1350, '978-1234567891',
                            False)
the_adventures_of_tom_sawyer = TheAdventuresOfTomSawye('Приключения Тома Сойера', 'Марк Твен',
                                                       366, '978-1234567892', False)
the_idiot = TheIdiot('Идиот', 'Фёдор Достоевский', 650, '978-1234567893',
                     False)
the_scaffold = TheScaffold('Плаха', 'Чингиз Айтматов', 420, '978-1234567894',
                           False)


print(the_count_of_monte_cristo)
print(war_and_peace)
print(the_adventures_of_tom_sawyer)
print(the_idiot)
print(the_scaffold)
print(book_of_mathematics)
print(book_of_history)
print(book_of_literature)
print(book_of_biology)
print(book_of_geography)
