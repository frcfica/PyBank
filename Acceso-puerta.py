clientes = {}   # diccionario global, es donde se guardan los registros nuevos 

contra_admin = "admini123"
# 1. solo puede crear un usuario nuevo es el administrador
def agregar_cliente():
    # 2. Ingresa contraseña de administrador 
    while True:
        print ("inicia la contraseña admiinistradora\n")
        admin = input("ingrese la contraseña: ")
        if admin==contra_admin:
            print("ACCESO CONSEDIDO\n")
            break # la contraseña admin fue valida
        print ("ERROR CONTRASEÑA\nINTENTAR DE NUEVO")

    # 3. el administrador tendra acceso a la creacion de cuentas
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")

    if rut in clientes:
        print("Error: el RUT ya existe.\n")
    else:
        clientes[rut] = {"nombre": nombre, "password": None}
        print("Cliente agregado correctamente.\n")

# 4. Solo puede acceder al menu es el administrador
def mostrar_clientes():

    # 5. Ingresa contraseña de administrador 
    while True:
        print ("inicia la contraseña admiinistradora\n")
        admin = input("ingrese la contraseña: ")
        if admin==contra_admin:
            print("ACCESO CONSEDIDO\n")
            break # la contraseña admin fue valida

        print ("ERROR CONTRASEÑA\nINTENTAR DE NUEVO")
    if not clientes:
        print("No hay clientes registrados.\n")
    else:
        print("\nLista de clientes:")
        for rut, datos in clientes.items():
            print(f"Nombre: {datos['nombre']} | RUT: {rut}")
        print()

# 6. Ingresa el rut 
def login():
    rut = input("Ingrese su RUT: ")

    # 7. Verificar si el rut existe y si esta en el diccionario global 
    if rut not in clientes:
        print("RUT no encontrado.\n")
        return None

    cliente = clientes[rut]

    # 8. Crear contraseña donde tambien confirmara la contraseña 
    if cliente["password"] is None:
        print("Debe crear una contraseña.")
        while True:
            p1 = input("Cree contraseña: ")
            p2 = input("Confirme contraseña: ")
            if p1 == p2:
                cliente["password"] = p1
                print("Contraseña creada.\n")
                break # la contraseña fue creada exitosamente
            print("No coinciden, intente otra vez.\n")

    # 9. Ingresa la contraseña creada y repetira el suceso hasta que la contraseña sea valida
    while True:
        intento = input("Ingrese su contraseña: ")
        if intento == cliente["password"]:
            print(f"Bienvenido {cliente['nombre']}\n")
            return rut
        print("Contraseña incorrecta.\n") 

def menu():
    while True:
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Iniciar sesion")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida\n")


menu()