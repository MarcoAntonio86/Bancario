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