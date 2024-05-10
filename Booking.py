from DoubleRoom import DoubleRoom
from SingleRoom import SingleRoom
from Suit import Suit
from Hotel import Hotel
from Reservation import  Reservation

class Booking:
  def __init__(self):
    self.hotel = Hotel()

  def load_data(self):
    self.hotel.add_room(SingleRoom("101", "25000"))
    self.hotel.add_room(SingleRoom("70", "19500"))
    self.hotel.add_room(DoubleRoom("201", "20000"))
    self.hotel.add_room(Suit("504", "30000"))

    booking.hotel.book_room_by_number("101", "2024-05-10")
    booking.hotel.book_room_by_number("70", "2024-05-11")
    booking.hotel.book_room_by_number("201", "2024-05-12")
    booking.hotel.book_room_by_number("504", "2024-05-13")
    booking.hotel.book_room_by_number("101", "2024-05-14")

  def user_interact(self):
    while True:
      print("1. Book a room")
      print("2. Check room availability")
      print("3. List room prices")
      print("4. Room property")
      print("5. Cancel a booking")
      print("6. List booked rooms")
      print("7. Exit")

      user_choice = input("Choose from the options: ")

      if user_choice == "1":
        room_number = input("Enter the room number to book: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        if self.hotel.book_room_by_number(room_number, date):
          print(f"Room {room_number} successfully booked for {date}.")
        else:
          print("Room is already booked for the selected date.")
      elif user_choice == "2":
        date = input("Enter the date (YYYY-MM-DD): ")
        print("Available rooms: ", self.hotel.check_availability(date))
      elif user_choice == "3":
        print("Room price: ", self.hotel.get_room_prices())
      elif user_choice == "4":
        print("Room property: ", self.hotel.write_room_property())
      elif user_choice == "5":
        room_number = input("Enter the room number to cancel: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        if self.hotel.cancel_booking(room_number, date):
          print(f"Booking for room {room_number} on {date} successfully canceled.")
        else:
          print("No booking found for the given room and date.")
      elif user_choice == "6":
        booked_rooms = self.hotel.list_booked_rooms()
        for room_number, dates in booked_rooms.items():
          print(f"Room {room_number} is booked on the following dates:")
          for date in dates:
            print(f"- {date}")

      elif user_choice == "7":
        break

booking = Booking()
booking.load_data()
booking.user_interact()

