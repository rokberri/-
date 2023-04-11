from user import User
from reestr import Reestr, REESTR


class Seller(User):

    def __init__(self, name, phone_num):
        super().__init__('seller', name, phone_num)

    def sell(self, *obj, r=REESTR):
        for item in obj:
            r.add_new(item)


# обертка
def register( name, phone_num):
    seller = Seller(name, phone_num)
    print(f'Пользователь {name} успешно зарегистрирован')
    return seller
