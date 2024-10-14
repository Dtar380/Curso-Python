###########################################################
#####  Ejemplo Ejercicio 1 curso Python 24/25 IES RM  #####
#####                Cajero Automatico                #####
###########################################################

#####  Primero, declaramos las variables
saldo = 0 # Saldo con el que se va a iniciar
opcion = "" # Opción que se va a realizar (vacía)

# Solicitamos el saldo inicial a traves de un input
saldo = float(input("Ingrese su saldo inicial: "))

#####  A continuación hacemos uso de un bucle while
# Iniciamos un bucle que terminara cuando opcion valga "s"
while opcion != "s":

    # Mostrar opciones 
    print("Opciones:")
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Ver saldo")
    print("s. Salir")

    # Solicitamos la opción que se va a realizar
    opcion = input("Ingrese su opción: ")

    #####  A continuación hacemos uso de condicionales
    # Evaluamos la opción recibida
    if opcion == "1":
        # * Este código se ejecuta si la opción es la 1 (Retirar dinero)

        # Solicitamos la cantidad que se va a retirar
        cantidad = float(input("Ingrese la cantidad a retirar: "))

        # Comprobamos que hay suficiente saldo
        if cantidad > saldo:
            # * Este código se ejecuta si no hay saldo suficiente en la cuenta

            print("No tiene suficiente saldo") # Avisamos al usuario de que no tiene suficiente saldo

        else:
            # * Este código se ejecuta si hay saldo suficiente en la cuenta

            saldo -= cantidad # Actualizamos el saldo restandole la cantidad retirada
            print("Retiro exitoso") # Avisamos al usuario de que se ha retirado correctamente

    elif opcion == "2":
        # * Este código se ejecuta si la opción es la 2 (Depositar dinero)

        # Solicitamos la cantidad que se va a depositar
        cantidad = float(input("Ingrese la cantidad a depositar: "))

        saldo += cantidad # Actualizamos el saldo sumando la cantidad depositada
        print("Depósito exitoso") # Avisamos al usuario de que se ha depositado correctamente

    elif opcion == "3":
        # * Este código se ejecuta si la opción es la 3 (Ver saldo)

        print("Su saldo es: ", saldo) # Imprimimos el saldo actual

    elif opcion == "s":
        # * Este código se ejecuta si la opción es la s (Salir)

        print("Gracias por utilizar el cajero") # Avisamos al usuario de que se ha cerrado el cajero

    else:
        # * Este código se ejecuta si la opción no es ninguna de las anteriores

        print("Opción inválida") # Avisamos al usuario de que la opción es inválida
