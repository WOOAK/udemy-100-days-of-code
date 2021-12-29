# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowername1 = name1.lower()
lowername2 = name2.lower()
count_T = lowername1.count('t') + lowername2.count('t')
count_R = lowername1.count('r') + lowername2.count('r')
count_U = lowername1.count('u') + lowername2.count('u')
count_E = lowername1.count('e') + lowername2.count('e')

digit1 = count_T + count_R + count_U + count_E
count_L = lowername1.count('l') + lowername2.count('l')
count_O = lowername1.count('o') + lowername2.count('o')
count_V = lowername1.count('v') + lowername2.count('v')
count_E = lowername1.count('e') + lowername2.count('e')
digit2  = count_L + count_O + count_V + count_E
percent = str(digit1) + str(digit2)
percent_num = int(percent)

if percent_num < 10 or percent_num > 90:
  print(f"Your score is {percent_num}, you go together like coke and mentos.")
elif percent_num >=40 and percent_num <=50:
    print(f"Your score is {percent_num}, you are alright together.")
else:
  print(f"Your score is {percent_num}.")