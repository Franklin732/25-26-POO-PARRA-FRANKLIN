"""main.py
Interfaz de consola para el sistema de gestion de inventarios con persistencia.
"""

from inventario import Inventario
from producto import Producto


def mostrar_menu():
    """Muestra las opciones del menu principal."""
    print("\nSistema de Gestion de Inventarios")
    print("1. Anadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def leer_entero(mensaje):
    """Lee un numero entero valido desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("Error: debe ingresar un numero entero.")


def leer_flotante(mensaje):
    """Lee un numero flotante valido desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Error: debe ingresar un numero valido.")


def leer_texto(mensaje):
    """Lee un texto no vacio desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el texto no puede estar vacio.")


def imprimir_producto(producto):
    """Imprime los datos de un producto en una linea."""
    print(
        f"ID: {producto.get_id()} | "
        f"Nombre: {producto.get_nombre()} | "
        f"Cantidad: {producto.get_cantidad()} | "
        f"Precio: {producto.get_precio():.2f}"
    )


def ejecutar_menu():
    """Ejecuta el flujo principal del programa con el menu interactivo."""
    inventario = Inventario()
    carga_ok, mensaje_carga = inventario.obtener_estado_carga()
    if carga_ok:
        print(mensaje_carga)
    else:
        print(f"Aviso: {mensaje_carga}")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            producto_id = leer_entero("Ingrese el ID del producto: ")
            nombre = leer_texto("Ingrese el nombre del producto: ")
            cantidad = leer_entero("Ingrese la cantidad: ")
            precio = leer_flotante("Ingrese el precio: ")

            nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
            exito, mensaje = inventario.agregar_producto(nuevo_producto)
            print(mensaje)

        elif opcion == "2":
            producto_id = leer_entero("Ingrese el ID del producto a eliminar: ")
            exito, mensaje = inventario.eliminar_producto(producto_id)
            print(mensaje)

        elif opcion == "3":
            producto_id = leer_entero("Ingrese el ID del producto a actualizar: ")
            print("Deje en blanco el campo que no desea actualizar.")

            cantidad_texto = input("Nueva cantidad: ").strip()
            precio_texto = input("Nuevo precio: ").strip()

            nueva_cantidad = None
            nuevo_precio = None

            if cantidad_texto:
                try:
                    nueva_cantidad = int(cantidad_texto)
                except ValueError:
                    print("Error: la cantidad debe ser un numero entero.")
                    continue

            if precio_texto:
                try:
                    nuevo_precio = float(precio_texto)
                except ValueError:
                    print("Error: el precio debe ser un numero valido.")
                    continue

            if nueva_cantidad is None and nuevo_precio is None:
                print("No se proporcionaron cambios para actualizar.")
                continue

            exito, mensaje = inventario.actualizar_producto(
                producto_id, nueva_cantidad, nuevo_precio
            )
            print(mensaje)

        elif opcion == "4":
            nombre = leer_texto("Ingrese el nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("Productos encontrados:")
                for producto in resultados:
                    imprimir_producto(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            productos = inventario.mostrar_todos()
            if productos:
                print("Listado de productos:")
                for producto in productos:
                    imprimir_producto(producto)
            else:
                print("El inventario esta vacio.")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion no valida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_menu()
