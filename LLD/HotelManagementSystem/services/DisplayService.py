class DisplayService:
    def __init__(self):
        pass

    @staticmethod
    def display_vacant_rooms(hotel):
        print(f'Available Rooms: {hotel.get_vacant_rooms()}')

    @staticmethod
    def print_recent_transaction_by_user(user, txn):
        print(f'Most recent transaction made by user: {user.get_username()} \
         is {txn.get_transactions(user)[-1].get_amount()}')
