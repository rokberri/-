import deal
from reestr import REESTR
from user import User


class Reeltor(User):

    def __init__(self, name, phone_num):
        super().__init__('reeltor', name, phone_num)

    def add_to_reester(self, *obj, r=REESTR):
        for item in obj:
            r.add_new(item)

    def show(self, obj, r=REESTR.base):
        return r.get_obj(obj)


    def register_deal(self, seller, buyer, obj, date, l=REESTR):
        l.remove_obj(obj)
        return deal.Deal(seller, buyer, self.id, obj, date)


def register(name, phone_num):
    reeltor = Reeltor(name, phone_num)
    print(f'Пользователь {name} успешно зарегистрирован')
    return reeltor
