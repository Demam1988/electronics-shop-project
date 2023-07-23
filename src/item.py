import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    PATH_DIR = os.path.abspath('../src/')
    PATH_CSV = os.path.join(PATH_DIR, 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)


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
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost


    def apply_discount(self) -> None:
        """
       Применяет установленную скидку для конкретного товара.
       """
        discoun = self.price * self.pay_rate
        self.price = discoun

    @classmethod
    def instantiate_from_csv(cls, path=PATH_CSV):
        with open(path, newline='', encoding='1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for x in reader:
                cls(x["name"], x["price"], x["quantity"])


    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))



