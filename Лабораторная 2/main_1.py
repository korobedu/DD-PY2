BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Класс, представляющий книгу
    """
    def __init__(self, id_: int = None, name: str = None, pages: int = None):
        """
        Инициализация объекта класса Book
        :param id_: id книги
        :param name: название книги
        :param pages: количество страниц у книги
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Представление объекта класса Book в виде строки
        :return: строка типа Книга "название_книги"
        """
        return 'Книга ' + '"' + self.name + '"'

    def __repr__(self) -> str:
        """
        Представление объекта класса Book
        :return:  валидная python строка
        """
        return self.__class__.__name__ + f"(id_={self.id}, name='{self.name}', pages={self.pages})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
