# Definimos la estructura del cliente
class Cliente:
    def __init__(self, rut, nombre, apellido, saldo, password=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = float(saldo)
        self.password = password

# utilize la formula de Diccionario global y no una lista, porque es mas rapido buscar por el rut, sin tener que recorrer toda la lista en un for
banco_datos = {}