"""
Módulo Main: Interfaz de usuario interactiva en consola para el sistema de gestión de inventario.

Este módulo proporciona un menú interactivo que permite al usuario realizar operaciones
sobre el inventario como añadir, eliminar, actualizar, buscar y mostrar productos.
"""

from inventario import Inventario
from producto import Producto


class GestorInventarioUI:
    """Clase que proporciona la interfaz de usuario para el gestor de inventario."""
    
    def __init__(self):
        """Inicializa el gestor de inventario con la UI."""
        self.inventario = Inventario("inventario.json")
    
    def limpiar_pantalla(self) -> None:
        """Limpia la pantalla de la consola."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu_principal(self) -> None:
        """Muestra el menú principal de opciones."""
        print("\n" + "="*60)
        print(" "*15 + "SISTEMA DE GESTIÓN DE INVENTARIO")
        print("="*60)
        print("\n1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Ver estadísticas del inventario")
        print("8. Ver producto por ID")
        print("9. Guardar inventario")
        print("0. Salir")
        print("="*60)
    
    def obtener_opcion(self) -> str:
        """Obtiene la opción del usuario."""
        while True:
            opcion = input("\nSeleccione una opción: ").strip()
            if opcion in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return opcion
            print("✗ Opción inválida. Por favor, intente de nuevo.")
    
    def añadir_producto(self) -> None:
        """Permite al usuario añadir un nuevo producto."""
        print("\n" + "-"*60)
        print("AÑADIR NUEVO PRODUCTO")
        print("-"*60)
        
        try:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("✗ El nombre no puede estar vacío")
                return
            
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("✗ La cantidad no puede ser negativa")
                return
            
            precio = float(input("Precio unitario: "))
            if precio < 0:
                print("✗ El precio no puede ser negativo")
                return
            
            id_producto = self.inventario.añadir_producto(nombre, cantidad, precio)
            print(f"✓ Producto añadido exitosamente con ID: {id_producto}")
        
        except ValueError:
            print("✗ Error: Ingrese valores numéricos válidos para cantidad y precio")
        except Exception as e:
            print(f"✗ Error al añadir producto: {e}")
    
    def eliminar_producto(self) -> None:
        """Permite al usuario eliminar un producto."""
        print("\n" + "-"*60)
        print("ELIMINAR PRODUCTO")
        print("-"*60)
        
        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            
            producto = self.inventario.buscar_por_id(id_producto)
            if not producto:
                print(f"✗ No se encontró producto con ID {id_producto}")
                return
            
            print(f"Producto a eliminar: {producto}")
            confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
            
            if confirmacion == 's':
                if self.inventario.eliminar_producto(id_producto):
                    print("✓ Producto eliminado exitosamente")
                else:
                    print("✗ Error al eliminar el producto")
            else:
                print("Operación cancelada")
        
        except ValueError:
            print("✗ Error: Ingrese un ID numérico válido")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def actualizar_cantidad(self) -> None:
        """Permite al usuario actualizar la cantidad de un producto."""
        print("\n" + "-"*60)
        print("ACTUALIZAR CANTIDAD DE PRODUCTO")
        print("-"*60)
        
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            producto = self.inventario.buscar_por_id(id_producto)
            
            if not producto:
                print(f"✗ No se encontró producto con ID {id_producto}")
                return
            
            print(f"Producto actual: {producto}")
            nueva_cantidad = int(input("Nueva cantidad: "))
            
            if self.inventario.actualizar_cantidad(id_producto, nueva_cantidad):
                print("✓ Cantidad actualizada exitosamente")
            else:
                print("✗ Error al actualizar la cantidad")
        
        except ValueError:
            print("✗ Error: Ingrese valores numéricos válidos")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def actualizar_precio(self) -> None:
        """Permite al usuario actualizar el precio de un producto."""
        print("\n" + "-"*60)
        print("ACTUALIZAR PRECIO DE PRODUCTO")
        print("-"*60)
        
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            producto = self.inventario.buscar_por_id(id_producto)
            
            if not producto:
                print(f"✗ No se encontró producto con ID {id_producto}")
                return
            
            print(f"Producto actual: {producto}")
            nuevo_precio = float(input("Nuevo precio: "))
            
            if self.inventario.actualizar_precio(id_producto, nuevo_precio):
                print("✓ Precio actualizado exitosamente")
            else:
                print("✗ Error al actualizar el precio")
        
        except ValueError:
            print("✗ Error: Ingrese valores numéricos válidos")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def buscar_por_nombre(self) -> None:
        """Permite al usuario buscar productos por nombre."""
        print("\n" + "-"*60)
        print("BUSCAR PRODUCTO POR NOMBRE")
        print("-"*60)
        
        nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        if not nombre:
            print("✗ El nombre no puede estar vacío")
            return
        
        resultados = self.inventario.buscar_por_nombre(nombre)
        
        if resultados:
            print(f"\n✓ Se encontraron {len(resultados)} producto(s):")
            print("-"*60)
            for i, producto in enumerate(resultados, 1):
                print(f"{i}. {producto}")
        else:
            print(f"✗ No se encontraron productos con '{nombre}'")
    
    def mostrar_todos_productos(self) -> None:
        """Muestra todos los productos en el inventario."""
        print("\n" + "-"*60)
        print("INVENTARIO COMPLETO")
        print("-"*60)
        
        productos = self.inventario.obtener_todos_productos()
        
        if not productos:
            print("✗ El inventario está vacío")
            return
        
        print(f"\nTotal de productos: {self.inventario.obtener_cantidad_productos()}\n")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. {producto}")
    
    def mostrar_estadisticas(self) -> None:
        """Muestra las estadísticas del inventario."""
        print("\n" + "-"*60)
        print("ESTADÍSTICAS DEL INVENTARIO")
        print("-"*60)
        
        stats = self.inventario.obtener_estadisticas()
        
        print(f"\nCantidad de productos diferentes: {stats['cantidad_productos']}")
        print(f"Cantidad total de items: {stats['cantidad_items_totales']}")
        print(f"Valor total del inventario: ${stats['valor_total_inventario']:.2f}")
        print(f"Precio promedio por producto: ${stats['precio_promedio']:.2f}")
    
    def mostrar_producto_por_id(self) -> None:
        """Muestra un producto específico por su ID."""
        print("\n" + "-"*60)
        print("BUSCAR PRODUCTO POR ID")
        print("-"*60)
        
        try:
            id_producto = int(input("Ingrese el ID del producto: "))
            producto = self.inventario.buscar_por_id(id_producto)
            
            if producto:
                print(f"\nProducto encontrado:")
                print(f"{producto}")
            else:
                print(f"✗ No se encontró producto con ID {id_producto}")
        
        except ValueError:
            print("✗ Error: Ingrese un ID numérico válido")
    
    def guardar_inventario(self) -> None:
        """Guarda el inventario en archivo."""
        self.inventario.guardar_en_archivo()
    
    def ejecutar(self) -> None:
        """Ejecuta el bucle principal del programa."""
        print("\n✓ Sistema de Gestión de Inventario inicializado")
        
        while True:
            self.mostrar_menu_principal()
            opcion = self.obtener_opcion()
            
            if opcion == '0':
                print("\n¿Desea guardar los cambios antes de salir? (s/n): ", end="")
                if input().lower() == 's':
                    self.guardar_inventario()
                print("\n¡Gracias por usar el Sistema de Gestión de Inventario!\n")
                break
            elif opcion == '1':
                self.añadir_producto()
            elif opcion == '2':
                self.eliminar_producto()
            elif opcion == '3':
                self.actualizar_cantidad()
            elif opcion == '4':
                self.actualizar_precio()
            elif opcion == '5':
                self.buscar_por_nombre()
            elif opcion == '6':
                self.mostrar_todos_productos()
            elif opcion == '7':
                self.mostrar_estadisticas()
            elif opcion == '8':
                self.mostrar_producto_por_id()
            elif opcion == '9':
                self.guardar_inventario()
            
            input("\nPresione Enter para continuar...")


def main():
    """Función principal del programa."""
    gestor = GestorInventarioUI()
    gestor.ejecutar()


if __name__ == "__main__":
    main()
