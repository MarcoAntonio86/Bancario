from modelos.Historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def saldo(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self.agencia
    
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo

        if excedeu_saldo:
             print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
           print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
          
        return False 
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
    
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False
        
        
             

    
