from datetime import datetime
from Reservation import  Reservation
class Hotel:
  def __init__(self):
    self.rooms = []
    self.reservations = []
    self.room_property = {
      "101": ["klima", "refrigerator"],
      "70": ["tv", "jakuzi"],
      "504": ["Minibar"],
      "201": [],
    }

  def add_room(self, room):
    self.rooms.append(room)

  def is_room_booked(self, room_number, date):
    for reservation in self.reservations:
      if reservation.room_number == room_number and reservation.date == date:
        return True
    return False

  def check_availability(self,date):
    available_rooms = []
    for room in self.rooms:
      if not self.is_room_booked(room.number, date):
        available_rooms.append(room.number)
    return available_rooms

  def book_room_by_number(self, room_number, date):
    for room in self.rooms:
      if room.number == room_number and not self.is_room_booked(room_number, date):
        room.book_room()
        self.reservations.append(Reservation(room_number, date))
        return True
    return False

  def get_room_prices(self):
    return {room.number: room.price for room in self.rooms}

  """def write_room_property(self):
    for room_number, property in self.room_property.items():
      property_str = ", ".join(property) if property else "Nothing"
      print(f"{room_number} room has : {property_str} .")"""

  def write_room_property(self):
    room_properties_text = ""
    for room_number, properties in self.room_property.items():
      properties_str = ", ".join(properties) if properties else "Nothing"
      room_properties_text += f"{room_number} room has: {properties_str}\n"
    return room_properties_text

  def cancel_booking(self, room_number, date):
    for reservation in self.reservations:
      if reservation.room_number == room_number and reservation.date == date:
        for room in self.rooms:
          if room.number == room_number:
            room.unbook_room()
        self.reservations.remove(reservation)
        return True
    return False

  def list_booked_rooms(self):
    booked_rooms = {}
    for reservation in self.reservations:
      if reservation.room_number not in booked_rooms:
        booked_rooms[reservation.room_number] = [reservation.date]
      else:
        booked_rooms[reservation.room_number].append(reservation.date)
    return booked_rooms

