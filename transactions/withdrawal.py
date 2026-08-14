from transactions.transaction import Transaction


class Withdrawal(Transaction):

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        success = account.withdraw(self.amount)

        if success:
             account.history.add_transaction(self)