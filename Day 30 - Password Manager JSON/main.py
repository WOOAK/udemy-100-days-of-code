from tkinter import *
# message box is not a class, * only import classes
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # modify day 5 codes by list comprehension
    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def sav_pw():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website:{
            "email": email,
            "password": password
        }
    }
    if website == "":
        messagebox.showinfo(title="Error", message="Website cannot be blank")
    elif email == "":
        messagebox.showinfo(title="Error", message="Username cannot be blank")
    elif password == "":
        messagebox.showinfo(title="Error", message="Password cannot be blank")
    else:
        is_ok = messagebox.askokcancel(title = website_entry.get(), message = f"These are the details entered: \n"
                                                                              f"Username = {email_entry.get()}\n"
                                                                              f"Password = {password_entry.get()}")
        if is_ok:
            try:
                with open("data.json", mode="r") as datafile:
                    data = json.load(datafile)
            except (FileNotFoundError,json.decoder.JSONDecodeError):
                with open("data.json", mode="w") as datafile:
                    json.dump(new_dict, datafile, indent=4)
            else:
                data.update(new_dict)
                with open("data.json", mode="w") as datafile:
                    json.dump(data, datafile, indent=4)
            finally:
                website_entry.delete(0, "end")
                website_entry.focus()
                email_entry.delete(0, "end")
                email_entry.insert(0, "aykuan1992@gmail.com")
                password_entry.delete(0, "end")
                messagebox.showinfo(title = "Confirmation", message = "Your password has been saved successfully!")
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    if website == "":
        messagebox.showinfo(title="Error", message="Website is blank for searching purpose")
    else:
        try:
            with open("data.json", mode="r") as datafile:
                data = json.load(datafile)
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="Error", message="No data file")
        except KeyError:
            messagebox.showinfo(title="Error", message="Website not found in database")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 20, width = 200, height =200)
window.title("Password Guardian")

canvas = Canvas(width = 200, height = 200)
logo =PhotoImage(file = "logo.png")
# tuple cor x and y for center of image
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

# Labels
website_label = Label(text = "Website:", justify = "left")
email_label = Label(text = "Email/Username:", justify = "left")
password_label = Label(text = "Password:", justify = "left")

website_label.grid(row = 1, column = 0)
email_label.grid(row = 2, column = 0)
password_label.grid(row = 3, column = 0)

# Entries

website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1, sticky = "EW")
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, sticky = "EW")
email_entry.insert(0, "aykuan1992@gmail.com")
password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1, sticky = "EW")

#Buttons

gen_pw_button = Button(text = "Gen Password", command = gen_pw)
gen_pw_button.grid(row = 3, column = 2)
add_pw_button = Button(text = "Save Password", width = 36, command = sav_pw)
add_pw_button.grid(row = 4, column = 1, columnspan = 2, sticky = "EW")
search_button = Button(text = "Search", command = search)
search_button.grid(row = 1, column = 2, sticky = "EW")

window.mainloop()