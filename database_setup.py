import sqlite3

con = sqlite3.connect("RESERVME.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS UserInformation(userID INTEGER PRIMARY KEY, room_type TEXT, full_name TEXT, address TEXT, email TEXT, zipcode INT, state TEXT, phoneNumber INT)"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS RoomsAvailability(roomID INTEGER PRIMARY KEY, availability TEXT DEFAULT 'Available', room_type TEXT, price REAL, size INT, guest TEXT)"
)

# cur.execute(
#     """INSERT INTO RoomsAvailability(room_type, price) VALUES
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("Studio Suite", 149),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("One-Bedroom Suite", 99),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Two-Bedroom Suite", 154),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Presidential Suite", 259),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324),
#     ("Premium Suite", 324)
#     """
# )
# con.commit()

# cur.execute(
#     "CREATE TABLE IF NOT EXISTS Rooms(room_type TEXT, capacity INT, price REAL)"
# )

# cur.execute(
#     """INSERT INTO Rooms VALUES
#     ("Studio Suite", 2, 149),
#     ("One-Bedroom Suite", 2, 99),
#     ("Two-Bedroom Suite", 4, 154),
#     ("Presidential Suite", 5, 259),
#     ("Premium Suite", 7, 324)
#     """
# )

# cur.execute("SELECT * FROM UserInformation")
# print(cur.fetchall())

# cur.execute(
#     "CREATE TABLE IF NOT EXISTS GuestPayment(card_carrier TEXT, card_number INT, card_csv INT, card_expiration TEXT, cardholder TEXT)"
# )

# cur.execute("SELECT * FROM GuestPayment")
# print(cur.fetchall())




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
