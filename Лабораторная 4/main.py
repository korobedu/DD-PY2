class Program:
    """
    Класс, представляющий компьютерную программу
    """
    def __init__(self, name: str, version: str):
        """
        Инициализация объекта класса Program

        :param name: название программы
        :param version: номер версии программы
        """
        self.name = name
        self.version = version
        self.legacy_version = None

    def __str__(self) -> str:
        """
        Метод для строкового представления объекта класса Program

        :return: строковое представление объекта класса Program
        """
        return f"Название: {self.name}, версия: {self.version}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр класса Program.

        :return: строка, показывающая, как может быть инициализирован экземпляр класса Program
        """
        return f"{self.__class__.__name__}(name={self.name!r}, version={self.version!r}, " \
               f"legacy_version={self.legacy_version!r}"

    # TODO: один метод, который можно наследовать в дочерний
    def get_previous_version(self) -> str:
        """
        Метод возвращает номер предыдущей версии программы,
        если таковая имеется,
        как последний элемент списка legacy_version.

        :return: предыдущая версия программы
        """
        ...

    # TODO: один метод, который нужно перегрузить в дочернем (с обоснованием)
    def is_version_up_to_date(self) -> bool:
        """
        Метод, проверяющий, является ли текущая версия актуальной
        путем просомтра списка legacy_version на наличие аналогичной версии.
        Если такой версии не было и она "больше" предыдущих, то считаем, что версия актуальна

        :return: True, если версия самая актуальная и False если нет
        """
        ...


class Net:
    """
    Класс, представляющий работу в сети
    """
    def __init__(self, ip_client: str, ip_server: str):
        """
        Инициализация объекта класса Net

        :param ip_client: IP-адрес клиента
        :param ip_server: IP-адрес сервера
        """
        self.ip_client = ip_client
        self.ip_server = ip_server

    def __str__(self) -> str:
        """
        Метод для строкового представления объекта класса Net

        :return: строковое представление объекта класса Program
        """
        return f"IP клиента: {self.ip_client}, IP сервера: {self.ip_server}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр класса Net.

        :return: строка, показывающая, как может быть инициализирован экземпляр класса Net
        """
        return f"{self.__class__.__name__}(ip_client={self.ip_client!r}, ip_server={self.ip_server!r}"

    # TODO: один метод, который можно наследовать в дочерний
    def change_ip_version(self, ip_version: int, type_: str) -> str:
        """
        Изменение версии ip адреса

        :param ip_version: версия 4 или 6
        :param type_: 'server' или 'client'
        :return: Измененный ip адрес
        """
        ...

    # TODO: один метод, который нужно перегрузить в дочернем (с обоснованием)
    def is_ipserver_right(self) -> bool:
        """
        Проверка отвечает ли сервер на запросы

        :return: True, если сервер ответает на запросы, False, если нет
        """
        ...


class Game(Program, Net):
    """
    Класс, представляющий компьютерную игру

    Строковое представление класса наследуется из базового класса Program.
    """
    def __init__(self, name: str, version: str,
                 ip_client: str, ip_server: str,
                 account: dict,
                 ):
        """
        Инициализация объекта класса Game

        :param name: название игры
        :param version: номер версии игры
        :param ip_client: IP-адрес пользователя
        :param ip_server: IP-адрес сервера игры
        :param account: аккаунт игрока
        """
        Program.__init__(name, version)
        Net.__init__(ip_client, ip_server)
        self.account = account

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр класса Game.

        :return: строка, показывающая, как может быть инициализирован экземпляр класса Game
        """
        return f"{self.__class__.__name__}(name={self.name!r}, version={self.version!r}, " \
               f"legacy_version={self.legacy_version!r}, ip_client={self.ip_client!r}, " \
               f"ip_server={self.ip_server!r}, account={self.account}"

    def is_version_up_to_date(self) -> bool:
        """
        Проверка соответствия текущей версии игры самой актуальной
        версии (получаем от сервера)
        для текущего региона игрока (получаем из account).

        Перегружаем, так как теперь есть зависимость от региона
        игрока (получаем из account).

        :return: True, если версия актуальна и False, если нет
        """
        ...

    def is_ipserver_right(self) -> bool:
        """
        Проверка соответствия IP-адреса текущего сервера,
        IP-ардесу сервера для региона игрока (необходимо для
        оптимизации нагрузки на сервер и увеличения скорости
        передачи по сети) и его работоспособность.

        Перегружаем, так как теперь есть зависимость от региона
        игрока (получаем из account).

        :return: True, если сервер подходящий и рабочий и False, в противном случае
        """
        ...


if __name__ == "__main__":
    # Write your solution here
    pass
