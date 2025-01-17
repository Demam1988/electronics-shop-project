import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'
    def __str__(self):
        return f'{self.message}'


class Item:
    """Класс для представления товара в магазине."""

    pay_rate = 1.0
    all = []
    PATH_DIR = os.path.abspath('../src/')
    PATH_CSV = os.path.join(PATH_DIR, 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item.:param name: Название товара. :param price: Цена за единицу товара. :param
        quantity: Количество товара в магазине."""
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]



    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.:return: Общая стоимость товара."""

        total_cost = self.price * self.quantity
        return total_cost


    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""

        discoun = self.price * self.pay_rate
        self.price = discoun

    @classmethod
    def instantiate_from_csv(cls, path=PATH_CSV, file_path="..\src\item.csv"):
        cls.all = []
        try:
            with open(file_path) as csvfile:
                readers = csv.DictReader(csvfile)
                for reader in readers:
                    try:
                        if len(reader) != 3:
                            raise InstantiateCSVError()
                    except InstantiateCSVError as message:
                        print(message)
                        return message
                        # break
                    else:
                        name = reader['name']
                        price = reader['price']
                        quantity = reader['quantity']
                        Item(name=name, price=price, quantity=quantity)
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл items.csv')


    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))

    def __add__(self, other):
        """ Возвращает сумму двух экземпляров """

        if self.validate(other):
            return self.quantity + other.quantity

    @classmethod
    def validate(cls, obj):
        """ Проверка на соответствие классу. """

        if not isinstance(obj, Item):
            raise TypeError('Объект должен быть экземпляром класса '
                            'Item или Phone!')
        return True

