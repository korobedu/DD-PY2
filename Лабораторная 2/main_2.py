from typing import List

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


# TODO написать класс Library
class Library:
    """
    Класс, представляющий библиотеку из книг
    """
    def __init__(self, books: list = []):
        """
        Инициализация объекта класса Library
        :param books: список из книг (объектов класса Book)
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: идентификатор для добавляния новой книги
        """
        return self.books[-1].id + 1 if len(self.books) != 0 else 1

    def get_index_by_book_id(self, id_: int):
        """
        Метод, возвращающий индекс книги в списке
        :param id_: запрашиваемый на поиск id книги
        :return: индекс книги в списке
        """
        for book_ in enumerate(self.books):
            if book_[1].id == id_:
                return book_[0]
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
