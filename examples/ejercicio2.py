###########################################################
#####  Ejemplo Ejercicio 2 curso Python 24/25 IES RM  #####
#####              Gestión de Inventario              #####
###########################################################

#####  Primero, declaramos las variables
# Lista para almacenar los productos
productos = []

#####  A continuación hacemos uso de las funciones
# Función para agregar un producto
def agregar_producto(nombre, descripcion, precio):
    try:
        # Crear un diccionario con los datos
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio
        }

        productos.append(producto) # Agregar el diccionario a la lista
        print("Producto agregado con éxito") # Mensaje de confirmación

    except Exception as e:
        # * Este código se ejecuta si hay un error
        print("Error al agregar producto:", str(e)) # Mensaje de error

# Función para eliminar un producto
def eliminar_producto(nombre):
    try:
        # Usamos un bucle for para recorrer la lista de productos
        for producto in productos:
            # Comprobamos si el nombre coincide
            if producto["nombre"] == nombre:
                # * Este código se ejecuta si el nombre coincide

                productos.remove(producto) # Eliminar el diccionario de la lista
                print("Producto eliminado con éxito") # Mensaje de confirmación
                return # Terminar la función

        # * Este código se ejecuta si el nombre no coincide
        print("Producto no encontrado")

    except Exception as e:
        # * Este código se ejecuta si hay un error
        print("Error al eliminar producto:", str(e))

# Función para buscar un producto
def buscar_producto(nombre):
    try:
        # Usamos un bucle for para recorrer la lista de productos
        for producto in productos:
            # Comprobamos si el nombre coincide
            if producto["nombre"] == nombre:
                # * Este código se ejecuta si el nombre coincide

                # Imprimir la información
                print("Nombre:", producto["nombre"])
                print("Descripción:", producto["descripcion"])
                print("Precio:", producto["precio"])
                return # Terminar la función

        # * Este código se ejecuta si el nombre no coincide
        print("Producto no encontrado")

    except Exception as e:
        # * Este código se ejecuta si hay un error
        print("Error al buscar producto:", str(e))

#####  A continuación hacemos uso de un bucle while infinito
# Bucle para repetir el proceso
while True:

    # Mostrar opciones
    print("Opciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Salir")

    # Solicitamos la opción que se va a realizar
    opcion = input("Ingrese su opción: ")

    #####  A continuación hacemos uso de condicionales
    # Evaluamos la opción recibida
    if opcion == "1":
        # * Este código se ejecuta si la opcion es la 1 (Agregar producto)
        try:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            # Ejecutar la función agregar producto
            agregar_producto(nombre, descripcion, precio)

        except ValueError:
            # * Este código se ejecuta si el precio no es un número
            print("Error: El precio debe ser un número")

    elif opcion == "2":
        # * Este código se ejecuta si la opción es la 2 (Eliminar un producto)
        try:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            # Ejecutar la función eliminar producto
            eliminar_producto(nombre)

        except Exception as e:
            print("Error al eliminar producto:", str(e))

    elif opcion == "3":
        # * Este código se ejecuta si la opción es la 3 (Buscar un producto)
        try:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            # Ejecutar la función buscar producto
            buscar_producto(nombre)

        except Exception as e:
            # * Este código se ejecuta si hay un error
            print("Error al buscar producto:", str(e))

    elif opcion == "4":
        # * Este código se ejecuta si la opción es la 4 (Salir)

        # Avisamos al usuario de que se ha cerrado el sistema
        print("Gracias por utilizar el sistema de gestión de productos")
        break # Terminar el bucle

    else:
        # * Este código se ejecuta si la opción no es ninguna de las anteriores
        print("Opción inválida") # Avisamos al usuario de que la opción es inválida
