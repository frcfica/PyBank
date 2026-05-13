##  Vamos a hacer el testeo del proyecto completo y va a ser volcado en Pybank.py luego
## Lo que no se haya agregado el proyecto lo vamos a agregar aqui y dejar prolijamente indicado

class Cliente: ## parte de "aliagaeyzaguirrej-lgtm" (en Github figura asi, no se quien es)
    def __init__(self, rut, nombre, apellido, saldo_inicial):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = float(saldo_inicial)
        self.password = None #Primeramente vacia ya que va a ser rellenada
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} (RUT: {self.rut})"

class Banco:
    def __init__(self):
        self.usuarios = {} ## Aca la key es el RUT y el valor o value es el objeto "Cliente"
        self.master_key = "hola123" ## Clave maestra para ingresar al portal Administrativo

    def menu_principal(self): ## Manuel tenia esta parte del PANEL y fue mejorada, para poder adaptarlo al sistema completo. 
        while True:
            print("=== SISTEMA BANCARIO CENTRAL ===")
            print("1- Panel de Administrador")
            print("2- Seccion Clientes")
            print("3- Salir de la aplicacion")
            opcion = input("Seleccione una opcion porfavor: ")

            if opcion == "1":
                self.panel_administrador()
            elif opcion == "2":
                self.seccion_clientes()
            elif opcion == "3":
                print("Gracias por usar el sistema bancario central. Que tenga un buen dia!")
                break
            else:
                print("Opcion no valida, pone una opcion valida porfavor.")
    
    ## Aca agregamos el panel de administrador
    def panel_administrador(self):## Manuel tenia esta parte del PANEL y fue mejorada, para poder adaptarlo al sistema completo. 
        clave = input("Ingrese la clave maestra para acceder al panel de administrador: ")
        if clave != self.master_key:
            print("Clave maestra incorrecta. No podes ingresar, intenta de nuevo.")
            return

        print("\n--- REGISTRO NUEVO DE CLIENTE ---") ## El registro de cliente nuevo lo tenia que hacer "sycg207" (en Github figura asi, no se quien es), lo adapte al sistema y lo deje mas ordenado. 
        rut = input("RUT: ")
        if rut in self.usuarios: ## Se verifica si el rut ya esta en el sistema o no.
            print("El RUT ya esta registrado, intenta con otro RUT.")
            return

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        try:
            monto = float(input("Monto inicial: "))
            nuevo_cliente = Cliente(rut, nombre, apellido, monto)
            self.usuarios[rut] = nuevo_cliente
            print("Cliente registrado exitosamente.")
        except ValueError:
            print("Monto inicial invalido. Por favor, ingrese un numero valido.")
    
    ## Aca vamos a colocar el acceso de los clientes a su cuenta
    def seccion_clientes(self):
        rut = input("Ingrese su RUT para acceder a su cuenta: ")
        if rut not in self.usuarios:
            print("RUT no registrado o Erroneo. Por favor, registrese primero en el panel de administrador o coloque bien su RUT.")
            return
        
        cliente = self.usuarios[rut]

        #Aca vamos a validar la clave del usuario

        if cliente.password is None: 
            print(f"Bienvenido {cliente.nombre} {cliente.apellido}. Parece que es tu primera vez ingresando, porfavor crea una clave de acceso para tu cuenta.")
            while True:
                pw1 = input("Ingrese su nueva clave de acceso: ")
                pw2 = input("Confirme su nueva clave de acceso: ")
                if pw1 == pw2 and pw1 != "":
                    cliente.password = pw1
                    print("Contraseña creada exitosamente")
                    break
                print("Las contraseñas no coinciden, intentar de nuevo por favor.")
            else:
                intentos = 3
                while intentos > 0:
                    pwd = input("Ingrese su clave de acceso: ")
                    if pwd == cliente.password:
                        break
                    intentos -= 1
                    print(f"Clave incorrecta, te quedan {intentos} intentos.")
                    if intentos == 0: return

        self.menu_cliente(cliente) ## Si la clave es correcta, se accede al menu del cliente


    def menu_cliente(self, cliente): ## Flavio e ivan, aca hicimos el menu del cliente donde se puede cambiar la clave, retirar dinero, ver su saldo y volver al menu principal.
        while True:
            print(f"\n--- BIENVENIDO {cliente.nombre} {cliente.apellido} ---")
            print("0- Cambiar contraseña")
            print("1- Consultar saldo")
            print("2- Retirar dinero")
            print("3- Volver al menu principal")
            
            op = input("Seleccione una opcion porfavor: ")

            if op == "0":
                actual = input("Ingrese su contraseña actual: ")
                if actual == cliente.password:
                    while True:
                        nueva1 = input("Ingrese su nueva contraseña: ")
                        nueva2 = input("Confirme su nueva contraseña: ")
                        if nueva1 == nueva2 and nueva1 != "":
                            cliente.password = nueva1
                            print("Contraseña cambiada exitosamente.")
                            break
                        print("Las contraseñas no coinciden, intenta de nuevo porfavor.")
                else:
                    print("Contraseña actual incorrecta, no se pudo cambiar la contraseña.")
            elif op == "1":
                print(f"Su saldo actual es: {cliente.saldo}")
            elif op == "2":
                try:
                    monto = float(input("Monto a retirar: "))
                    if monto > cliente.saldo:
                        print("Saldo insuficiente para realizar el retiro.")
                    else:
                        confirmar = input("Confirme su clave para retirar: ")
                        if confirmar == cliente.password:
                            cliente.saldo -= monto
                            print(f"Retiro exitoso. Saldo actual: ${cliente.saldo}")
                except ValueError:
                    print("Monto invalido, porfavor ingrese un numero valido.")

            elif op == "3":
                print("Volviendo al menu principal...")
                break

if __name__ == "__main__":
    banco = Banco()
    banco.menu_principal()