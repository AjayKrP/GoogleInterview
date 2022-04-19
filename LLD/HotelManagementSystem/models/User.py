class User:
    def __init__(self, userId, name, phone):
        self.__userId = userId
        self.__name = name
        self.__phone = phone

    def get_userId(self):
        return self.__userId

    def get_username(self):
        return self.__name

    def get_phone(self):
        return self.__phone
   