class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_username(self):
        return self.username

    def __str__(self):
        return f'Current User: {self.username}'
