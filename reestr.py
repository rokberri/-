class Reestr:

    def __init__(self):
        self.__base = list()

    @property
    def base(self):
        return self.__base

    def add_new(self, obj):
        self.__base.append(obj)

    def get_obj(self, index):
        return self.__base[index]

    def remove_obj(self, obj):
        self.__base.remove(obj)


REESTR = Reestr()
