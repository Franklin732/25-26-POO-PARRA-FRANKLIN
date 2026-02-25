"""
Módulo de pruebas: Tests para validar la funcionalidad del sistema de inventario.

Este módulo contiene pruebas automatizadas para validar que todas las funcionalidades
del sistema de gestión de inventario funcionan correctamente.
"""

import os
import json
import tempfile
from producto import Producto
from inventario import Inventario


def test_producto():
    """Prueba la clase Producto."""
    print("\n" + "="*60)
    print("PRUEBAS - CLASE PRODUCTO")
    print("="*60)
    
    # Crear un producto
    producto = Producto(1, "Laptop", 5, 1299.99)
    print(f"\n✓ Producto creado: {producto}")
    
    # Prubar getters
    assert producto.id == 1
    assert producto.nombre == "Laptop"
    assert producto.cantidad == 5
    assert producto.precio == 1299.99
    print("✓ Getters funcionan correctamente")
    
    # Prubar setters
    producto.nombre = "Laptop Gaming"
    assert producto.nombre == "Laptop Gaming"
    print("✓ Setter de nombre funciona")
    
    producto.cantidad = 10
    assert producto.cantidad == 10
    print("✓ Setter de cantidad funciona")
    
    producto.precio = 1499.99
    assert producto.precio == 1499.99
    print("✓ Setter de precio funciona")
    
    # Prubar valor total
    valor_total = producto.obtener_valor_total()
    assert valor_total == 10 * 1499.99
    print(f"✓ Valor total calculado correctamente: ${valor_total:.2f}")
    
    # Prubar conversión a diccionario
    dict_producto = producto.a_diccionario()
    assert dict_producto['id'] == 1
    assert dict_producto['nombre'] == "Laptop Gaming"
    print("✓ Conversión a diccionario funciona")
    
    # Prubar creación desde diccionario
    producto2 = Producto.desde_diccionario(dict_producto)
    assert producto2.id == producto.id
    assert producto2.nombre == producto.nombre
    print("✓ Creación desde diccionario funciona")
    
    # Prubar validaciones
    try:
        producto_invalido = Producto(2, "Test", -5, 100)
        print("✗ No se validó cantidad negativa")
    except ValueError:
        print("✓ Se valida cantidad negativa correctamente")
    
    try:
        producto_invalido = Producto(2, "Test", 5, -100)
        print("✗ No se validó precio negativo")
    except ValueError:
        print("✓ Se valida precio negativo correctamente")


def test_inventario_operaciones_basicas():
    """Prueba las operaciones básicas del inventario."""
    print("\n" + "="*60)
    print("PRUEBAS - INVENTARIO: OPERACIONES BÁSICAS")
    print("="*60)
    
    inv = Inventario(":memory:")  # Usar archivo temporal
    
    # Prubar añadir productos
    id1 = inv.añadir_producto("Mouse", 50, 25.99)
    id2 = inv.añadir_producto("Teclado", 30, 49.99)
    id3 = inv.añadir_producto("Monitor", 10, 299.99)
    print(f"\n✓ Se añadieron 3 productos (IDs: {id1}, {id2}, {id3})")
    
    # Prubar cantidad de productos
    assert inv.obtener_cantidad_productos() == 3
    print("✓ Cantidad de productos es correcta")
    
    # Prubar cantidad de items totales
    cantidad_total = inv.obtener_cantidad_items()
    assert cantidad_total == 50 + 30 + 10
    print(f"✓ Cantidad total de items: {cantidad_total}")
    
    # Prubar búsqueda por ID
    producto = inv.buscar_por_id(id1)
    assert producto is not None
    assert producto.nombre == "Mouse"
    print(f"✓ Búsqueda por ID funciona: {producto.nombre}")
    
    # Prubar actualización de cantidad
    inv.actualizar_cantidad(id1, 100)
    producto = inv.buscar_por_id(id1)
    assert producto.cantidad == 100
    print("✓ Actualización de cantidad funciona")
    
    # Prubar actualización de precio
    inv.actualizar_precio(id2, 59.99)
    producto = inv.buscar_por_id(id2)
    assert producto.precio == 59.99
    print("✓ Actualización de precio funciona")
    
    # Prubar eliminación de producto
    resultado = inv.eliminar_producto(id3)
    assert resultado == True
    assert inv.obtener_cantidad_productos() == 2
    print("✓ Eliminación de producto funciona")
    
    # Prubar eliminación de producto inexistente
    resultado = inv.eliminar_producto(999)
    assert resultado == False
    print("✓ Se maneja correctamente eliminación de producto inexistente")


def test_busqueda_productos():
    """Prueba la funcionalidad de búsqueda."""
    print("\n" + "="*60)
    print("PRUEBAS - BÚSQUEDA DE PRODUCTOS")
    print("="*60)
    
    inv = Inventario(":memory:")
    
    # Añadir productos con nombres similares
    inv.añadir_producto("Laptop Dell", 5, 1299.99)
    inv.añadir_producto("Laptop HP", 3, 1199.99)
    inv.añadir_producto("Laptop Lenovo", 2, 999.99)
    inv.añadir_producto("Mouse Logitech", 50, 25.99)
    
    # Prueba búsqueda por nombre
    resultados = inv.buscar_por_nombre("Laptop")
    assert len(resultados) == 3
    print(f"✓ Búsqueda por 'Laptop' encontró {len(resultados)} productos")
    
    # Prueba búsqueda parcial
    resultados = inv.buscar_por_nombre("Dell")
    assert len(resultados) == 1
    print(f"✓ Búsqueda por 'Dell' encontró {len(resultados)} producto")
    
    # Prueba búsqueda sin importar mayúsculas/minúsculas
    resultados = inv.buscar_por_nombre("LAPTOP")
    assert len(resultados) == 3
    print("✓ Búsqueda funciona sin importar mayúsculas/minúsculas")
    
    # Prueba búsqueda que no encuentra nada
    resultados = inv.buscar_por_nombre("Inexistente")
    assert len(resultados) == 0
    print("✓ Búsqueda sin resultados retorna lista vacía")


