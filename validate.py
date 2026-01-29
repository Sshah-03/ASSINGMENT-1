def validate():
    choice = "WRONG"
    acceptable_range = range(0, 11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please, enter a number from 0 to 10: ")

        if choice.isdigit() == False:
            print("Please enter a digit instead of a string.")
        else:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Number not in range 0 to 10.")

    return int(choice)

print(validate())
