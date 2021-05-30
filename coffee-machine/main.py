from data import MENU, resources, coffee_emoji, logo

machine_on = True
money = 0.0


def print_report():
    """Prints the value of the remaining resources and the money in the machine"""
    for resource_key in resources:
        print(f'{resource_key}: {resources[resource_key]}')
    global money
    print(f'money: {format_to_currency(money)}')


def print_menu():
    """Prints the menu out"""
    print('--Menu-- ')
    for resource_key in MENU:
        print(f'{resource_key}: {format_to_currency(MENU[resource_key]["cost"])}')


def is_valid_order(order_input):
    """Checks if the order input is valid"""
    return order_input in MENU


def is_valid_admin_command(admin_input):
    """Checks if the input is a valid admin command"""
    return admin_input == 'report' or admin_input == 'off' or admin_input == 'menu'


def format_to_currency(number):
    """Formats a float to a dollar currency string"""
    return f'${"{:.2f}".format(number)}'


def check_has_resources(resource_type):
    """Checks if the machine has enough resources to make a certain drink type"""
    required_resources = MENU[resource_type]['ingredients']

    for resource_key in required_resources:
        if required_resources[resource_key] > resources[resource_key]:
            print("The machine does not have the resources necessary to make this item.")
            return False
    return True


def get_inserted_money():
    """Prompts the user to input the coins, and gets the total inserted value"""
    pennies = float(input("How many pennies? "))
    nickles = float(input("How many nickles? "))
    dimes = float(input("How many dimes? "))
    quarters = float(input("How many quarters? "))

    total_inserted = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
    return total_inserted


def check_cost(coffee_order, money_inserted):
    """Checks if the money inserted in the machine is enough to order the drink"""
    cost_to_buy = MENU[coffee_order]['cost']

    if money_inserted < cost_to_buy:
        return False
    return True


def get_change(resource, money_paid):
    """Gets the change required based on the drink purchased and the money paid"""
    cost_of_resource = MENU[resource]['cost']

    return money_paid - cost_of_resource


def deduct_resources(resource_type):
    """Removes the resources from the machine to make the coffee"""
    required_resources = MENU[resource_type]['ingredients']
    for resource_key in required_resources:
        resources[resource_key] -= required_resources[resource_key]


def order():
    """Main order flow of the program"""
    coffee_ordered = input("What would you like to order? ")
    if is_valid_order(coffee_ordered):
        if check_has_resources(coffee_ordered):
            print("Machine has required resources")
            money_inserted = get_inserted_money()
            if check_cost(coffee_ordered, money_inserted):
                global money
                deduct_resources(coffee_ordered)
                change = get_change(coffee_ordered, money_inserted)
                money += money_inserted - change
                print(f'Change: {format_to_currency(change)}')
                print(f"Here is your {coffee_emoji} {coffee_ordered}")
            else:
                print(f"Not enough, refunded {format_to_currency(money_inserted)}")

    elif is_valid_admin_command(coffee_ordered):
        if coffee_ordered == 'off':
            global machine_on
            machine_on = False
        elif coffee_ordered == 'report':
            print_report()
        elif coffee_ordered == 'menu':
            print_menu()
    else:
        print("Wrong order type. Use espresso, cappuccino or latte")


if __name__ == '__main__':
    print(logo)
    print_menu()
    while machine_on:
        order()
