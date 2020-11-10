import sqlite3
from classes import Rooms

print(
    """
    
                                RESERVEME
                  . .                     -:-             .  .  .
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
                                     |=    :    =|                      
_____________________________________L___________J________________________
--------------------------------------------------------------------------


"""
)

print(
    """
WELCOME TO ReservME WHERE YOU RESERVE FOR A ME! 

We are delighted to have you here with us today.

Let's get started!
"""
)
print("We have 5 types of rooms.")
print("\n" + "\033[1m" + "Studio Suite: ")

# "\033[0m"
print("\033[0m" + str((Rooms("Studio Suite"))))

print("\n" + "\033[1m" + "One-Bedroom Suite: ")
print("\033[0m" + str((Rooms("One-Bedroom Suite"))))

print("\n\n" + "\033[1m" + "Two-Bedroom Suite: ")
print("\033[0m" + str((Rooms("Two-Bedroom Suite"))))

print("\n\n" + "\033[1m" + "Presidential Suite: ")
print("\033[0m" + str((Rooms("Presidential Suite"))))

print("\n\n" + "\033[1m" + "Premium Suite: ")
print("\033[0m" + str((Rooms("Premium Suite"))))

# input_room_type = room_type.lower()
# for i in ROOMS:
#     if input_room_type not in ROOMS:
#         print("That room does not exist. Please try again.")
#         room_type = input("\n" + "What type of room would you like to reserve today?: ")

# print("Great. Before you can reserve a hotel room we need some information.")

# con.commit()
# con.close()