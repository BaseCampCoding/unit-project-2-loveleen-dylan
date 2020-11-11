import sqlite3
from classes import Rooms
from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk




con = sqlite3.connect("RESERVME.db")
c = con.cursor()


print("WELCOME TO ReservME WHERE YOU RESERVE FOR A ME!\n\n\We are delighted to have you here with us today.\n\nLet's get started!")
print("We have 5 types of rooms.")
print("\n" + "\033[1m" + "Studio Suite: ")

# "\033[0m"
print("\033[0m" + str((Rooms("Studio Suite"))))

print("\n" + "\033[1m" + "One-Bedroom Suite: ")
print("\033[0m" + str((Rooms("One-Bedroom Suite"))))

print("\n\n" + "\033[1m" + "Two-Bedroom Suite: ")
print("\033[0m" + str((Rooms("Two-Bedroom Suite"))))

print("\n\n" + "\033[1m" + "Presidential Suite: ")
print("\033[0m" + str((Rooms("Presidential Suite"))))

print("\n\n" + "\033[1m" + "Premium Suite: ")
print("\033[0m" + str((Rooms("Premium Suite"))))

# input_room_type = room_type.lower()
# for i in ROOMS:
#     if input_room_type not in ROOMS:
#         print("That room does not exist. Please try again.")
#         room_type = input("\n" + "What type of room would you like to reserve today?: ")

# print("Great. Before you can reserve a hotel room we need some information.")

# con.commit()
# con.close()
root = Tk()
root.title(" Rooms")
root.iconbitmap(
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-bkeqe&psig=AOvVaw2oBqXabpCHoyEx9EyMKvdl&ust=1605115375818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDPvfG--OwCFQAAAAAdAAAAABAh"
)
root.geometry("200x100")

# room_t = Entry(root, width=30)
# room_t.grid(row=0, column=1)
# room_population = Entry(root, width=30)
# room_population.grid(row=1, column=1)
# price = Entry(root, width=30)
# price.grid(row=2, column=1)

# room_t_label = Label(root, text="Room Type")
# room_t_label.grid(row=0, column=0)
# room_population_label = Label(root, text="Room Capacity")
# room_population_label.grid(row=1, column=0)
# price_label = Label(root, text="Price")
# price_label.grid(row=2, column=0)
room_label_entry = Entry(root, width=30)
room_label_entry.grid(row=2, column=0)
room_label = Label(root, text="Room Type")
room_label.grid(row=1, column=0)

ROOMS= ['studio suite', 'one-bedroom suite', 'two-bedroom suite', 'presidential suite', 'premium suite']


def submit():
    root = Tk()
    room_label_get = room_label_entry.get()
    input_room_type = room_label_get.lower()
    if input_room_type not in ROOMS:
        messagebox.showerror("Error", "The room you are looking for is not available. Please try again.")
    if input_room_type == "studio suite":
        room = "Studio Suite"
        return room
    elif input_room_type == "one-bedroom suite":
        room = "One-Bedroom Suite"
        return room
    elif input_room_type == "two-bedroom suite":
        room_type = "Two-Bedroom Suite"
        return room
    elif input_room_type == "presidential suite":
        room_type = "Presidential Suite"
        return room
    elif input_room_type == "premium suite":
        room_type = "Premium Suite"
        return room
    root.title(" Available Rooms")
    root.iconbitmap(
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-bkeqe&psig=AOvVaw2oBqXabpCHoyEx9EyMKvdl&ust=1605115375818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDPvfG--OwCFQAAAAAdAAAAABAh"
    )
    root.geometry("300x300")
    c.execute(
        "SELECT roomID,availability,room_type,price FROM RoomsAvailability WHERE room_type =(?) AND  availability = 'Available'",
        (room,),
    )
    rooms = c.fetchall()

    print_info = ""
    for info in rooms:
        print_info += str(info) + "\n"

    query_label = Label(root, text=print_info)
    query_label.grid(row=0, column=0, columnspan=1)


submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=6, column=0, columnspan=1, ipady=5, ipadx=69)


root.mainloop()