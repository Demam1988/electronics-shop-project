"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

from src.phone import Phone


def test_calculate_total_price():
    """
    Рассчитываем Общая стоимость товара
    """
    price = 10
    quantity = 10
    total_cost = price * quantity
    assert total_cost == 100


def test_apply_discount():
    """
    Применяет установленную скидку
    """
    price = 100000
    pay_rate = 0.8
    price = price * pay_rate
    assert price == 80000.0


@pytest.fixture()
def item():
    return Item("Bob", 1000, 5)


def test_getters(item):
    assert item.name == "Bob"
    assert item.price == 1000
    assert item.quantity == 5


def test__repr__():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str__():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"




@pytest.fixture()
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


@pytest.fixture()
def number_of_sim():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(number_of_sim):
    number_of_sim.number_of_sim = 1
    assert number_of_sim.number_of_sim == 1
    with pytest.raises(ValueError):
        number_of_sim.number_of_sim = 0
        number_of_sim.number_of_sim = -1
        number_of_sim.number_of_sim = 2.0
        number_of_sim.number_of_sim = '2.0'


@pytest.fixture()
# Тестируем сложение по атрибуту 'quantity'
def phone1():
    return Phone('iPhone 14', 120_000, 5, 2)


@pytest.fixture()
# Тестируем сложение по атрибуту 'quantity'
def item1():
    return Item("Смартфон", 10000, 20)


def test_add(phone1, item1):
    assert phone1 + item1 == 25
