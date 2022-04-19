from LLD.HotelManagementSystem.models.User import User


class UserService:
    def __init__(self):
        self.__users = {}

    def resister_user(self, user: User):
        if user.get_userId() not in self.__users.keys():
            self.__users[user.get_userId()] = user
            return True
        raise ValueError('User Already Exists!')

    def remove_user(self, userId):
        if userId in self.__users:
            del self.__users[userId]
            return True
        raise ValueError('User Not Found!')


