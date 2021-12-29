# Write your code below this line 👇
def prime_checker(number):
    # initialise
    number1 = 2
    rem = 1
    while number > number1 and rem != 0:
        rem = number % number1
        number1 += 1

    if rem == 0 or number == 1:
        print("It's not a prime number.")
    else:
        print("It's a prime mumber.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



