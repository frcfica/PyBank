# ==========================================================
# PAREJA 4: OPERACIONES (RETIRO)
# ==========================================================
def retirar(usuario):
    monto = float(input("Monto a retirar: "))
    if monto > usuario.saldo:
        print("Saldo insuficiente")
    else:
        confirmar = input("Confirme su clave para retirar: ")
        if confirmar == usuario.password:
            usuario.saldo -= monto
            print(f"Retiro exitoso. Saldo: {usuario.saldo}")
        else:
            print("Clave incorrecta")