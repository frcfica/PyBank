# verifica si el rut existe y si esta en el diccionario dg_clientes
def login_clinte():
    rut = input ("Ingrese su rut:")
    if rut not in clientes:
        print ("Error El RUT no fue encontrado")
        return None
    
    cliente = clientes[rut]

    if cliente["password"] is None :
        print ("Debe de crear una contraseña\n")
        while True:
            cont1 = input ("Cree contraseña:")
            cont2 = input ("Confirme contraseña:")

            if cont1 == cont2:
                cliente["password"] = cont1
                print ("La contraseña fue creada exitosamente\n")
                break #la contraseña fue creda exitosamente 
            
            print ("ERROR La contraseña no coencide\nPorfavor reintentar otravez")

        while True:
            intentos = input ("Ingrese la contraseña:")
            if intentos == cliente["password"]:
                print (f"Bienveido {cliente["nombre"]}")
                return rut 
            
            print ("La contraseña en incorrecta\n")