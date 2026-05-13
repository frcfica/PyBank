clientes = {}

#esto es para agregar los nombres y rut de los clientes al diccionario
def agregar_cliente():
    nombre = input("Ingrese su nombre: ")
    rut = input("Ingrese su RUT: ")

    #en caso de que el rut ya exista esto explica que no funciona, el porque no funciona es el rut es una clave asi que no se puede duplicar
    if rut in clientes:
        print("Error: el RUT ya existe.\n")

    else:
        clientes[rut] = nombre
        print("Nombre agregado correctamente.\n")

#esto muestra los clientes
def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
    else:
        print("\nLista de clientes:")
        for rut, nombre in clientes.items():
            print(f"Nombre: {nombre} | RUT: {rut}")
        print()

#esto es un menu que supongo que es temporal, es mas que nada para mostrar que el codigo sirve
def menu():
    while True:
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida\n")

menu()