def test_estadisticas():
    """Prueba el cálculo de estadísticas."""
    print("\n" + "="*60)
    print("PRUEBAS - ESTADÍSTICAS DEL INVENTARIO")
    print("="*60)
    
    inv = Inventario(":memory:")
    
    # Producto 1: 10 * $100 = $1000
    inv.añadir_producto("Producto A", 10, 100)
    # Producto 2: 20 * $50 = $1000
    inv.añadir_producto("Producto B", 20, 50)
    # Producto 3: 5 * $200 = $1000
    inv.añadir_producto("Producto C", 5, 200)
    
    stats = inv.obtener_estadisticas()
    
    assert stats['cantidad_productos'] == 3
    print(f"✓ Cantidad de productos: {stats['cantidad_productos']}")
    
    assert stats['cantidad_items_totales'] == 35
    print(f"✓ Cantidad total de items: {stats['cantidad_items_totales']}")
    
    assert stats['valor_total_inventario'] == 3000
    print(f"✓ Valor total del inventario: ${stats['valor_total_inventario']:.2f}")
    
    precio_promedio = (100 + 50 + 200) / 3
    assert abs(stats['precio_promedio'] - precio_promedio) < 0.01
    print(f"✓ Precio promedio: ${stats['precio_promedio']:.2f}")


def test_serializacion():
    """Prueba la serialización y deserialización."""
    print("\n" + "="*60)
    print("PRUEBAS - SERIALIZACIÓN Y DESERIALIZACIÓN")
    print("="*60)
    
    # Crear archivo temporal
    archivo_temp = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
    ruta_archivo = archivo_temp.name
    archivo_temp.close()
    
    try:
        # Crear inventario y añadir productos
        inv1 = Inventario(ruta_archivo)
        inv1.añadir_producto("Producto 1", 10, 100.00)
        inv1.añadir_producto("Producto 2", 20, 200.00)
        inv1.guardar_en_archivo()
        print("✓ Inventario guardado en archivo")
        
        # Cargar en nuevo inventario
        inv2 = Inventario(ruta_archivo)
        assert inv2.obtener_cantidad_productos() == 2
        print("✓ Inventario cargado correctamente desde archivo")
        
        # Verificar datos
        productos = inv2.obtener_todos_productos()
        assert productos[0].nombre == "Producto 1"
        assert productos[0].cantidad == 10
        assert productos[1].nombre == "Producto 2"
        assert productos[1].cantidad == 20
        print("✓ Datos restaurados correctamente")
        
        # Verificar que el archivo es JSON válido
        with open(ruta_archivo, 'r') as f:
            datos = json.load(f)
        assert 'productos' in datos
        assert 'siguiente_id' in datos
        print("✓ Formato JSON válido")
    
    finally:
        # Limpiar archivo temporal
        if os.path.exists(ruta_archivo):
            os.unlink(ruta_archivo)


def test_casos_limite():
    """Prueba casos límite y errores."""
    print("\n" + "="*60)
    print("PRUEBAS - CASOS LÍMITE")
    print("="*60)
    
    inv = Inventario(":memory:")
    
    # Caso: Inventario vacío
    assert inv.obtener_cantidad_productos() == 0
    assert inv.obtener_todos_productos() == []
    print("✓ Manejo de inventario vacío")
    
    # Caso: Búsqueda en inventario vacío
    assert inv.buscar_por_nombre("Test") == []
    print("✓ Búsqueda en inventario vacío retorna lista vacía")
    
    # Caso: Eliminar de inventario vacío
    assert inv.eliminar_producto(1) == False
    print("✓ Eliminación en inventario vacío maneja error")
    
    # Caso: IDs secuenciales
    id1 = inv.añadir_producto("P1", 1, 1)
    id2 = inv.añadir_producto("P2", 1, 1)
    id3 = inv.añadir_producto("P3", 1, 1)
    assert id1 == 1 and id2 == 2 and id3 == 3
    print("✓ IDs asignados secuencialmente")
    
    # Caso: Cantidad y precio cero
    inv.actualizar_cantidad(id1, 0)
    inv.actualizar_precio(id2, 0)
    assert inv.buscar_por_id(id1).cantidad == 0
    assert inv.buscar_por_id(id2).precio == 0
    print("✓ Se permiten valores cero para cantidad y precio")
    
    # Caso: Nombres especiales
    id_especial = inv.añadir_producto("Producto!@#$%^&*()", 1, 1)
    resultado = inv.buscar_por_nombre("!@#$%")
    assert len(resultado) == 1
    print("✓ Manejo de caracteres especiales en nombres")


def ejecutar_todas_pruebas():
    """Ejecuta todas las pruebas."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "PRUEBAS DEL SISTEMA DE INVENTARIO" + " "*11 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        test_producto()
        test_inventario_operaciones_basicas()
        test_busqueda_productos()
        test_estadisticas()
        test_serializacion()
        test_casos_limite()
        
        print("\n" + "="*60)
        print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60 + "\n")
    
    except AssertionError as e:
        print(f"\n✗ PRUEBA FALLIDA: {e}\n")
    except Exception as e:
        print(f"\n✗ ERROR EN LAS PRUEBAS: {e}\n")


if __name__ == "__main__":
    ejecutar_todas_pruebas()
