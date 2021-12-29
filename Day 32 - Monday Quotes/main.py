import smtplib
#
my_email = "killer_1021@hotmail.com"
# your_email = "aykuan1992@gmail.com"
your_email = "aykuan.woo@silverlakeaxis.com"
# SUBJECT = "Python testing"
# TEXT = "Hi my name is Ay Kuan"
#
# # Solve BCC issue
# message = "From: %s\r\n" % my_email + "To: %s\r\n" % your_email + "Subject: %s\r\n" % SUBJECT + "\r\n" + TEXT
# # Cant solve BCC issue. Found on internet
# # message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# # Cant solve BCC issue. Angela code
# # message = "Subject: Hello\n\nBody of email. Bye"
password = "kuan1120//"
connection = smtplib.SMTP("smtp.live.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=your_email, msg=message)
# connection.close()

import datetime as dt
from random import choice
# # current date time
# now = dt.datetime.now()
# year = now.year
# print(year)
# # which day in a week
# # start from index 0, Monday
# day_in_week = now.weekday()
# print(day_in_week)
# DOB = dt.datetime(year=1992, month=11, day=20, hour=9, minute=39)
# print(DOB)
SUBJECT = "There are some pieces of words which might inspire you.."

with open("quotes.txt") as file:
    content = file.read()
    quotes_list = content.splitlines()

selected_quote = choice(quotes_list)
TEXT = selected_quote
message = "From: %s\r\n" % my_email + "To: %s\r\n" % your_email + "Subject: %s\r\n" % SUBJECT + "\r\n" + TEXT

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 1:
    connection.sendmail(from_addr=my_email, to_addrs=your_email, msg=message)
    connection.close()