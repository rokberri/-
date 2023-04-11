from datetime import date

import building
import buyer
import reeltor
import reestr
import seller


def main():
    sel_man = seller.register('A', '123')
    buy_man = buyer.register('B', '456')
    reeltor_man = reeltor.register('C', '789')

    house = building.Building('house', 'str Kirova', sel_man.id)
    flat = building.Building('flat', 'str Dimitrova', sel_man.id)

    sel_man.sell(house, flat)

    buy_man.look()

    buy_man.buy(flat, reeltor_man, sel_man, date.today())

    buy_man.look()


if __name__ == '__main__':
    main()


