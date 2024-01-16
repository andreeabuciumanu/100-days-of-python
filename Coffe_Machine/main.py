MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def has_resources(drink):
    for item in resources:
        if (item in MENU[drink]['ingredients'] and
                MENU[drink]['ingredients'][item] > resources[item]):
            return False
    return True


def calculate_total(quarters, dimes, nickles, pennies):
    total_amount = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    total_amount = round(total_amount, 2)
    return total_amount


def has_enough_money(total_amount, drink):
    return total_amount >= MENU[drink]['cost']


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f'Money: ${profit}')


def make_coffee():
    global profit

    while True:
        my_drink = input("What would you like? (espresso/latte/cappuccino):  ")

        if my_drink == "report":
            report()
            continue

        if not has_resources(my_drink):
            continue
        else:
            print("Please insert coins")
            q = int(input("how many quarters:  "))
            d = int(input("how many dimes:  "))
            n = int(input("how many nickles:  "))
            p = int(input("how many pennies:  "))
            total_amount = calculate_total(q, d, n, p)

            if not has_enough_money(total_amount, my_drink):
                print(f"Sorry, that's not enough money. Money refunded.")
                continue

            cost = MENU[my_drink]['cost']
            if total_amount > cost:
                change = total_amount - cost
                print(f'Here is ${change} in change')
            print(f'Here is your {my_drink}. Enjoy!')
            profit += cost

            for item in resources:
                if item in MENU[my_drink]['ingredients']:
                    resources[item] -= MENU[my_drink]['ingredients'][item]


make_coffee()
