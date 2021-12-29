from data import MENU, resources, unit


def insert_coins(drink, cost):
    changes = 0
    money_enough = True
    print("Please inset coins.")
    qua = int(input("How many quarters (0.25)?"))
    dim = int(input("How many dimes (0.10)?"))
    nic = int(input("How many nickles (0.05)?"))
    pen = int(input("How many pennies (0.01)?"))
    inserted = 0.25 * qua + 0.10 * dim + 0.05 * nic + 0.01 * pen
    changes = inserted - cost
    if changes < 0:
        money_enough = False
        print("Sorry not enough money, money refunded")
    else:
        if changes > 0:
            print(f"Here is your {round(changes,2)} changes.")
        print(f"Here is your {drink}")
    return money_enough


def check_resource(resources, used_materials):
    #saved_resources = resources
    resource_enough = True
    for liter in resources.keys():
        if used_materials.get(liter):
            remaining = resources[liter] - used_materials[liter]
            if remaining < 0:
                print(f"Sorry, there is not enough {liter}.")
                #resources = saved_resources
                resource_enough = False
            else:
                resources[liter] = remaining
    return resources, resource_enough


def report(resources, unit):
    for resource in resources.keys():
        print(f"{resource.title()}: {resources[resource]}{unit[resource]}")

def coffee_machine(resources):
    earned = 0
    option = input("What would you like? Espresso/Cappuccino/Latte")
    option_list = ["Espresso", "Cappuccino", "Latte", "report", "off"]

    while option != 'off':
        if option != 'report':
            saved_resources = resources
            materials = MENU[option]["ingredients"]
            resources, resource_enough = check_resource(resources, materials)
            if resource_enough == True:
                cost = MENU[option]["cost"]
                money_enough = insert_coins(option, cost)
            if resource_enough == False or money_enough == False:
                resources = saved_resources
            else:
                earned += cost
            print(resources)
            print(resource_enough)
            print(money_enough)
        else:
            report(resources, unit)
            print(f"Money: ${earned}")
        option = input("What would you like? Espresso/Cappuccino/Latte")


coffee_machine(resources)




