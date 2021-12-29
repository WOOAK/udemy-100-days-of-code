#Calculator
from art import logo
from replit import clear
def add(n1,n2):
    return n1 + n2
def minus(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    while n2 == 0:
        print("Cannot divide by 0")
        n2 = float(input("Please pick another number")) 
        
    return n1/n2
operations = {
'+':add,
'-':minus,
'*':multiply,
'/':divide
}
def check_operator():
    operator = input("Pick an operation: ") 
    if operator not in operations.keys():
        print("Invalid input, please pick it again.")
        return check_operator()
    else:
        return operator

def calculator():
    print(logo)
    str = ''
    num1 = float(input("The first number: "))
    for symbol in operations:
        str += symbol + ' '
    print(str)
    #operator = input("Pick an operation: ")
    #num2 = int(input("The second number: "))

    #calc_function = operations[operator]
    #answer = calc_function(num1,num2)
    #print(f"{num1} {operator} {num2} = {answer}")

    is_end = False
    #option = input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit: ")
    #if option == 'n':
    #    is_end = True
    while not is_end:
        operator = check_operator()
        #operator = input("Pick an operation: ")
        num2 = float(input("The next number: "))
        calc_function = operations[operator]
        answer = calc_function(num1,num2)
        print(num2)
        print(f"{num1} {operator} {num2} = {answer}")
        #num1 = answer
        option = input(f"Type 'y' to continue calculating with {answer},or type 'n' to exit: ")
        if option == 'n':
            is_end = True
            clear()
            calculator()
        else:
            num1 = answer

calculator()


