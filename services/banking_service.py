from transactions.deposit import Deposit
from transactions.withdrawal import Withdrawal


def filter_customer(cpf, customers):
    filtered_customers = [
        customer
        for customer in customers
        if customer.cpf == cpf
    ]

    return filtered_customers[0] if filtered_customers else None

def recover_customer_account(customer):
    if not customer.accounts:
        print("\n@@@ Customer does not have an account! @@@")
        return None

    # FIXME: currently does not allow the customer to choose an account
    return customer.accounts[0]

def deposit(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    amount = float(input("Enter the deposit amount: "))
    transaction = Deposit(amount)

    account = recover_customer_account(customer)

    if not account:
        return

    customer.perform_transaction(account, transaction)


def withdraw(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    amount = float(input("Enter the withdrawal amount: "))
    transaction = Withdrawal(amount)

    account = recover_customer_account(customer)

    if not account:
        return

    customer.perform_transaction(account, transaction)