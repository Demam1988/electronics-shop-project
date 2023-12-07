from src.item import Item


class MixinLan:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(MixinLan, Item):
    pass