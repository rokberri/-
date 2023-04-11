class Deal:

    def __init__(self, seller_id, buyer_id, reeltor_id, obj_id, date):
        self.__id = id(self)
        self.__seller = seller_id
        self.__buyer = buyer_id
        self.__reelor = reeltor_id
        self.__obj = obj_id
        self.__date = date

    @property
    def id(self):
        return self.__id

    @property
    def seller(self):
        return self.__seller

    @property
    def buyer(self):
        return self.__buyer

    @property
    def reeltor(self):
        return self.__reelor

    @property
    def obj(self):
        return self.__obj

    @property
    def date(self):
        return self.__date
