import re
from bank import models

def print_err(errors):
    for error in errors:
        print(f'\033[1;31m{error}\033[0m')

def print_success(msg : str):
    print(f'\033[1;33m{msg}\033[0m')

def create_customer_menu(bank: models.Bank):
    name = input('Enter Customer Name: ').strip()
    phone = input('Enter Phone Number: ').strip()
    email = input('Enter Email: ').strip()

    errors = []

    if not re.search(r'^[a-zA-Z\s]{2,}$', name):
        errors.append('❌ Please Enter Valid Name!')
    
    if not re.search(r'^[6-9]\d{9}$', phone):
        errors.append('❌ Please Enter Valid Phone Number!')
    
    if not re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        errors.append('❌ Please Enter Valid Email!')

    if errors:
        print_err(errors)
        return create_customer_menu()
    
    # Creating an new object for entering the new user data
    bank.create_customer(name, phone, email)
    print_success("✅ Customer Id Created Successfully!")
    
def create_account_menu(bank: models.Bank):
    print('Select Account Type: ')
    print('1. Saving Account ( Minimum Balance: ₹1000 )')
    print('2. Current Account ( Overdraft Allowed )')
    choice = int(input('Enter Choice: '))
    initial_amount = float(input('Enter Initiale Deposit Amout: ₹'))
    errors = list()
    if choice == 1 and initial_amount < 1000:
        errors.append('❌ In Savings Account minimum balance should be ₹1000 !')
    
    new_created_account = bank.create_account(choice, initial_amount)

    if not new_created_account:
        errors.append('❌ Please Enter Valid Account Type')
    
    if errors:
        print_err(errors)
        return create_account_menu(bank)
    else:
        print_success('✅ Customer Bank Account Created Successfully!')
        

def deposit_menu(bank: models.Bank):
    pass
def withdraw_menu(bank: models.Bank):
    pass
def transfer_menu(bank: models.Bank):
    pass
def show_account_details(bank: models.Bank):
    pass
def show_transaction_history(bank: models.Bank):
    pass
def add_interest_menu(bank: models.Bank):
    pass
def list_all_customers_menu(bank: models.Bank):
    pass
def bye():
    pass

def display_menu():
    """A Function that descirbe the controlers or or ask your choice."""
    commands = {
        1: create_customer_menu,
        2: create_account_menu,
        3: deposit_menu,
        4: withdraw_menu,
        5: transfer_menu,
        6: show_account_details,
        7: show_transaction_history,
        8: add_interest_menu,
        9: list_all_customers_menu,
        0: bye,
        10: display_menu
    }
    print('=' *  80)
    print(' ' * 30, 'LIVEBANK - A Banking System')
    print('=' * 80)
    print()
    print('Welcome to LIVEBANK')
    print()
    for command, func in commands.items():
        print(str(command) + '.', func.__name__.replace('_', ' ').title())
    print()
    print('-' * 80)
    return commands

def handel_choice(commands, choice, bank: models.Bank):
    commands[choice](bank)

def main():
    """Main programm Loop here."""
    bank = models.Bank('lochan')
    # Commands that we can use in it
    commands = display_menu()
    while True:
        try:
            choice = int(input('\033[1;32mEnter Your Choice: \033[0m'))
        except ValueError:
            print_err(['Enter a Valid Command'])
            continue
        else:
            handel_choice(commands, choice, bank)


if __name__ == "__main__":
    main()