class Cart:
    def __init__(self, cart_id, user_id):
        self.user_id = user_id
        self.cart_id = cart_id
        self.items = []

    def get_totals(self):
        pass