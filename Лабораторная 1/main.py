import doctest
from typing import Union


class Zoo:
    def __init__(self, animals: dict, number_of_cages: int):
        """
        Создание объекта класса Зоопарк

        :param animals: Животные обитающие в зоопарке
        :param number_of_cages: Количество клеток в зоопарке

        Примеры:
        >>> moscow_zoo = Zoo({'Лев': 5}, 6) # Инициализация экземпляра класса
        """

        if not isinstance(animals, dict):
            raise TypeError("animals")
        self.animals = animals

        if not isinstance(number_of_cages, int):
            raise TypeError("number_of_cages")
        if number_of_cages < 0:
            raise ValueError("number_of_cages")
        self.number_of_cages = number_of_cages

    def add_animals(self, new_animals: dict) -> None:
        """
        Функция, добавляющая животных в зоопарк

        :param new_animals: Новые животные и их количество

        Примеры:
        >>> moscow_zoo = Zoo({'Лев': 5}, 6)
        >>> moscow_zoo.add_animals({'Слон': 1})
        """

        ...

    def add_cages(self, num: int) -> None:
        """
        Функция, добавляющая новые клетки в зоопарк

        :param num: Количество новых клеток

        Примеры:
        >>> moscow_zoo = Zoo({'Лев': 5}, 6)
        >>> moscow_zoo.add_cages(5)
        """

        ...

    def number_of_animals(self) -> int:
        """
        Функция для подсчёта количества всех животных в зоопарке

        :return: Количество всех животных

        Примеры:
        >>> moscow_zoo = Zoo({'Лев': 5}, 6)
        >>> moscow_zoo.number_of_animals()
        """

        ...


class Shop:
    def __init__(self, number_of_staff: int, income: Union[float, int]):
        """
        Создание объекта класса Магазин

        :param number_of_staff: Число работников в магазине
        :param income: Доход магазина

        Примеры:
        >>> shop_dns = Shop(16000, 200000)
        """

        if not isinstance(number_of_staff, int):
            raise TypeError("number_of_staff")
        if number_of_staff < 0:
            raise ValueError("number_of_staff")
        self.number_of_staff = number_of_staff

        if not isinstance(income, (float, int)):
            raise TypeError("income")
        self.income = income

    def add_staff(self, num: int):
        """
        Функция, добавляющая новых работников

        :param num: Количество новых работников

        Пример:
        >>> shop_dns = Shop(16000, 200000)
        >>> shop_dns.add_staff(200)
        """

        ...

    def new_income(self, income: Union[float, int]):
        """
        Функция, устанавливающая новый доход

        :param income: Новый доход

        Пример:
        >>> shop_dns = Shop(16000, 200000)
        >>> shop_dns.new_income(180000)
        """

        ...


class University:
    def __init__(self, type_: str, name: str):
        """
        Создание нового объекта класса Университет

        :param type_: Тип университета ('public' - государственный,
                                        'private' - частный)
        :param name: Название университета

        Пример:
        >>> new_uni = University('private', 'Russian New University')
        """

        if not isinstance(type_, str):
            raise TypeError("type_")
        if not (str == 'public' or type_ == 'private'):
            raise ValueError("type_")
        self.type_ = type_

        if not isinstance(name, str):
            raise TypeError("name")
        self.name = name

    def change_name(self, name: str):
        """
        Изменить название университета

        :param name: Новое название университета

        Пример:
        >>> new_uni = University('private', 'Russian New University')
        >>> new_uni.change_name('RSN')
        """

        ...

    def change_type(self, type_: str):
        """
        Изменить тип университета

        :param type_: Новый тип университета

        Пример:
        >>> new_uni = University('private', 'Russian New University')
        >>> new_uni.change_type('public')
        """

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
