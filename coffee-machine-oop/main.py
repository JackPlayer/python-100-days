from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    is_on = True

    while is_on:
        order = input(f"What would you like to order? ({menu.get_items()}): ")
        menu_item = menu.find_drink(order)
        if menu_item:
            if coffee_maker.is_resource_sufficient(menu_item):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)
        elif order == "off":
            is_on = False
        elif order == "report":
            coffee_maker.report()
            money_machine.report()


if __name__ == "__main__":
    coffee_machine()
