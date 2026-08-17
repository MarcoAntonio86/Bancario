from utils.menu import menu
from services.banking_service import (
    create_account,
    create_customer,
    deposit,
    list_accounts,
    show_statement,
    withdraw,
)

def main():
    customers = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            deposit(customers)

        elif option == "w":
            withdraw(customers)

        elif option == "s":
            show_statement(customers)

        elif option == "nc":
            create_customer(customers)

        elif option == "na":
            account_number = len(accounts) + 1
            create_account(account_number, customers, accounts)

        elif option == "la":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("\n@@@ Invalid option! Please select a valid operation. @@@")