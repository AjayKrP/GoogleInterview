class Hotel:
    __locations = [Location]
    __name = None


class Location:
    _street = None
    _city = None
    _pincode = None
    country = None


class Room:
    room_number: None
    type: RoomType
    style: RoomStyle
    booking_status: None


class RoomKey:
    rooms = []
    is_master: None

    def get_room(self):
        pass


class Person:
    name: None
    email: None
    mobile: None


class RoomBooking:
    reservation_id: None
    end_date: None
    duration_stay: None
    checkin: None
    checkout: None

    def create_booking(self, user_id):
        pass

    def booking_details(self):
        pass


class Guest(Person):
    room_booking: RoomBooking
