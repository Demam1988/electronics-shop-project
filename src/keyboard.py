from src.item import Item


class MixinLan:

    Language = "EN"

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        """ Возвращает атрибут language. """
        return self.__language

    def change_lang(self):
        """ Метод для изменения языка (раскладки клавиатуры). """

        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

        return self.language


class Keyboard(Item, MixinLan):
    pass
