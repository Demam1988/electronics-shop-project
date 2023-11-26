import pytest

from src.item import Item
from src.phone import Phone



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
