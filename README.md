# Desafío de Programación: Sistema de Gestión Bancaria "PyBank"

Contexto del Proyecto
El objetivo es desarrollar un sistema de consola que gestione cuentas bancarias mediante dos módulos diferenciados: uno de Administración (para dar de alta usuarios) y uno de Cliente (para operaciones financieras).


El sistema debe utilizar Programación Orientada a Objetos (POO) para representar a los clientes y Diccionarios para el almacenamiento global de la información.


🛠️ Estructura de Datos (El Modelo)
Deben definir una clase Cliente que actúe como estructura base.

Atributos iniciales: RUT, nombre, apellido, saldo inicial y contraseña (que inicialmente estará vacía o en None).

Contenedor Principal: Un diccionario donde la Key sea el RUT y el Value sea la instancia (objeto) del cliente.

🔐 Sistema 1: Panel de Administración
Este módulo es la puerta de entrada para la creación de cuentas.

Validación de Acceso: El administrador debe ingresar una contraseña maestra para entrar (ej: admin123).

Registro de Clientes:

Solicitar RUT, Nombre, Apellido y Monto inicial.

Crear el objeto Cliente y almacenarlo en el diccionario global.

Regla: No se pueden duplicar RUTs.

👤 Sistema 2: Portal del Cliente
Una vez que el cliente existe en el sistema, puede interactuar con su cuenta.

A. Validación e Inicio de Sesión
El usuario ingresa su RUT.

Si el RUT existe:

Caso Nuevo: Si el usuario no tiene contraseña registrada, el sistema debe obligarlo a crear una. Debe pedirla 2 veces y validar que coincidan. Si fallan, mostrar error y reintentar.

Caso Recurrente: Si ya tiene contraseña, solicitarla para ingresar al menú principal.

B. Menú de Operaciones
Al ingresar con éxito, se despliega el siguiente menú:

Cambiar Contraseña: Solicitar la clave actual, validar y luego permitir el ingreso de la nueva (con doble verificación).

Ver Monto: Mostrar el saldo actual del cliente de forma clara.

Realizar Retiro:

Solicitar el monto a retirar.

Validar que el cliente tenga saldo suficiente.

Seguridad: Solicitar la contraseña antes de procesar el retiro.

Resultado: Mostrar el dinero entregado y el saldo restante en la cuenta.

Salir: Finalizar la sesión del cliente y volver al inicio del programa.