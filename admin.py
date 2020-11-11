import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter as tk


def main_control():
    root = Tk()
    root.title("Admin Control")
    root.geometry("500x500")

    # Query function to insert data
    def query():
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Insert into table
        c.execute(
            "INSERT INTO UserInformation VALUES(:room_type, :f_name, :address, :email, :zipcode, :state, :phoneNumber)",
            {
                "room_type": room_type.get(),
                "f_name": f_name.get(),
                "address": address.get(),
                "email": email.get(),
                "zipcode": zipcode.get(),
                "state": state.get(),
                "phoneNumber": phoneNumber.get(),
            },
        )
        con.commit()
        # Commit data
        con.commit()
        # Close database
        con.close()
        # Clear Text Boxes
        room_type.delete(0, END)
        f_name.delete(0, END)
        address.delete(0, END)
        email.delete(0, END)
        zipcode.delete(0, END)
        state.delete(0, END)
        phoneNumber.delete(0, END)

    # Function to show data
    def records():
        root = Tk()
        root.title("DataBase")
        root.geometry("702x400")
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Select data
        c.execute("SELECT * FROM UserInformation")
        records = c.fetchall()
        columns = (
            "Room Type",
            "Name",
            "Address",
            "Email",
            "Zipcode",
            "State",
            "Phonenumber",
        )
        tree = ttk.Treeview(root, height=20, columns=columns, show="headings")
        tree.grid(row=0, column=0, sticky="news")

        # Centering the columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)
        # Inserting the data into the columns
        for info in records:
            tree.insert("", "end", value=info)

        query_label = Label(root, text=print_records)
        query_label.grid(row=9, column=0, columnspan=2)

        # Commit changes
        con.commit()

        # Close Connection
        con.close()

    # Function to delete data
    def delete():
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        c.execute("DELETE from UserInformation WHERE oid= " + delete_box.get())

        # Commit changes
        con.commit()

        # Close Connection
        con.close()

    # Function to save the updated data
    def save():
        # Connect to database
        editor = Tk()
        record_id = delete_box.get()
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()
        c.execute(
            """ UPDATE UserInformation SET
        room_type = :room,
        full_name = :name,
        address = :address,
        email = :email,
        zipcode =:zipcode,
        state = :state,
        phoneNumber = :phonenumber

        WHERE oid = :oid""",
            {
                "room": room_type_editor.get(),
                "name": f_name_editor.get(),
                "address": address_editor.get(),
                "email": email_editor.get(),
                "zipcode": zipcode_editor.get(),
                "state": state_editor.get(),
                "phonenumber": phoneNumber_editor.get(),
                "oid": record_id,
            },
        )
        # Close database
        con.commit()
        con.close()
        editor.destroy()

    # Function to update the data
    def update():
        editor = Tk()
        editor.title("Update A Record")
        editor.geometry("400x600")

        # Create Global Variables
        global room_type_editor
        global f_name_editor
        global address_editor
        global email_editor
        global zipcode_editor
        global state_editor
        global phoneNumber_editor

        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()
        record_id = delete_box.get()
        # Select data

        # Create Text Boxes
        room_type_editor = Entry(editor, width=30)
        room_type_editor.grid(row=0, column=1)
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=1, column=1)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)
        email_editor = Entry(editor, width=30)
        email_editor.grid(row=3, column=1)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=4, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=5, column=1)
        phoneNumber_editor = Entry(editor, width=30)
        phoneNumber_editor.grid(row=6, column=1)

        # Create Text Box Labels
        room_type_label = Label(editor, text="Room Type")
        room_type_label.grid(row=0, column=0)
        f_name_label = Label(editor, text="Full Name")
        f_name_label.grid(row=1, column=0)
        address_label = Label(editor, text="Address")
        address_label.grid(row=2, column=0)
        email_label = Label(editor, text="Email")
        email_label.grid(row=3, column=0)
        zipcode_label = Label(editor, text="Zipcode")
        zipcode_label.grid(row=4, column=0)
        state_label = Label(editor, text="State")
        state_label.grid(row=5, column=0)
        phoneNumber_label = Label(editor, text="Phone Number")
        phoneNumber_label.grid(row=6, column=0)

        edit_record = Button(editor, text="Save Record", command=save)
        edit_record.grid(row=7, column=1, columnspan=1, ipady=5, ipadx=84)

        c.execute("SELECT * FROM UserInformation WHERE oid=" + record_id)
        records = c.fetchall()
        for record in records:
            room_type_editor.insert(0, record[0])
            f_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            email_editor.insert(0, record[3])
            zipcode_editor.insert(0, record[4])
            state_editor.insert(0, record[5])
            phoneNumber_editor.insert(0, [6])

    # Create Text Boxes
    room_type = Entry(root, width=30)
    room_type.grid(row=0, column=1)
    f_name = Entry(root, width=30)
    f_name.grid(row=1, column=1)
    address = Entry(root, width=30)
    address.grid(row=2, column=1)
    email = Entry(root, width=30)
    email.grid(row=3, column=1)
    zipcode = Entry(root, width=30)
    zipcode.grid(row=4, column=1)
    state = Entry(root, width=30)
    state.grid(row=5, column=1)
    phoneNumber = Entry(root, width=30)
    phoneNumber.grid(row=6, column=1)
    delete_box = Entry(root, width=30)
    delete_box.grid(row=9, column=1)

    # Create Text Box Labels
    room_type_label = Label(root, text="Room Type")
    room_type_label.grid(row=0, column=0)
    f_name_label = Label(root, text="Full Name")
    f_name_label.grid(row=1, column=0)
    address_label = Label(root, text="Address")
    address_label.grid(row=2, column=0)
    email_label = Label(root, text="Email")
    email_label.grid(row=3, column=0)
    zipcode_label = Label(root, text="Zipcode")
    zipcode_label.grid(row=4, column=0)
    state_label = Label(root, text="State")
    state_label.grid(row=5, column=0)
    phoneNumber_label = Label(root, text="Phone Number")
    phoneNumber_label.grid(row=6, column=0)
    delete_box_label = Label(root, text="Select ID Number")
    delete_box_label.grid(row=9, column=0)

    # Submit Button
    submit_btn = Button(root, text="Add to Database", command=query)
    submit_btn.grid(row=7, column=1, columnspan=1, ipady=5, ipadx=72.4)
    # Show Records Button
    show_records = Button(root, text="Show Records", command=records)
    show_records.grid(row=8, column=1, columnspan=1, ipady=5, ipadx=79)

    # Delete Records Button
    delete_records = Button(root, text="Delete Record", command=delete)
    delete_records.grid(row=10, column=1, columnspan=1, ipady=5, ipadx=77)
    # Edit Record Button
    edit_record = Button(root, text="Edit Record", command=update)
    edit_record.grid(row=11, column=1, columnspan=1, ipady=5, ipadx=84)
