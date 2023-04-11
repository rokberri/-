class User:
    # по факту создание и являтся регистрацией но чисто на всякий случай сделаю обёртку для каждого потомка
    def __init__(self, type_of_user, name, phone_num):
        self.__id = id(self)
        self.__type = type_of_user
        self.__name = name
        self.__phone_num = phone_num

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name

    @property
    def phone_num(self):
        return self.__phone_num

