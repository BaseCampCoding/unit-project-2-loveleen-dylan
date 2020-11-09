import sqlite3

con = sqlite3.connect("RESERVEME.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS UserInformation(full_name TEXT, address TEXT, email TEXT, zipcode INT, state TEXT, phoneNumber INT)"
)

cur.execute("CREATE TABLE IF NOT EXISTS RoomsAvailability(roomID AUTO_INCREMENT, availability TEXT, room_type TEXT, price REAL, size INT, guest TEXT)"
)
