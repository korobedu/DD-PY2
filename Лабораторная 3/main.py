class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_: str):
        self._name = name_

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author_: str):
        self._author = author_


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, " \
               f"pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages_: int):
        if 0 > pages_:
            raise ValueError('pages < 0')
        if not isinstance(pages_, int):
            raise TypeError("pages isn't int")
        self._pages = pages_


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, " \
               f"pages={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration_: float):
        if duration_ < 0:
            raise ValueError("duration < 0")
        if not isinstance(duration_, float):
            raise TypeError("duration isn't float")
        self._duration = duration_
