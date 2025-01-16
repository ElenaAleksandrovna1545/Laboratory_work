class Table:
    def __init__(self, material: str, shape: str, height: float):
        """
        Инициализирует объект класса Table.

        :param material: Материал, из которого изготовлен стол (например, дерево, металл).
        :param shape: Форма стола (например, круглый, прямоугольный).
        :param height: Высота стола в метрах.
        :raises ValueError: Если высота меньше 0.3 или больше 2.0 метров.
        """
        if height < 0.3 or height > 2.0:
            raise ValueError("Высота стола должна быть в диапазоне от 0.3 до 2.0 метров.")
        self.material = material
        self.shape = shape
        self.height = height

    def adjust_height(self, new_height: float) -> None:
        """
        Изменяет высоту стола.

        :param new_height: Новая высота стола в метрах.
        :raises ValueError: Если высота меньше 0.3 или больше 2.0 метров.

        >>> table = Table("wood", "round", 0.75)
        >>> table.adjust_height(0.9)
        """
        if new_height < 0.3 or new_height > 2.0:
            raise ValueError("Высота стола должна быть в диапазоне от 0.3 до 2.0 метров.")
        self.height = new_height

    def describe(self) -> str:
        """
        Возвращает описание стола.

        :return: Строка с описанием.

        >>> table = Table("wood", "round", 0.75)
        >>> table.describe()
        'Стол из материала wood, форма round, высота 0.75 м.'
        """
        return f"Стол из материала {self.material}, форма {self.shape}, высота {self.height} м."


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Инициализирует объект класса Tree.

        :param species: Вид дерева (например, дуб, сосна).
        :param age: Возраст дерева в годах.
        :param height: Высота дерева в метрах.
        :raises ValueError: Если возраст или высота отрицательные.
        """
        if age < 0 or height < 0:
            raise ValueError("Возраст и высота не могут быть отрицательными.")
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.

        :param years: Количество лет, на которое дерево выросло.
        :raises ValueError: Если количество лет отрицательное.

        >>> tree = Tree("oak", 10, 5.0)
        >>> tree.grow(5)
        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")
        self.age += years
        self.height += years * 0.5  # Дерево растёт на 0.5 м в год

    def describe(self) -> str:
        """
        Возвращает описание дерева.

        :return: Строка с описанием.

        >>> tree = Tree("oak", 10, 5.0)
        >>> tree.describe()
        'Дерево вида oak, возраст 10 лет, высота 5.0 м.'
        """
        return f"Дерево вида {self.species}, возраст {self.age} лет, высота {self.height} м."

    class SocialNetwork:
        def __init__(self, name: str, users: int, monthly_active_users: int):
            """
            Инициализирует объект класса SocialNetwork.

            :param name: Название социальной сети.
            :param users: Общее количество пользователей.
            :param monthly_active_users: Количество активных пользователей за месяц.
            :raises ValueError: Если количество пользователей меньше 0.
            """
            if users < 0 or monthly_active_users < 0:
                raise ValueError("Количество пользователей не может быть отрицательным.")
            if monthly_active_users > users:
                raise ValueError("Число активных пользователей не может превышать общее количество пользователей.")
            self.name = name
            self.users = users
            self.monthly_active_users = monthly_active_users

        def add_users(self, new_users: int) -> None:
            """
            Добавляет новых пользователей.

            :param new_users: Количество новых пользователей.
            :raises ValueError: Если количество новых пользователей отрицательное.

            >>> network = SocialNetwork("Facebook", 1000, 800)
            >>> network.add_users(200)
            """
            if new_users < 0:
                raise ValueError("Количество новых пользователей не может быть отрицательным.")
            self.users += new_users

        def engagement_rate(self) -> float:
            """
            Рассчитывает коэффициент вовлечённости.

            :return: Доля активных пользователей.

            >>> network = SocialNetwork("Facebook", 1000, 800)
            >>> network.engagement_rate()
            0.8
            """
            return self.monthly_active_users / self.users

