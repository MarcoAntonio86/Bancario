from unicodedata import name

from transactions.deposit import Deposit
from transactions.withdrawal import Withdrawal

from models.individual_customer import IndividualCustomer
from models.corporate_customer import CorporateCustomer
from models.checking_account import CheckingAccount

from iterators.account_iterator import AccountIterator

from utils.transaction_log import transaction_log

from datetime import datetime

from database.customer_repository import (
    find_individual_customer_by_cpf,
    insert_individual_customer,
    find_corporate_customer_by_cnpj,
    insert_corporate_customer,
)

from database.customer_repository import (
    find_individual_customer_by_cpf,
    insert_individual_customer,
    find_corporate_customer_by_cnpj,
    insert_corporate_customer,
    list_individual_customers,
    list_corporate_customers,
)

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


@transaction_log
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


@transaction_log
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


@transaction_log
def create_individual_customer(customers):
    cpf = input("Enter CPF (numbers only): ")

    if len(cpf) != 11 or not cpf.isdigit():
        print("\n@@@ Invalid CPF! Enter exactly 11 digits. @@@")
        return

    
    customer = filter_customer(cpf, customers)
    customer_db = find_individual_customer_by_cpf(cpf)

    if customer or customer_db:
        print("\n@@@ A customer with this CPF already exists! @@@")
        return


    name = input("Enter full name: ").strip()

    if not name:
        print("\n@@@ Name cannot be empty! @@@")
        return
    
    birth_date_input = input("Enter birth date (dd-mm-yyyy): ")

    try:
        birth_date = datetime.strptime(
            birth_date_input,
            "%d-%m-%Y",
        )
    except ValueError:
        print("\n@@@ Invalid birth date! Use the format dd-mm-yyyy. @@@")
        return

    address = input(
    "Enter address (street, number - neighborhood - city/state): "
).strip()

    if not address:
        print("\n@@@ Address cannot be empty! @@@")
        return

    customer = IndividualCustomer(
        address=address,
        cpf=cpf,
        name=name,
        birth_date=birth_date,
    )

    customers.append(customer)

    insert_individual_customer(customer)

    print("\n=== Customer created successfully! ===")
    

@transaction_log
def create_account(account_number, customers, accounts):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! Account creation canceled. @@@")
        return

    account = CheckingAccount.new_account(customer, account_number)

    accounts.append(account)
    customer.add_account(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    for account in AccountIterator(accounts):
        print("=" * 50)
        print(f"Branch: {account['branch']}")
        print(f"Account number: {account['number']}")
        print(f"Customer: {account['customer']}")
        print(f"Balance: ${account['balance']:.2f}")


@transaction_log
def show_statement(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\n@@@ Customer not found! @@@")
        return

    account = recover_customer_account(customer)

    if not account:
        return

    print("\n================ STATEMENT ================")

    has_transactions = False

    for transaction in account.history.generate_report():
        has_transactions = True

        print(
            f"\n{transaction['type']}:"
            f"\n\tAmount: ${transaction['amount']:.2f}"
            f"\n\tDate: {transaction['date']}"
        )

    if not has_transactions:
        print("No transactions were made.")

    print(f"\nBalance: ${account.balance:.2f}")
    print("===========================================")

def create_customer(customers):
    customer_type = input(
        "\n[1] Individual customer"
        "\n[2] Corporate customer"
        "\n=> "
    )

    if customer_type == "1":
        create_individual_customer(customers)

    elif customer_type == "2":
        create_corporate_customer(customers)

    else:
        print("\n@@@ Invalid customer type! @@@")

@transaction_log
def create_corporate_customer(customers):
    cnpj = input("Enter CNPJ (numbers only): ")

    if len(cnpj) != 14 or not cnpj.isdigit():
        print("\n@@@ Invalid CNPJ! Enter exactly 14 digits. @@@")
        return

    customer_db = find_corporate_customer_by_cnpj(cnpj)

    if customer_db:
        print("\n@@@ A customer with this CNPJ already exists! @@@")
        return

    company_name = input("Enter company name: ").strip()

    if not company_name:
        print("\n@@@ Company name cannot be empty! @@@")
        return

    address = input(
        "Enter address (street, number - neighborhood - city/state): "
    )

    customer = CorporateCustomer(
        address=address,
        cnpj=cnpj,
        company_name=company_name,
    )

    customers.append(customer)

    insert_corporate_customer(customer)

    print("\n=== Corporate customer created successfully! ===")

def list_customers():
    individual_customers = list_individual_customers()
    corporate_customers = list_corporate_customers()

    print("\n=== Individual Customers ===")

    for customer in individual_customers:
        print(f"ID: {customer[0]}")
        print(f"Name: {customer[1]}")
        print(f"CPF: {customer[2]}")
        print(f"Birth date: {customer[3]}")
        print(f"Address: {customer[4]}")
        print("-" * 40)

    print("\n=== Corporate Customers ===")

    for customer in corporate_customers:
        print(f"ID: {customer[0]}")
        print(f"Company name: {customer[1]}")
        print(f"CNPJ: {customer[2]}")
        print(f"Address: {customer[3]}")
        print("-" * 40)