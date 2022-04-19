from LLD.HotelManagementSystem.HotelSystem import HotelSystem
from LLD.HotelManagementSystem.models.Hotel import Hotel
from LLD.HotelManagementSystem.models.User import User

if __name__ == "__main__":
    hotel = Hotel(1, 'Hayat Place', 'Hinjewadi')
    hms = HotelSystem(hotel)

    user1 = User(1, 'Ajay', '9999999999')
    hms.checkin(user1, 44)