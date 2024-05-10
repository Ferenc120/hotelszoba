import tkinter as tk
from tkinter import ttk, scrolledtext
from DoubleRoom import DoubleRoom
from SingleRoom import SingleRoom
from Suit import Suit
from Hotel import Hotel
from Reservation import Reservation

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Booking System")
        master.geometry("800x600")

        # Fő keret
        self.main_frame = tk.Frame(master, bg="white")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Üdvözlő szöveg
        self.label = tk.Label(self.main_frame, text="Welcome to Booking System", fg="red", bg="white", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        # Szoba szám bekérés
        self.room_number_label = tk.Label(self.main_frame, text="Enter Room Number:", bg="white")
        self.room_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.room_number_entry = tk.Entry(self.main_frame)
        self.room_number_entry.grid(row=1, column=1, padx=10, pady=5)

        # Dátum bekérés
        self.date_label = tk.Label(self.main_frame, text="Enter Date (YYYY-MM-DD):", bg="white")
        self.date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.date_entry = tk.Entry(self.main_frame)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Gombok
        buttons_frame = tk.Frame(self.main_frame, bg="white")
        buttons_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.book_button = tk.Button(buttons_frame, text="Book a Room", command=self.book_room)
        self.book_button.grid(row=0, column=0, padx=5)

        self.availability_button = tk.Button(buttons_frame, text="Check Room Availability", command=self.check_availability)
        self.availability_button.grid(row=0, column=1, padx=5)

        self.list_prices_button = tk.Button(buttons_frame, text="List Room Prices", command=self.list_room_prices)
        self.list_prices_button.grid(row=0, column=2, padx=5)

        self.room_property_button = tk.Button(buttons_frame, text="Room Property", command=self.room_property)
        self.room_property_button.grid(row=0, column=3, padx=5)

        self.cancel_booking_button = tk.Button(buttons_frame, text="Cancel a Booking", command=self.cancel_booking)
        self.cancel_booking_button.grid(row=0, column=4, padx=5)

        self.list_booked_button = tk.Button(buttons_frame, text="List Booked Rooms", command=self.list_booked_rooms)
        self.list_booked_button.grid(row=0, column=5, padx=5)

        # Text mező a válaszok megjelenítéséhez
        self.text_box = scrolledtext.ScrolledText(self.main_frame, width=70, height=15)
        self.text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Hotel példány létrehozása és adatok betöltése
        self.booking = Booking()
        self.booking.load_data()

    def book_room(self):
        room_number = self.room_number_entry.get()
        date = self.date_entry.get()
        if self.booking.hotel.book_room_by_number(room_number, date):
            self.append_to_text_box(f"Room {room_number} successfully booked for {date}.")
        else:
            self.append_to_text_box("Room is already booked for the selected date.")

    def check_availability(self):
        date = self.date_entry.get()
        available_rooms = self.booking.hotel.check_availability(date)
        self.append_to_text_box(f"Available rooms: {', '.join(available_rooms)}")

    def list_room_prices(self):
        room_prices = self.booking.hotel.get_room_prices()
        self.append_to_text_box("Room prices:")
        for room_number, price in room_prices.items():
            self.append_to_text_box(f"- Room {room_number}: {price}")

    def room_property(self):
        self.append_to_text_box("Room property:")
        room_properties_text = self.booking.hotel.write_room_property()
        self.append_to_text_box(room_properties_text)

    def cancel_booking(self):
        room_number = self.room_number_entry.get()
        date = self.date_entry.get()
        if self.booking.hotel.cancel_booking(room_number, date):
            self.append_to_text_box(f"Booking for room {room_number} on {date} successfully canceled.")
        else:
            self.append_to_text_box("No booking found for the given room and date.")

    def list_booked_rooms(self):
        booked_rooms = self.booking.hotel.list_booked_rooms()
        self.append_to_text_box("Booked rooms:")
        for room_number, dates in booked_rooms.items():
            self.append_to_text_box(f"Room {room_number} is booked on the following dates:")
            for date in dates:
                self.append_to_text_box(f"- {date}")

    def append_to_text_box(self, text):
        self.text_box.insert(tk.END, text + "\n")

class Booking:
    def __init__(self):
        self.hotel = Hotel()

    def load_data(self):
        self.hotel.add_room(SingleRoom("101", "25000"))
        self.hotel.add_room(SingleRoom("70", "19500"))
        self.hotel.add_room(DoubleRoom("201", "20000"))
        self.hotel.add_room(Suit("504", "30000"))

        self.hotel.book_room_by_number("101", "2024-05-10")
        self.hotel.book_room_by_number("70", "2024-05-11")
        self.hotel.book_room_by_number("201", "2024-05-12")
        self.hotel.book_room_by_number("504", "2024-05-13")
        self.hotel.book_room_by_number("101", "2024-05-14")

root = tk.Tk()
gui = GUI(root)
root.mainloop()
