###########################################################
#####  Ejemplo Ejercicio 3 curso Python 24/25 IES RM  #####
#####              Gestión de Inventario              #####
###########################################################

#####  Creamos una clase para los productos
# Clase Producto
class Producto:

    # Constructor de la clase
    def __init__(self, nombre, descripcion, precio):

        # Asignar valores
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    # Mostrar información
    def mostrar_informacion(self):

        # Imprimir la información
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Precio:", self.precio)

# Lista para almacenar los productos
productos = []

# Función para agregar un producto
def agregar_producto(nombre, descripcion, precio):
    try:
        # Crear un producto nuevo a partir de la clase Producto
        producto = Producto(nombre, descripcion, precio)
        # Agregar el producto a la lista
        productos.append(producto)
        # Imprimir mensaje de confirmación
        print("Producto agregado con éxito")

    except Exception as e:
        # * Este código se ejecuta si hay un error
        print("Error al agregar producto:", str(e))

# Función para eliminar un producto
def eliminar_producto(nombre):
    try:
        # Usamos un bucle for para recorrer la lista de productos
        for producto in productos:
            # Comprobamos si el nombre coincide
            if producto.nombre == nombre:
                # * Este código se ejecuta si el nombre coincide

                productos.remove(producto) # Eliminar el objeto de la lista
                print("Producto eliminado con éxito") # Imprimir mensaje de confirmación
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
            if producto.nombre == nombre:
                # * Este código se ejecuta si el nombre coincide

                producto.mostrar_informacion() # Mostrar los datos
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
        # * Este código se ejecuta si la opción es la 1 (Agregar producto)
        try:
            # Solicitamos los datos
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))

            agregar_producto(nombre, descripcion, precio) # Ejecutar la función agregar producto

        except ValueError:
            # * Este código se ejecuta si el precio no es un número
            print("Error: El precio debe ser un número")

    elif opcion == "2":
        # * Este código se ejecuta si la opción es la 2 (izar un producto)
        try:
            # Solicitamos los datos
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre) # Ejecutar la función eliminar producto

        except Exception as e:
            # * Este código se ejecuta si hay un error
            print("Error al eliminar producto:", str(e))

    elif opcion == "3":
        # * Este código se ejecuta si la opción es la 3 (Buscar un producto)
        try:
            # Solicitamos los datos
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(nombre) # Ejecutar la función buscar producto

        except Exception as e:
            # * Este código se ejecuta si hay un error
            print("Error al buscar producto:", str(e))

    elif opcion == "4":
        # * Este código se ejecuta si la opcion es la 4 (Salir)
        print("Gracias por utilizar el sistema de gestión de productos")
        break # Terminar el bucle

    else:
        # * Este código se ejecuta si la opción no es ninguna de las anteriores
        print("Opción inválida") # Avisamos al usuario de que la función es inválida
