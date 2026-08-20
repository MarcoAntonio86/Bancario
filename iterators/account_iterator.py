class AccountIterator:
    def __init__(self, accounts):
        self._accounts = accounts
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._accounts):
            raise StopIteration

        account = self._accounts[self._index]
        self._index += 1

        return {
            "branch": account.branch,
            "number": account.number,
            "customer": account.customer.name,
            "balance": account.balance,
        }