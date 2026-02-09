"""main.py
Interfaz de consola para el sistema de gestión de inventarios.
"""

from inventario import Inventario
from producto import Producto


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def leer_entero(mensaje):
    """Lee un número entero válido desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        try:
            return int(valor)
        except ValueError:
            print("Error: debe ingresar un número entero.")


def leer_flotante(mensaje):
    """Lee un número flotante válido desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        try:
            return float(valor)
        except ValueError:
            print("Error: debe ingresar un número válido.")


def leer_texto(mensaje):
    """Lee un texto no vacío desde la entrada del usuario."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el texto no puede estar vacío.")


def imprimir_producto(producto):
    """Imprime los datos de un producto en una línea."""
    print(
        f"ID: {producto.get_id()} | "
        f"Nombre: {producto.get_nombre()} | "
        f"Cantidad: {producto.get_cantidad()} | "
        f"Precio: {producto.get_precio():.2f}"
    )


def ejecutar_menu():
    """Ejecuta el flujo principal del programa con el menú interactivo."""
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            producto_id = leer_entero("Ingrese el ID del producto: ")
            nombre = leer_texto("Ingrese el nombre del producto: ")
            cantidad = leer_entero("Ingrese la cantidad: ")
            precio = leer_flotante("Ingrese el precio: ")

            nuevo_producto = Producto(producto_id, nombre, cantidad, precio)
            if inventario.agregar_producto(nuevo_producto):
                print("Producto agregado correctamente.")
            else:
                print("Error: ya existe un producto con ese ID.")

        elif opcion == "2":
            producto_id = leer_entero("Ingrese el ID del producto a eliminar: ")
            if inventario.eliminar_producto(producto_id):
                print("Producto eliminado correctamente.")
            else:
                print("Error: no se encontró un producto con ese ID.")

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
                    print("Error: la cantidad debe ser un número entero.")
                    continue

            if precio_texto:
                try:
                    nuevo_precio = float(precio_texto)
                except ValueError:
                    print("Error: el precio debe ser un número válido.")
                    continue

            if nueva_cantidad is None and nuevo_precio is None:
                print("No se proporcionaron cambios para actualizar.")
                continue

            if inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio):
                print("Producto actualizado correctamente.")
            else:
                print("Error: no se encontró un producto con ese ID.")

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
                print("El inventario está vacío.")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    ejecutar_menu()
