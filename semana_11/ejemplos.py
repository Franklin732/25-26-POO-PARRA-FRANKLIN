"""
Módulo de ejemplos: Demuestra el uso del sistema de gestión de inventario.

Este módulo contiene ejemplos prácticos de cómo usar las clases Producto
e Inventario para realizar operaciones comunes.
"""

from inventario import Inventario
from producto import Producto


def ejemplo_1_operaciones_basicas():
    """Ejemplo 1: Operaciones básicas de inventario."""
    print("\n" + "="*60)
    print("EJEMPLO 1: OPERACIONES BÁSICAS")
    print("="*60)
    
    # Crear un nuevo inventario (no persistente para este ejemplo)
    inv = Inventario("ejemplo_1.json")
    
    # Añadir productos
    print("\n1. Añadiendo productos...")
    id_laptop = inv.añadir_producto("Laptop Dell", 5, 1299.99)
    id_mouse = inv.añadir_producto("Mouse Logitech", 50, 25.99)
    id_teclado = inv.añadir_producto("Teclado Mecánico", 20, 79.99)
    
    print(f"   - Laptop agregada con ID: {id_laptop}")
    print(f"   - Mouse agregado con ID: {id_mouse}")
    print(f"   - Teclado agregado con ID: {id_teclado}")
    
    # Mostrar todos los productos
    print("\n2. Mostrando todos los productos...")
    for i, producto in enumerate(inv.obtener_todos_productos(), 1):
        print(f"   {i}. {producto}")
    
    # Actualizar cantidad
    print("\n3. Actualizando cantidad de mouse...")
    inv.actualizar_cantidad(id_mouse, 45)
    print(f"   Nueva cantidad: {inv.buscar_por_id(id_mouse).cantidad}")
    
    # Actualizar precio
    print("\n4. Actualizando precio del teclado...")
    inv.actualizar_precio(id_teclado, 89.99)
    print(f"   Nuevo precio: ${inv.buscar_por_id(id_teclado).precio}")


def ejemplo_2_busqueda():
    """Ejemplo 2: Búsqueda de productos."""
    print("\n" + "="*60)
    print("EJEMPLO 2: BÚSQUEDA DE PRODUCTOS")
    print("="*60)
    
    inv = Inventario("ejemplo_2.json")
    
    # Agregar productos
    print("\n1. Agregando productos...")
    productos = [
        ("Pantalla Samsung 24\"", 8, 199.99),
        ("Pantalla LG 27\"", 5, 299.99),
        ("Pantalla Asus 32\"", 3, 399.99),
        ("Laptop Lenovo ThinkPad", 2, 899.99),
        ("Laptop HP Pavilion", 4, 799.99),
    ]
    
    for nombre, cantidad, precio in productos:
        inv.añadir_producto(nombre, cantidad, precio)
    
    print(f"   Total agregados: {inv.obtener_cantidad_productos()} productos")
    
    # Búsqueda por nombre: "Pantalla"
    print("\n2. Buscando productos con 'Pantalla'...")
    resultados = inv.buscar_por_nombre("Pantalla")
    print(f"   Se encontraron {len(resultados)} productos:")
    for producto in resultados:
        print(f"   - {producto.nombre}")
    
    # Búsqueda por nombre: "Laptop"
    print("\n3. Buscando productos con 'Laptop'...")
    resultados = inv.buscar_por_nombre("Laptop")
    print(f"   Se encontraron {len(resultados)} productos:")
    for producto in resultados:
        print(f"   - {producto.nombre}")
    
    # Búsqueda por ID
    print("\n4. Buscando producto con ID 1...")
    producto = inv.buscar_por_id(1)
    if producto:
        print(f"   Encontrado: {producto}")


def ejemplo_3_estadisticas():
    """Ejemplo 3: Cálculo de estadísticas."""
    print("\n" + "="*60)
    print("EJEMPLO 3: ESTADÍSTICAS DEL INVENTARIO")
    print("="*60)
    
    inv = Inventario("ejemplo_3.json")
    
    # Agregar productos con diferentes valores
    print("\n1. Agregando productos de ejemplo...")
    inv.añadir_producto("Producto A", 100, 10.00)  # Valor: $1000
    inv.añadir_producto("Producto B", 50, 20.00)   # Valor: $1000
    inv.añadir_producto("Producto C", 25, 40.00)   # Valor: $1000
    inv.añadir_producto("Producto D", 10, 100.00)  # Valor: $1000
    
    # Calcular y mostrar estadísticas
    print("\n2. Calculando estadísticas...")
    stats = inv.obtener_estadisticas()
    
    print(f"\n   Cantidad de productos diferentes: {stats['cantidad_productos']}")
    print(f"   Cantidad total de items: {stats['cantidad_items_totales']}")
    print(f"   Valor total inventario: ${stats['valor_total_inventario']:.2f}")
    print(f"   Precio promedio por producto: ${stats['precio_promedio']:.2f}")
    
    # Calcular valor de producto específico
    print("\n3. Cálculo de valor por producto:")
    for producto in inv.obtener_todos_productos():
        print(f"   {producto.nombre}: ${producto.obtener_valor_total():.2f}")


