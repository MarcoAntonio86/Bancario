from models.customer import Customer

class IndividualCustomer(Customer):
    def __init__(self, address, cpf, name, birth_date):
        super().__init__(address)
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date

    @property
    def cpf(self):
        return self._cpf

    @property
    def name(self):
        return self._name

    @property
    def birth_date(self):
        return self._birth_date