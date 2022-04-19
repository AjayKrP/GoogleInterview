from LLD.HotelManagementSystem.services.DisplayService import DisplayService
from LLD.HotelManagementSystem.services.PaymentService import PaymentService
from LLD.HotelManagementSystem.services.RoomService import RoomService
from LLD.HotelManagementSystem.services.UserService import UserService


class HotelSystem:
    def __init__(self, hotel):
        self.__user_service = UserService()
        self.__room_service = RoomService(hotel)
        self.__payment_service = PaymentService()
        self.__display_service = DisplayService()
        self.__current_user = None
        self.__current_hotel = hotel

    def get_user_service(self):
        return self.__user_service

    def get_payment_service(self):
        return self.__payment_service

    def get_room_service(self):
        return self.__room_service

    def get_display_service(self):
        return self.__display_service

    def get_current_user(self):
        return self.__current_user

    def get_current_hotel(self):
        return self.__current_hotel

    def set_current_user(self, user):
        self.__current_user = user

    def set_current_hotel(self, hotel):
        self.__current_hotel = hotel

    def checkin(self, user, no_of_guests):
        self.set_current_user(user)
        self.get_display_service().display_vacant_rooms(self.__current_hotel)
        amount_to_be_paid = self.get_room_service().book_room(user, no_of_guests)
        print(f'Amount to be paid is {amount_to_be_paid}.')
        self.get_display_service().display_vacant_rooms(self.__current_hotel)
        return self.get_payment_service().make_transaction(self.__current_user, amount_to_be_paid)

    def checkout(self, user):
        self.set_current_user(user)
        # TODO: calculate extra-charge in case of delay in checkout
        res = self.get_room_service().vacant_room(user)
        self.get_display_service().display_vacant_rooms(self.__room_service)
        return res

    def get_current_user_recent_transaction(self):
        if self.__current_user is not None:
            self.get_display_service().print_recent_transaction_by_user(self.__current_user, self.get_payment_service())
