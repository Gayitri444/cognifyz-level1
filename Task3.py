import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
        return True
    else:
        return False

user_email = input("Please enter an email address")
if validate_email(user_email):

    print("The email address is valid.")
else:
    print("The email address is invalid.")