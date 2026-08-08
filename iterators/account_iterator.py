
class AccountIterator:
    def __init__(self, accounts):
        self._accounts = accounts
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        pass