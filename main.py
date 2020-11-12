import sqlite3
from classes import Rooms
from tkinter import *
from tkinter import ttk
import tkinter as tk
from admin import main_control
from tkinter import messagebox

def reservme():
    # Creating the GUI
    root = Tk()
    root.title(" Rooms")
    root.iconbitmap(
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-bkeqe&psig=AOvVaw2oBqXabpCHoyEx9EyMKvdl&ust=1605115375818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDPvfG--OwCFQAAAAAdAAAAABAh"
    )
    root.geometry("193x87")
    # Creating the textbox and the label on the GUI
    room_label_entry = Entry(root, width=30)
    room_label_entry.grid(row=2, column=0)
    room_label = Label(root, text="Room Type")
    room_label.grid(row=1, column=0)

    ROOMS= ['studio suite', 'one-bedroom suite', 'two-bedroom suite', 'presidential suite', 'premium suite']


    def submit():

        # Creating another window after submitting
        root = Tk()
        room_label_get = room_label_entry.get()
        input_room_type = room_label_get.lower()
        if input_room_type not in ROOMS:
            root.withdraw()
            messagebox.showerror("Error", "The room you are looking for is not available. Please try again.")
        if input_room_type == "studio suite":
            room = "Studio Suite"
        elif input_room_type == "one-bedroom suite":
            room = "One-Bedroom Suite"
        elif input_room_type == "two-bedroom suite":
            room = "Two-Bedroom Suite"
        elif input_room_type == "presidential suite":
            room = "Presidential Suite"
        elif input_room_type == "premium suite":
            room = "Premium Suite"
        root.title(" Available Rooms")
        root.iconbitmap(
            "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngwing.com%2Fen%2Ffree-png-bkeqe&psig=AOvVaw2oBqXabpCHoyEx9EyMKvdl&ust=1605115375818000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDPvfG--OwCFQAAAAAdAAAAABAh"
        )
        root.geometry("400x467")
        # Checking for the input from the textbox
        c.execute(
            "SELECT roomID,availability,room_type,price FROM RoomsAvailability WHERE room_type =(?) AND  availability = 'Available'",
            (room,),
        )
        rooms = c.fetchall()
        # Creating columns for the data
        columns = ("RoomID", "Availability", "Room Type", "Price")
        tree = ttk.Treeview(root, height=20, columns=columns, show="headings")
        tree.grid(row=0, column=0, sticky="news")

        # Centering the columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)
        # Inserting the data into the columns
        for info in rooms:
            tree.insert("", "end", value=info)

        confirm_btn = Button(root, text="Confirm", command=main_control)
        confirm_btn.grid(row=7, column=0, columnspan=1, ipady=5, ipadx=69)

    # # creating payment gui
    # root = Tk()
    # btn = Button(root, text= "Make a Payment", fg= 'blue')
    # btn.grid(row=80, column=100)
    # root.title('Payment')
    # root.geometry("300x200+10+10")

    # Submit button for the input in the text box
    # The button runs the submit function
    submit_btn = Button(root, text="Submit", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=1, ipady=5, ipadx=69)
    # Run the GUI
    root.mainloop()

con = sqlite3.connect("RESERVME.db")
c = con.cursor()


root = Tk()
root.title("ReservME")
root.geometry("2000x2500")
welcome_label = Label(root, text="WELCOME TO ReservME WHERE YOU RESERVE FOR A ME!\n\nWe are delighted to have you here with us today.\n\nLet's get started!")
welcome_label.grid(row=0, column=0)


studio_suite_label = Label(root, text="Studio Suite: ")
studio_suite_label.grid(row=1, column=0)
studio_suite_description_label = Label(root, text=str((Rooms('Studio Suite'))))
studio_suite_description_label.grid(row=2, column=0)

onebedroom_suite_label = Label(root, text="One-Bedroom Suite:  ")
onebedroom_suite_label.grid(row=3, column=0)
onebedroom_suite_description_label = Label(root, text=str((Rooms('One-Bedroom Suite'))))
onebedroom_suite_description_label.grid(row=4, column=0)

twobedroom_suite_label = Label(root, text="Two-Bedroom Suite: ")
twobedroom_suite_label.grid(row=5, column=0)
twobedroom_suite_description_label = Label(root, text=str((Rooms("Two-Bedroom Suite"))))
twobedroom_suite_description_label.grid(row=6, column=0)

presidential_suite_label = Label(root, text="Presidential Suite: ")
presidential_suite_label.grid(row=7, column=0)
presidential_suite_description_label = Label(root, text=str((Rooms("Presidential Suite"))))
presidential_suite_description_label.grid(row=8, column=0)

premium_suite_label = Label(root, text="Premium Suite: ")
premium_suite_label.grid(row=9, column=0)
premium_suite_description_label = Label(root, text=str((Rooms("Premium Suite"))))
premium_suite_description_label.grid(row=10, column=0)

confirmButton = Button(root, text="Confirm", command=reservme)
confirmButton.grid(row=15, column=0, columnspan=1, ipady=5, ipadx=84)

root.mainloop()
