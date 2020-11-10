import sqlite3

con = sqlite3.connect("RESERVME.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS UserInformation(full_name TEXT, address TEXT, email TEXT, zipcode INT, state TEXT, phoneNumber INT)"
)

cur.execute("CREATE TABLE IF NOT EXISTS RoomsAvailability(roomID AUTO_INCREMENT, availability TEXT, room_type TEXT, price REAL, size INT, guest TEXT)"
)

# cur.execute("""INSERT INTO RoomsAvailability(room_type, price) VALUES
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
#     """)
# con.commit()
# cur.execute("SELECT * FROM RoomsAvailability")
# print(cur.fetchall())

cur.execute("CREATE TABLE IF NOT EXISTS Rooms(room_type TEXT, capacity INT, price REAL)")

# cur.execute("""INSERT INTO Rooms VALUES 
#     ("Studio Suite", 2, 149),
#     ("One-Bedroom Suite", 2, 99),
#     ("Two-Bedroom Suite", 4, 154),
#     ("Presidential Suite", 5, 259),
#     ("Premium Suite", 7, 324)
#     """)

# cur.execute("SELECT * FROM Rooms")
# print(cur.fetchall())

