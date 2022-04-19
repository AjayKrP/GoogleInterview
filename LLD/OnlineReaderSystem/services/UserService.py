from OnlineReaderSystem.models.User import User


class UserService:
    def __init__(self):
        self.__users = {}

    def add_user(self, user):
        if user.username not in self.__users.keys():
            self.__users[user.username] = user
            return True
        raise ValueError('User already exists!')

    def remove_user(self, username):
        for idx, usr in enumerate(self.__users.items()):
            if username == usr[username]:
                del self.__users[idx]
                return True
        raise ValueError('user does not exists!')

    def __str__(self):
        output = ''
        for username in self.__users.keys():
            output += self.__users[username]

        return output

    def create_membership(self, user):
        pass

    def extend_membership(self, user):
        pass

    def cancel_membership(self):
        pass
