R  number_guests = input_number_check("How many guests will there be in total?: ")
        guests = []
        for i in range(len(number_guests)):
            name_of_guest = input("Enter Guest Name: ")
            guests.append(name_of_guest)
    phone_number = input_number_check("What is your phone number?: ")
    address = input("What is your address?: ")
    zip_code = input_number_check("What is your zipcode?: ")
    state = input("What state are you from?: ")
    email = input("What is your email address?: ")
