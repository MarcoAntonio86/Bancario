from models.customer import Customer


class CorporateCustomer(Customer):
    def __init__(self, address, cnpj, company_name):
        super().__init__(address)
        self._cnpj = cnpj
        self._company_name = company_name

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def company_name(self):
        return self._company_name