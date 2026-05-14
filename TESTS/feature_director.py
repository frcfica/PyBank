#importar funciones y clases de las otras parejas
#crear un bucle while true para el menu prinpipal
#mantener el programa vivo hasta dar opcion en salir

clientes = {}

def menu_admin():
    while True:
        print("\n" + "="*20)
        print("  PANEL DE ADMIN")
        print("="*20)
        print("1. Registrar nuevo cliente")
        print("2. Listar clientes")
        print("3. Volver al Menú Principal")
        
        opcion = input("Seleccione: ")
        if opcion == "3":
            break

def menu_cliente():
    while True:
        print("\n" + "-"*20)
        print("  PORTAL CLIENTE")
        print("-"*20)
        print("1. Ver Saldo")
        print("2. Retirar Dinero")
        print("3. Volver al Menú Principal")
        
        opcion = input("Seleccione: ")
        if opcion == "3":
            break

# Programa Principal
while True:
    print("\n" + "*"*30)
    print("      SISTEMA PYBANK")
    print("*"*30)
    print("1. Menú Administrador")
    print("2. Menú Cliente")
    print("3. Salir")
    
    principal = input("\nIngrese una opción: ")
    
    if principal == "1":
        clave_admin = input("Ingrese clave maestra (ej: admin123): ")
        if clave_admin == "admin123":
            menu_admin()
        else:
            print("Acceso denegado.")
            
    elif principal == "2":
        menu_cliente()
            
    elif principal == "3":
        print("Gracias por usar PyBank. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intente nuevamente.")

print("\nPrograma finalizado.")