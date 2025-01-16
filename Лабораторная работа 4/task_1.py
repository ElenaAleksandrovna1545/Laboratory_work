class Animal:
    """
    Базовый класс для животных.
    Содержит общие атрибуты и методы, характерные для всех животных.
    """
    def __init__(self, name: str, age: int):
        """
        Инициализация атрибутов животного.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        :return: Строка с именем и возрастом.
        """
        return f"{self.name}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление животного.
        :return: Строка для отладки.
        """
        return f"Animal(name='{self.name}', age={self.age})"

    def make_sound(self) -> str:
        """
        Генерирует звук, издаваемый животным.
        :return: Звук животного в виде строки.
        """
        return "Неизвестный звук"


class Dog(Animal):
    """
    Дочерний класс для собак.
    Расширяет и модифицирует функциональность базового класса Animal.
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация атрибутов собаки.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Унаследованная инициализация имени и возраста.
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.
        Переопределено, чтобы включать породу.
        :return: Строка с именем, возрастом и породой.
        """
        return f"{self.name}, возраст: {self.age} лет, порода: {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление собаки.
        :return: Строка для отладки.
        """
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Генерирует звук, издаваемый собакой.
        Перегружено, так как собаки издают специфический звук — лай.
        :return: Звук собаки.
        """
        return "Гав-гав!"

    def fetch(self, item: str) -> str:
        """
        Метод для симуляции команды "принеси".
        :param item: Предмет, который собака должна принести.
        :return: Строка, описывающая результат.
        """
        return f"{self.name} принес(ла) {item}."


class Cat(Animal):
    """
    Дочерний класс для кошек.
    Расширяет и модифицирует функциональность базового класса Animal.
    """
    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация атрибутов кошки.
        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление кошки.
        Переопределено, чтобы включать цвет.
        :return: Строка с именем, возрастом и цветом.
        """
        return f"{self.name}, возраст: {self.age} лет, цвет: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление кошки.
        :return: Строка для отладки.
        """
        return f"Cat(name='{self.name}', age={self.age}, color='{self.color}')"

    def make_sound(self) -> str:
        """
        Генерирует звук, издаваемый кошкой.
        Перегружено, так как кошки издают специфический звук — мяуканье.
        :return: Звук кошки.
        """
        return "Мяу!"

    def scratch(self) -> str:
        """
        Метод для симуляции царапанья.
        :return: Строка, описывающая действие кошки.
        """
        return f"{self.name} поцарапал(а) мебель!"


if __name__ == "__main__":
    dog = Dog(name="Шарик", age=3, breed="Лабрадор")
    cat = Cat(name="Мурка", age=2, color="Белый")

    print(dog)  # Шарик, возраст: 3 лет, порода: Лабрадор
    print(cat)  # Мурка, возраст: 2 лет, цвет: Белый

    print(dog.make_sound())  # Гав-гав!
    print(cat.make_sound())  # Мяу!

    print(dog.fetch("мячик"))  # Шарик принес(ла) мячик.
    print(cat.scratch())  # Мурка поцарапал(а) мебель!
