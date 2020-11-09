import sqlite3

con = sqlite3.connect("Customer_Info.db")
cur = con.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS UserInformation(full_name TEXT, address TEXT, email TEXT, zipcode INT, state TEXT, phoneNumber INT"
)
