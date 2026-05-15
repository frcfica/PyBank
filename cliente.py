# Pareja 1 - Javier F. y Adrian
# Esta clase es el "molde" de cada cliente del banco

class Cliente:
    def __init__(self, rut, nombre, apellido, saldo, password=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = float(saldo)
        self.password = password  # empieza en None hasta que el cliente cree su contraseña

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Deposito exitoso. Saldo actual: ${self.saldo}")
        else:
            print("El monto a depositar tiene que ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar tiene que ser mayor a 0.")
        elif monto > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo actual: ${self.saldo}")

    def verificar_password(self, intento):
        return self.password == intento  # devuelve True si coincide, False si no


# Diccionario global donde se guardan todos los clientes
# usamos diccionario y no lista para buscar por RUT rapido, sin recorrer todo
banco_datos = {}
