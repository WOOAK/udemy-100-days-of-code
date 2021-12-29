# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rem4 = year % 4
rem100 = year % 100
rem400 = year % 400

if rem4 == 0:
  if rem100 == 0:
    if rem400 == 0:
      print('Leap year')
    else:
      print('Not Leap year')
  else:
    print('Leap year')
else:
  print('Not leap year')




