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


class TheCountOfCristo(Book):
    pass


class WarAndPeace(Book):
    pass


class TheAdventuresOfTomSawye(Book):
    pass


class TheIdiot(Book):
    pass


class TheScaffold(Book):
    pass


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
