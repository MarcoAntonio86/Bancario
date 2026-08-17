from transactions.deposit import Deposit
from transactions.withdrawal import Withdrawal
from models.individual_customer import IndividualCustomer
from models.checking_account import CheckingAccount
from iterators.account_iterator import AccountIterator
from utils.transaction_log import transaction_log


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
def create_customer(customers):
    cpf = input("Enter CPF (numbers only): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\n@@@ A customer with this CPF already exists! @@@")
        return

    name = input("Enter full name: ")
    birth_date = input("Enter birth date (dd-mm-yyyy): ")
    address = input(
        "Enter address (street, number - neighborhood - city/state): "
    )

    customer = IndividualCustomer(
        address=address,
        cpf=cpf,
        name=name,
        birth_date=birth_date,
    )

    customers.append(customer)

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