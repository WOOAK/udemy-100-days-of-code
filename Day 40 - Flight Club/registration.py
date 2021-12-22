import requests
SHEET_ENDPOINT= "https://api.sheety.co/8b6c843d0b5584ab3894f9aee99bd4ce/flightDeals/users"

def register(firstName, lastName,Email):
    reg_params = {
    "user":
        {
            "firstName":firstName,
            "lastName":lastName,
            "email":Email
        }
    }
    result = requests.post(url=SHEET_ENDPOINT,json=reg_params)
    print(result.text)


def entry():
    print("Welcome to Junin's Flight Club!\nWe find the best flight deals and email you.\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email_input = input("What is your email?\n")
    email_confirm = input("Type your email again.\n")
    if email_confirm != email_input:
        option = input("Your email is not matched with your input. Please register again or exit.\nPress any key and enter to proceed, key in ""Esc"" to exit")
        if option == "Esc":
            return False
        else:
            return entry()
    else:
        print("You are in the club!")
        register(first_name,last_name,email_input)
        return True



is_success = entry()