def ejemplo_4_crud_completo():
    """Ejemplo 4: Operaciones CRUD completas."""
    print("\n" + "="*60)
    print("EJEMPLO 4: OPERACIONES CRUD COMPLETAS")
    print("="*60)
    
    inv = Inventario("ejemplo_4.json")
    
    # CREATE (Crear)
    print("\n1. CREATE - Creando productos...")
    id1 = inv.añadir_producto("Monitor Samsung", 10, 250.00)
    id2 = inv.añadir_producto("Teclado Corsair", 15, 120.00)
    id3 = inv.añadir_producto("Mouse Razer", 20, 80.00)
    print(f"   Productos creados: {inv.obtener_cantidad_productos()}")
    
    # READ (Leer)
    print("\n2. READ - Leyendo datos...")
    print("   Todos los productos:")
    for p in inv.obtener_todos_productos():
        print(f"   - {p}")
    
    # UPDATE (Actualizar)
    print("\n3. UPDATE - Actualizando datos...")
    print("   - Actualizando cantidad de Monitor...")
    inv.actualizar_cantidad(id1, 5)
    print("   - Actualizando precio de Teclado...")
    inv.actualizar_precio(id2, 99.99)
    
    print(f"\n   Monitor actualizado: {inv.buscar_por_id(id1)}")
    print(f"   Teclado actualizado: {inv.buscar_por_id(id2)}")
    
    # DELETE (Eliminar)
    print("\n4. DELETE - Eliminando producto...")
    print(f"   - Eliminando Mouse (ID {id3})...")
    if inv.eliminar_producto(id3):
        print(f"   Productos restantes: {inv.obtener_cantidad_productos()}")


def ejemplo_5_persistencia():
    """Ejemplo 5: Almacenamiento en archivos."""
    print("\n" + "="*60)
    print("EJEMPLO 5: ALMACENAMIENTO EN ARCHIVOS (PERSISTENCIA)")
    print("="*60)
    
    # GUARDAR
    print("\n1. Creando inventario y guardando...")
    inv1 = Inventario("ejemplo_persistencia.json")
    inv1.añadir_producto("Producto X", 25, 150.00)
    inv1.añadir_producto("Producto Y", 30, 200.00)
    inv1.guardar_en_archivo()
    
    print(f"   Inventario guardado con {inv1.obtener_cantidad_productos()} productos")
    
    # CARGAR
    print("\n2. Creando nuevo inventario y cargando desde archivo...")
    inv2 = Inventario("ejemplo_persistencia.json")  # Se carga automáticamente
    
    print(f"   Inventario cargado con {inv2.obtener_cantidad_productos()} productos")
    print("   Productos recuperados:")
    for p in inv2.obtener_todos_productos():
        print(f"   - {p}")


def ejemplo_6_validaciones():
    """Ejemplo 6: Validaciones y manejo de errores."""
    print("\n" + "="*60)
    print("EJEMPLO 6: VALIDACIONES Y MANEJO DE ERRORES")
    print("="*60)
    
    inv = Inventario("ejemplo_6.json")
    
    # Intento con valores negativos
    print("\n1. Intentando crear producto con cantidad negativa...")
    try:
        inv.añadir_producto("Producto", -5, 100)
        print("   ✗ No se validó correctamente")
    except ValueError as e:
        print(f"   ✓ Validación correcta: {e}")
    
    # Intento con ID inexistente
    print("\n2. Buscando producto con ID inexistente...")
    producto = inv.buscar_por_id(999)
    if producto is None:
        print("   ✓ Retorna None para ID inexistente")
    
    # Intento de eliminar inexistente
    print("\n3. Intentando eliminar producto inexistente...")
    resultado = inv.eliminar_producto(999)
    if not resultado:
        print("   ✓ Retorna False para eliminación fallida")
    
    # Actualización de producto inexistente
    print("\n4. Intentando actualizar producto inexistente...")
    resultado = inv.actualizar_cantidad(999, 100)
    if not resultado:
        print("   ✓ Retorna False para actualización en inexistente")


def main():
    """Ejecuta todos los ejemplos."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*12 + "EJEMPLOS DE USO - SISTEMA DE INVENTARIO" + " "*6 + "║")
    print("╚" + "="*58 + "╝")
    
    # Ejecutar ejemplos
    ejemplo_1_operaciones_basicas()
    ejemplo_2_busqueda()
    ejemplo_3_estadisticas()
    ejemplo_4_crud_completo()
    ejemplo_5_persistencia()
    ejemplo_6_validaciones()
    
    print("\n" + "="*60)
    print("✓ TODOS LOS EJEMPLOS COMPLETADOS EXITOSAMENTE")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
