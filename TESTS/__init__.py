
class Cliente:
    def __init__(self, rut, nombre, apellido, saldo, password=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.password = password

    def depositar(self, monto):
        self.saldo += monto
    def retirar(self, monto):
        self.saldo -= monto
    def new_password(self, intento):
        if self.password == intento:
           return intento 
        



