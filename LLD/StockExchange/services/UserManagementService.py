class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.id not in self.users:
            self.users[user.id] = user
            return True
        return False

    def get_user(self, user):
        return self.users[user.id]

    def remove_user(self, user):
        if user.id in self.users:
            self.users.pop(user.id)
            return True
        return False
