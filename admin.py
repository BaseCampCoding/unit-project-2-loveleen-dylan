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
            "INSERT INTO UserInformation(room_type, full_name, address,email,zipcode,state,phoneNumber) VALUES(:room_type, :f_name, :address, :email, :zipcode, :state, :phoneNumber)",
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

    # Function to show userinfo data
    def records():
        root = Tk()
        root.title("DataBase")
        root.geometry("807x400")
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Select data
        c.execute("SELECT * FROM UserInformation")
        records = c.fetchall()
        columns = (
            "ID",
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

        # Commit changes
        con.commit()

        # Close Connection
        con.close()

    # Function to delete userinfo data
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

    # Function to save the userinfo updated data
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
        userID_editor = Entry(editor, width=30)
        userID_editor.grid(row=0, column=1)
        room_type_editor = Entry(editor, width=30)
        room_type_editor.grid(row=1, column=1)
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=2, column=1)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=3, column=1)
        email_editor = Entry(editor, width=30)
        email_editor.grid(row=4, column=1)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=6, column=1)
        phoneNumber_editor = Entry(editor, width=30)
        phoneNumber_editor.grid(row=7, column=1)

        # Create Text Box Labels
        userID_label = Label(editor, text="User ID")
        userID_label.grid(row=0, column=0)
        room_type_label = Label(editor, text="Room Type")
        room_type_label.grid(row=1, column=0)
        f_name_label = Label(editor, text="Full Name")
        f_name_label.grid(row=2, column=0)
        address_label = Label(editor, text="Address")
        address_label.grid(row=3, column=0)
        email_label = Label(editor, text="Email")
        email_label.grid(row=4, column=0)
        zipcode_label = Label(editor, text="Zipcode")
        zipcode_label.grid(row=5, column=0)
        state_label = Label(editor, text="State")
        state_label.grid(row=6, column=0)
        phoneNumber_label = Label(editor, text="Phone Number")
        phoneNumber_label.grid(row=7, column=0)

        edit_record = Button(editor, text="Save Record", command=save)
        edit_record.grid(row=8, column=1, columnspan=1, ipady=5, ipadx=84)

        c.execute("SELECT * FROM UserInformation WHERE oid=" + record_id)
        records = c.fetchall()
        for record in records:
            userID_editor.insert(0, record[0])
            room_type_editor.insert(0, record[1])
            f_name_editor.insert(0, record[2])
            address_editor.insert(0, record[3])
            email_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])
            state_editor.insert(0, record[6])
            phoneNumber_editor.insert(0, [7])

    # Function to show paymentinfo data
    def paymentRecords():
        root = Tk()
        root.title("PaymentDataBase")
        root.geometry("600x400")
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Select data
        c.execute("SELECT * FROM GuestPayment")
        paymentRecords = c.fetchall()
        columns = (
            "Payment ID",
            "Card Company",
            "Card Number",
            "CSV",
            "Expiration Date",
            "Cardholder",
        )
        tree = ttk.Treeview(root, height=20, columns=columns, show="headings")
        tree.grid(row=0, column=0, sticky="news")

        # Centering the columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)
        # Inserting the data into the columns
        for info in paymentRecords:
            tree.insert("", "end", value=info)

        # Commit changes
        con.commit()

        # Close Connection
        con.close()

    # Function to delete paymentinfo data
    def deletePayment():
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        c.execute("DELETE from GuestPayment WHERE oid= " + card_id.get())

        # Commit changes
        con.commit()

        # Close Connection
        con.close()

    # Function to save the userinfo updated data
    def savePayment():
        # Connect to database
        editor = Tk()
        record_id = card_id.get()
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()
        c.execute(
            """ UPDATE GuestPayment SET
        card_carrier = :carrier,
        card_number = :number,
        card_csv = :csv,
        card_expiration = :expiration,
        cardholder =:cardholder

        WHERE oid = :oid""",
            {
                "carrier": card_carrier_editor.get(),
                "number": card_number_editor.get(),
                "csv": card_csv_editor.get(),
                "expiration": card_expiration_editor.get(),
                "cardholder": cardholder_editor.get(),
                "oid": record_id,
            },
        )
        # Close database
        con.commit()
        con.close()
        editor.destroy()

    def editPayment():
        editor = Tk()
        editor.title("Edit a Payment")

        editor.geometry("400x600")
        global card_carrier_editor
        global card_number_editor
        global card_csv_editor
        global card_expiration_editor
        global cardholder_editor
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()
        global paymentRecord_id
        paymentRecord_id = card_id.get()

        # Create Text Boxes
        card_id_editor = Entry(editor, width=30)
        card_id_editor.grid(row=0, column=1)
        card_carrier_editor = Entry(editor, width=30)
        card_carrier_editor.grid(row=1, column=1)
        card_number_editor = Entry(editor, width=30)
        card_number_editor.grid(row=2, column=1)
        card_csv_editor = Entry(editor, width=30)
        card_csv_editor.grid(row=3, column=1)
        card_expiration_editor = Entry(editor, width=30)
        card_expiration_editor.grid(row=4, column=1)
        cardholder_editor = Entry(editor, width=30)
        cardholder_editor.grid(row=5, column=1)

        # Create Text Box Labels
        card_id_label = Label(editor, text="Payment ID")
        card_id_label.grid(row=0, column=0)
        card_carrier_label = Label(editor, text="Card Carrier")
        card_carrier_label.grid(row=1, column=0)
        card_number_label = Label(editor, text="Card Number")
        card_number_label.grid(row=2, column=0)
        card_csv_label = Label(editor, text="CSV")
        card_csv_label.grid(row=3, column=0)
        card_expiration_label = Label(editor, text="Expiration Date")
        card_expiration_label.grid(row=4, column=0)
        cardholder_label = Label(editor, text="Cardholder Name")
        cardholder_label.grid(row=5, column=0)

        edit_paymentrecord = Button(editor, text="Save", command=savePayment)
        edit_paymentrecord.grid(row=6, column=1, columnspan=1, ipady=5, ipadx=84)

        c.execute("SELECT * FROM GuestPayment WHERE oid=" + paymentRecord_id)
        paymentrecords = c.fetchall()
        for record in paymentrecords:
            card_id_editor.insert(0, record[0])
            card_carrier_editor.insert(0, record[1])
            card_number_editor.insert(0, record[2])
            card_csv_editor.insert(0, record[3])
            card_expiration_editor.insert(0, record[4])
            cardholder_editor.insert(0, record[5])

    def insertPaymenttoDB():
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # Insert into table
        c.execute(
            "INSERT INTO GuestPayment (card_carrier, card_number, card_csv, card_expiration, cardholder) VALUES(:card_carrier, :card_number, :card_csv, :card_expiration, :cardholder)",
            {
                "card_carrier": card_carrier.get(),
                "card_number": card_number.get(),
                "card_csv": card_csv.get(),
                "card_expiration": card_expiration.get(),
                "cardholder": cardholder.get(),
            },
        )
        con.commit()
        # Commit data
        con.commit()
        # Close database
        con.close()
        # Clear Text Boxes
        card_carrier.delete(0, END)
        card_number.delete(0, END)
        card_csv.delete(0, END)
        card_expiration.delete(0, END)
        cardholder.delete(0, END)

    def updatePayment():
        global card_carrier
        global card_number
        global card_csv
        global card_expiration
        global card_id
        global cardholder
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # creating payment gui
        root = Tk()
        root.title("Payment")
        root.geometry("420x220")
        c = con.cursor()

        # Insert into table
        c.execute(
            "INSERT INTO GuestPayment VALUES(:card_carrier, :card_number, :card_csv, :card_expiration, :cardholder)",
            {
                "card_carrier": card_carrier.get(),
                "card_number": card_number.get(),
                "card_csv": card_csv.get(),
                "card_expiration": card_expiration.get(),
                "cardholder": cardholder.get(),
            },
        )  # Commit data
        con.commit()
        # Close database
        con.close()
        # Clear Text Boxes
        card_carrier.delete(0, END)
        card_number.delete(0, END)
        card_csv.delete(0, END)
        card_expiration.delete(0, END)
        cardholder.delete(0, END)

    def payment():
        global card_carrier
        global card_number
        global card_csv
        global card_expiration
        global cardholder
        global card_id
        # Connect to database
        con = sqlite3.connect("RESERVME.db")
        # Cursor
        c = con.cursor()

        # creating payment gui
        root = Tk()
        root.title("Payment")
        root.geometry("400x400")
        # c.execute(
        #     "SELECT price FROM RoomsAvailability WHERE guest = (?)", (f_name.get(),),
        # )
        # total = c.fetchall()
        # columns = ("Price")
        # tree = ttk.Treeview(root, height=20, columns=columns, show="headings")
        # tree.grid(row=0, column=0, sticky="news")
        # for data in total:
        #     tree.insert("", "end", value=info)

        # Payment Textbox
        card_carrier = Entry(root, width=30)
        card_carrier.grid(row=0, column=1)
        card_number = Entry(root, width=30)
        card_number.grid(row=1, column=1)
        card_csv = Entry(root, width=30)
        card_csv.grid(row=2, column=1)
        card_expiration = Entry(root, width=30)
        card_expiration.grid(row=3, column=1)
        cardholder = Entry(root, width=30)
        cardholder.grid(row=4, column=1)
        card_id = Entry(root, width=30)
        card_id.grid(row=6, column=1)

        # Labels for Payment textboxes
        card_carrier_label = Label(root, text="Card Company")
        card_carrier_label.grid(row=0, column=0)
        card_number_label = Label(root, text="Card Number")
        card_number_label.grid(row=1, column=0)
        card_csv_label = Label(root, text="CSV #")
        card_csv_label.grid(row=2, column=0)
        card_expiration_label = Label(root, text="Expiration Date (MM/YY)")
        card_expiration_label.grid(row=3, column=0)
        cardholder_label = Label(root, text="Cardholder Name")
        cardholder_label.grid(row=4, column=0)
        card_id_label = Label(root, text="Card ID")
        card_id_label.grid(row=6, column=0)

        # Payment button
        make_payment_btn = Button(root, text="Make Payment", command=insertPaymenttoDB)
        make_payment_btn.grid(row=5, column=1, columnspan=1, ipady=5, ipadx=77)
        # Show Payment Records Button
        show_payments = Button(root, text="Show Payments", command=paymentRecords)
        show_payments.grid(row=7, column=1, columnspan=1, ipady=5, ipadx=79)
        # Delete Records Button
        delete_payment = Button(root, text="Delete Payment", command=deletePayment)
        delete_payment.grid(row=8, column=1, columnspan=1, ipady=5, ipadx=77)
        # Edit Record Button
        edit_payments = Button(root, text="Edit Payment", command=editPayment)
        edit_payments.grid(row=9, column=1, columnspan=1, ipady=5, ipadx=84)

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

    # Make Payment button
    payment_btn = Button(root, text="Add a Payment", command=payment)
    payment_btn.grid(row=8, column=1, columnspan=1, ipady=5, ipadx=73.6)

    # Show Records Button
    show_records = Button(root, text="Show Records", command=records)
    show_records.grid(row=10, column=1, columnspan=1, ipady=5, ipadx=79)
    # Show Records Button
    show_records = Button(root, text="Show Records", command=records)
    show_records.grid(row=10, column=1, columnspan=1, ipady=5, ipadx=77.7)

    # Edit Record Button
    edit_record = Button(root, text="Edit Record", command=update)
    edit_record.grid(row=11, column=1, columnspan=1, ipady=5, ipadx=84)

    # Show Records Button
    show_records = Button(root, text="Show Records", command=records)
    show_records.grid(row=10, column=1, columnspan=1, ipady=5, ipadx=79)

    # Delete Records Button
    delete_records = Button(root, text="Delete Record", command=delete)
    delete_records.grid(row=13, column=1, columnspan=1, ipady=5, ipadx=77.3)
    delete_records.grid(row=13, column=1, columnspan=1, ipady=5, ipadx=77.3)