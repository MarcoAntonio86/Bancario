from datetime import datetime


class TransactionHistory:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def generate_report(self, transaction_type=None):
        for transaction in self.transactions:
            if(
                transaction_type is None
                or transaction["type"] == transaction_type
            ):
                yield transaction