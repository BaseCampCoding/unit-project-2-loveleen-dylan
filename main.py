import sqlite3
from tkinter import *
from PIL import Image, ImageTk


con = sqlite3.connect("RESERVME.db")
c = con.cursor()

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


def submit():
    root = Tk()
    room_label_get = room_label_entry.get()
    root.title(" Available Rooms")
    root.iconbitmap(
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-bkeqe&psig=AOvVaw2oBqXabpCHoyEx9EyMKvdl&ust=1605115375818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDPvfG--OwCFQAAAAAdAAAAABAh"
    )
    root.geometry("300x300")
    c.execute(
        "SELECT roomID,availability,room_type,price FROM RoomsAvailability WHERE room_type =(?) AND  availability = 'Available'",
        (room_label_get,),
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
