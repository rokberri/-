from reestr import REESTR
from user import User


class Buyer(User):

    def __init__(self, name, phone_num):
        super().__init__('buyer', name, phone_num)

    def look(self, r=REESTR.base):
        for item in r:
            item.show_info()

    def buy(self, obj, reeltor, seller, date, r=REESTR):
        reeltor.register_deal(seller, self, obj, date, r)


def register(name, phone_num):
    buyer = Buyer(name, phone_num)
    print(f'Пользователь {name} успешно зарегистрирован')
    return buyer
