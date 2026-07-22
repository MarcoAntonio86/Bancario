
from models.history import TransactionHistory


class Account:
    def __init__(self, number, customer):
        self._balance = 0
        self._number = number
        self._branch = "0001"
        self._customer = customer
        self._history = TransactionHistory()

    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def branch(self):
        return self._branch

    @property
    def customer(self):
        return self._customer

    @property
    def history(self):
        return self._history

    def withdraw(self, amount):
        exceeded_balance = amount > self.balance

        if exceeded_balance:
            print("\n@@@ Operation failed! Insufficient balance. @@@")

        elif amount > 0:
            self._balance -= amount
            print("\n=== Withdrawal completed successfully! ===")
            return True

        else:
            print("\n@@@ Operation failed! Invalid amount. @@@")

        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("\n=== Deposit completed successfully! ===")
            return True

        print("\n@@@ Operation failed! Invalid amount. @@@")
        return False