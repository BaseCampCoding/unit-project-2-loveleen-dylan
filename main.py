import time
import sqlite3

def input_number_check(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isdigit():
            response = int(response)
            if response >= 0:
                return response
        print("Please provide a valid input.")


print(
    """              . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|:::|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
            RESERVEME                |=    :    =|                      
_____________________________________L___________J________________________
--------------------------------------------------------------------------"""
)
time.sleep(1)
print(
    """
WELCOME TO ReservME WHERE YOU RESERVE FOR A ME! 

We are delighted to have you here with us today.

Let's get started!
"""
)
time.sleep(2)
print("We have 5 types of rooms.")
print("\n" + "\033[1m" + "Studio Suite: ")
print(
    "\033[0m"
    + "Featuring a plush bed and living space with extra seating, a sleeper sofa, and a TV that can be seen from every angle of the suite. Each studio suite includes a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$99")
print("\n\n" + "\033[1m" + "One-Bedroom Suite: ")
print(
    "\033[0m"
    + "Including a separate living room with sleeper sofa and a bedroom with a TV in both spaces. Each one-bedroom suite features a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$149")
print("\n\n" + "\033[1m" + "Two-Bedroom Suite: ")
print(
    "\033[0m"
    + "Spread out in the separate living room with sleeper sofa and two bedrooms with a TV in all three spaces. Each two-bedroom suite includes a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$154")
print("\n\n" + "\033[1m" + "Presidential Suite: ")
print(
    "\033[0m"
    + "Experience even more space and comfort in our Presidential Suite. Some hotels’ Presidential Suites feature an espresso machine, fireplace, a luxury bathroom feature like whirlpool tubs, or a conference table with seating for up to eight."
)
print("$259")
print("\n\n" + "\033[1m" + "Premium Suite: ")
print(
    "\033[0m"
    + "Offering the same experience as our popular one-bedroom suites, Premium Suites include additional upgrades of Premium WiFi, a Keurig coffee brewer, plus snacks and drinks which are replenished daily."
)
print("$324")

time.sleep(5)
ROOMS = [
    "studio suite",
    "one-bedroom suite",
    "two-bedroom suite",
    "presidential suite",
    "premium suite",
]

PRICES = [99, 149, 154, 259, 324]

room_type = input("\n" + "What type of room would you like to reserve today?: ")
input_room_type = room_type.lower()
for i in ROOMS:
    if input_room_type not in ROOMS:
        print("That room does not exist. Please try again.")
        room_type = input("\n" + "What type of room would you like to reserve today?: ")

i = ROOMS.index(input_room_type)
price = PRICES[i]

import sqlite3

con = sqlite3.connect("RESERVME.db")

cur = con.cursor()

print("Great. Before you can reserve a hotel room we need some information.")
full_name = input("What is your name?: ")
number_guests = input_number_check("How many guests will there be in total?: ")
phone_number = input_number_check("What is your phone number?: ")
address = input("What is your address?: ")
zip_code = input_number_check("What is your zipcode?: ")
state = input("What state are you from?: ")
email = input("What is your email address?: ")

cur.execute(
    "INSERT INTO UserInformation(full_name, address, email, zipcode, state, phoneNumber) VALUES(?,?,?,?,?,?)",
    (full_name, address, email, zip_code, state, phone_number),
)
cur.execute("SELECT * FROM UserInformation")

cur.execute(
    "INSERT INTO RoomsAvailability(room_type, price, size, guest) VALUES (?, ?, ?, ?)", (input_room_type, price, number_guests, full_name)
)
