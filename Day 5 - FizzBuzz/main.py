#Write your code below this row 👇

Fizzbuzz = "FizzBuzz"
Fizz = "Fizz"
Buzz = "Buzz"
for number in range(1,101):
  rem3 = number % 3
  rem5 = number % 5
  if rem3 == 0 and rem5 == 0:
    print(Fizzbuzz)
  elif rem3 == 0:
    print(Fizz)
  elif rem5 == 0:
    print(Buzz)
  else:
    print(number)
