import sqlite3
from tkinter import *


def main_control():
    root = Tk()
    root.title("Admin Control")
    root.geometry("400x167")

    # Query function to insert data
    def query():
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Insert into table
        c.execute(
            "INSERT INTO UserInformation VALUES(:f_name, :address, :email, :zipcode, :state, :phoneNumber)",
            {
                "f_name": f_name.get(),
                "address": address.get(),
                "email": email.get(),
                "zipcode": zipcode.get(),
                "state": state.get(),
                "phoneNumber": phoneNumber.get(),
            },
        )

        c.execute("INSERT INTO RoomsAvailability(guest) VALUES(?)", (f_name.get(),))

        # Commit data
        con.commit()
        # Close database
        con.close()
        # Clear Text Boxes
        f_name.delete(0, END)
        address.delete(0, END)
        email.delete(0, END)
        zipcode.delete(0, END)
        state.delete(0, END)
        phoneNumber.delete(0, END)

    # Create Text Boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1)
    address = Entry(root, width=30)
    address.grid(row=1, column=1)
    email = Entry(root, width=30)
    email.grid(row=2, column=1)
    zipcode = Entry(root, width=30)
    zipcode.grid(row=3, column=1)
    state = Entry(root, width=30)
    state.grid(row=4, column=1)
    phoneNumber = Entry(root, width=30)
    phoneNumber.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label = Label(root, text="Full Name")
    f_name_label.grid(row=0, column=0)
    address_label = Label(root, text="Address")
    address_label.grid(row=1, column=0)
    email_label = Label(root, text="Email")
    email_label.grid(row=2, column=0)
    zipcode_label = Label(root, text="Zipcode")
    zipcode_label.grid(row=3, column=0)
    state_label = Label(root, text="State")
    state_label.grid(row=4, column=0)
    phoneNumber_label = Label(root, text="Phone Number")
    phoneNumber_label.grid(row=5, column=0)

    submit_btn = Button(root, text="Add to Database", command=query)
    submit_btn.grid(row=6, column=1, columnspan=1, ipady=5, ipadx=69)
