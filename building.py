class Building:

    def __init__(self, obj_type, address, seller_id):
        self.__id = id(self)
        self.__obj_type = obj_type
        self.__address = address
        self.__seller_id = seller_id

    @property
    def id(self):
        return self.__id

    @property
    def obj_type(self):
        return self.__obj_type

    @property
    def address(self):
        return self.__address

    @property
    def seller_id(self):
        return self.__seller_id

    def change_seller(self, new_id):
        self.__seller_id = new_id

    def show_info(self):
        print('-------------------------')
        print(f'{self.__obj_type}')
        print(f'{self.__address}')
        print('-------------------------')
