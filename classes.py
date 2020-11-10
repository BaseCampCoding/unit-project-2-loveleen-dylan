def input_number_check(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isdigit():
            response = int(response)
            if response >= 0:
                return response
        print("Please provide a valid input.")
        
class Rooms:
    def __init__(self, type, description, price, inquiries):
    self.type = room_type
    self.description = description
    self.price = price

    def inquiries():
    full_name = input("What is your name?: ")
    will_there_be_guests = input("Will there be any other guests?(Y/N): ")
    if will_there_be_guests.lower() == "y":
        number_guests = input_number_check("How many guests will there be in total?: ")
        guests = []
        for i in range(len(number_guests)):
            name_of_guest = input("Enter Guest Name: ")
            guests.append(name_of_guest)
    phone_number = input_number_check("What is your phone number?: ")
    address = input("What is your address?: ")
    zip_code = input_number_check("What is your zipcode?: ")
    state = input("What state are you from?: ")
    email = input("What is your email address?: ")

    