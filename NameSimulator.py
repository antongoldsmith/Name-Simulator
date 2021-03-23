def full_name():
    """ This program will be used to validate that a user enters inputs at least two names when asked to enter their full name."""
    
    full_name = input("Please enter your full name below:\n") # prompts user to enter full name
    parts = full_name.split(' ')
    if len(full_name) <= 0:
        print("You haven’t entered anything. Please enter your full name.") # prints message when nothing is entered
    elif len(full_name) <= 4:
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.") # prints message when character length is 4 or less
    elif len(full_name) > 25:
        print("You have entered more than 25 characters. Please make sure that you have only entered your full name.") # prints message when character length is greater than 25
    elif len(parts) != 2:
        print("Please enter your first name and surname with a space.")
    elif len(full_name) >= 4 and len(full_name) < 25 and len(parts) == 2:
        print("Thank you for entering your name.") # prints message when all parameters are met
    
full_name()
