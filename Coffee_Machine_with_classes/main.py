from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    answer = input(f"What yould you like: {menu.get_items()}? ")

    if answer == "off":
        exit()
    if answer == "report":
        coffee_maker.report()
        money_machine.report()

    menu_item = menu.find_drink(answer)
    if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
        coffee_maker.make_coffee(menu_item)





