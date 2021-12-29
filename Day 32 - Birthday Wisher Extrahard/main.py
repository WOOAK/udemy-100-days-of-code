##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random


LETTER_TEMPLATE = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
TEMPLATE_REPLACE = "[NAME]"
MY_EMAIL = "aykuan1992@gmail.com"
MY_PASSWORD = "eT9f!8J*ks7Go*4"
SUBJECT = "Big Day! (Python testing purpose)"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day

data = data[data["month"] == current_month]
data = data[data["day"] == current_day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for (index, row) in data.iterrows():
    template = random.choice(LETTER_TEMPLATE)
    with open(f"letter_templates/{template}") as template_text:
        content = template_text.read()
# 4. Send the letter generated in step 3 to that person's email address.
        body = content.replace(TEMPLATE_REPLACE, row["name"])
        message = "From: %s\r\n" % MY_EMAIL + "To: %s\r\n" % row["email"] + "Subject: %s\r\n" % SUBJECT + "\r\n" + body
        connection.sendmail(from_addr=MY_EMAIL, to_addrs= row["email"], msg=message)
connection.close()






