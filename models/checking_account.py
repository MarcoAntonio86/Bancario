from models.account import Account

class CheckingAccount(Account):

    def __init__(self, number, customer, withdrawal_limit=500, withdrawal_count_limit=3):
        super().__init__(number, customer)
        self._withdrawal_limit = withdrawal_limit
        self._withdrawal_count_limit = withdrawal_count_limit

    @property
    def withdrawal_limit(self):
        return self._withdrawal_limit

    @property
    def withdrawal_count_limit(self):
        return self._withdrawal_count_limit

   
    def withdraw(self, amount):
        withdrawal_count = len(
            [
                transaction
                for transaction in self.history.transactions
                if transaction["type"] == "Withdrawal"
            ]
        )

        exceeded_limit = amount > self.withdrawal_limit
        exceeded_withdrawals = (
            withdrawal_count >= self.withdrawal_count_limit
        )

        if exceeded_limit:
            print("\n@@@ Operation failed! Withdrawal amount exceeds the limit. @@@")

        elif exceeded_withdrawals:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        else:
            return super().withdraw(amount)

        return False