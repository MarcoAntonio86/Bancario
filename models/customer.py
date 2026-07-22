class Customer:
    def __init__(self, address):
        self._address = address
        self._accounts = []

    @property
    def address(self):
        return self._address

    @property
    def accounts(self):
        return self._accounts

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self._accounts.append(account)