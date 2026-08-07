from transaction.transaction import Transaction


class Deposit(Transaction):

    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        success = account.deposit(self.amount)

        if success:
             account.history.add_transaction(self)