"""
Programa principal - Sistema de Gestión de Biblioteca Digital
Demostración completa del funcionamiento del sistema
"""

from biblioteca import Libro, Usuario, Biblioteca


def separador(titulo=""):
    """Imprime un separador visual."""
    print("\n" + "=" * 70)
    if titulo:
        print(f"  {titulo}")
        print("=" * 70)
    print()


def main():
    """Función principal que ejecuta todas las pruebas del sistema."""
    
    # ==================== INICIALIZACIÓN ====================
    separador("SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL")
    
    # Crear la biblioteca
    biblioteca = Biblioteca()
    print("✓ Biblioteca inicializada\n")
    
    # ==================== AGREGAR LIBROS ====================
    separador("1. AGREGANDO LIBROS A LA BIBLIOTECA")
    
    libros_datos = [
        ("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", "978-8498385755"),
        ("Harry Potter y la Cámara Secreta", "J.K. Rowling", "Fantasía", "978-8498385762"),
        ("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "978-8445076330"),
        ("1984", "George Orwell", "Ciencia Ficción", "978-8499896755"),
        ("Fundación", "Isaac Asimov", "Ciencia Ficción", "978-8435906228"),
        ("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "978-8425402053"),
        ("El quijote", "Miguel de Cervantes", "Clásico", "978-8418802002"),
        ("Orgullo y prejuicio", "Jane Austen", "Romance", "978-8490693032"),
        ("Misterio en el expreso de Oriente", "Agatha Christie", "Misterio", "978-8427289116"),
        ("Los hombres que no amaban a las mujeres", "Stieg Larsson", "Thriller", "978-8466649383"),
    ]
    
    for titulo, autor, categoria, isbn in libros_datos:
        biblioteca.agregar_libro(titulo, autor, categoria, isbn)
    
    # ==================== REGISTRAR USUARIOS ====================
    separador("2. REGISTRANDO USUARIOS")
    
    usuarios_datos = [
        ("U001", "Juan García"),
        ("U002", "María López"),
        ("U003", "Carlos Rodríguez"),
        ("U004", "Ana Martínez"),
        ("U005", "Pedro Sánchez"),
    ]
    
    for id_usuario, nombre in usuarios_datos:
        biblioteca.registrar_usuario(id_usuario, nombre)
    
    # ==================== REALIZAR PRÉSTAMOS ====================
    separador("3. REALIZANDO PRÉSTAMOS")
    
    prestamos = [
        ("U001", "978-8498385755"),  # Juan - Harry Potter 1
        ("U001", "978-8498385762"),  # Juan - Harry Potter 2
        ("U002", "978-8445076330"),  # María - LOTR
        ("U003", "978-8499896755"),  # Carlos - 1984
        ("U004", "978-8435906228"),  # Ana - Fundación
        ("U005", "978-8418802002"),  # Pedro - Quijote
        ("U002", "978-8425402053"),  # María - Cien años de soledad
    ]
    
    for id_usuario, isbn in prestamos:
        biblioteca.prestar_libro(id_usuario, isbn)
    
    # ==================== INTENTAR PRÉSTAMO CON ERRORES ====================
    separador("4. INTENTOS DE PRÉSTAMO CON ERRORES")
    
    print("Intentando prestar un libro ya prestado:")
    biblioteca.prestar_libro("U003", "978-8498385755")  # ISBN está prestado
    
    print("\nIntentando prestar a usuario no registrado:")
    biblioteca.prestar_libro("U999", "978-8490693032")  # Usuario no existe
    
    print("\nIntentando prestar ISBN inexistente:")
    biblioteca.prestar_libro("U001", "000-0000000000")  # ISBN no existe
    
    # ==================== LISTAR LIBROS PRESTADOS ====================
    separador("5. LIBROS PRESTADOS POR USUARIO")
    
    for id_usuario, nombre in usuarios_datos:
        libros_prestados = biblioteca.listar_libros_prestados_usuario(id_usuario)
        print(f"\n📚 Usuario: {nombre} (ID: {id_usuario})")
        if libros_prestados and len(libros_prestados) > 0:
            for libro in libros_prestados:
                print(f"   • {libro.titulo} - {libro.autor}")
        else:
            print("   (Sin libros prestados)")
    
    # ==================== BÚSQUEDAS ====================
    separador("6. BÚSQUEDAS POR DIFERENTES CRITERIOS")
    
    print("Búsqueda por título: 'Harry'")
    resultados = biblioteca.buscar_por_titulo("Harry")
    for libro in resultados:
        print(f"  • {libro}")
    
    print("\nBúsqueda por autor: 'Rowling'")
    resultados = biblioteca.buscar_por_autor("Rowling")
    for libro in resultados:
        print(f"  • {libro}")
    
    print("\nBúsqueda por categoría: 'Fantasía'")
    resultados = biblioteca.buscar_por_categoria("Fantasía")
    for libro in resultados:
        print(f"  • {libro}")
    
    # ==================== DEVOLUCIONES ====================
    separador("7. DEVOLUCIONES DE LIBROS")
    
    devoluciones = [
        ("U001", "978-8498385755"),  # Juan devuelve Harry Potter 1
        ("U002", "978-8445076330"),  # María devuelve LOTR
    ]
    
    for id_usuario, isbn in devoluciones:
        biblioteca.devolver_libro(id_usuario, isbn)
    
    # ==================== INTENTOS DE DEVOLUCIÓN CON ERRORES ====================
    separador("8. INTENTOS DE DEVOLUCIÓN CON ERRORES")
    
    print("Intentando devolver libro no prestado:")
    biblioteca.devolver_libro("U001", "978-8499896755")  # Juan no tiene 1984
    
    print("\nIntentando devolver con usuario no registrado:")
    biblioteca.devolver_libro("U999", "978-8498385755")  # Usuario no existe
    
    # ==================== LISTAR TODOS LOS LIBROS ====================
    separador("9. CATÁLOGO COMPLETO DE LIBROS")
    
    print("Todos los libros en la biblioteca:")
    todos_los_libros = biblioteca.listar_todos_libros()
    for i, libro in enumerate(todos_los_libros, 1):
        print(f"{i:2}. {libro}")
    
    print("\n\nSolo libros disponibles:")
    libros_disponibles = biblioteca.listar_todos_libros(solo_disponibles=True)
    for i, libro in enumerate(libros_disponibles, 1):
        print(f"{i:2}. {libro}")
    
    # ==================== LISTAR CATEGORÍAS ====================
    separador("10. CATEGORÍAS DISPONIBLES")
    
    categorias = biblioteca.listar_categorias()
    print(f"Categorías disponibles ({len(categorias)}):")
    for i, categoria in enumerate(sorted(categorias), 1):
        print(f"  {i}. {categoria}")
    
    # ==================== ESTADÍSTICAS ====================
    separador("11. ESTADÍSTICAS DE LA BIBLIOTECA")
    
    stats = biblioteca.obtener_estadisticas()
    print(f"Total de libros: {stats['total_libros']}")
    print(f"Libros disponibles: {stats['libros_disponibles']}")
    print(f"Libros prestados: {stats['libros_prestados']}")
    print(f"Usuarios registrados: {stats['total_usuarios']}")
    print(f"Categorías: {stats['categorias']}")
    
    # ==================== LISTAR USUARIOS ====================
    separador("12. USUARIOS REGISTRADOS")
    
    usuarios = biblioteca.listar_usuarios()
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. {usuario}")
    
    # ==================== INTENTO DE DAR DE BAJA CON ERROR ====================
    separador("13. INTENTOS DE DAR DE BAJA")
    
    print("Intentando dar de baja a usuario con préstamos pendientes:")
    biblioteca.dar_baja_usuario("U001")  # U001 tiene 1 libro prestado
    
    print("\nIntentando dar de baja a usuario no registrado:")
    biblioteca.dar_baja_usuario("U999")  # Usuario no existe
    
    # ==================== DEVOLVER LIBROS Y DAR DE BAJA ====================
    separador("14. DEVOLUCIÓN Y BAJA DE USUARIO")
    
    print("Devolviendo el último libro de Juan:")
    biblioteca.devolver_libro("U001", "978-8498385762")
    
    print("\nAhora dando de baja a Juan:")
    biblioteca.dar_baja_usuario("U001")
    
    # ==================== QUITAR LIBRO ====================
    separador("15. REMOVER LIBROS")
    
    print("Intentando remover un libro que está prestado:")
    biblioteca.quitar_libro("978-8499896755")  # Está prestado a Carlos
    
    print("\nRemoviendo un libro disponible:")
    biblioteca.quitar_libro("978-8490693032")  # Orgullo y prejuicio (no prestado)
    
    # ==================== ESTADÍSTICAS FINALES ====================
    separador("16. ESTADÍSTICAS FINALES")
    
    stats_finales = biblioteca.obtener_estadisticas()
    print(f"Total de libros: {stats_finales['total_libros']}")
    print(f"Libros disponibles: {stats_finales['libros_disponibles']}")
    print(f"Libros prestados: {stats_finales['libros_prestados']}")
    print(f"Usuarios registrados: {stats_finales['total_usuarios']}")
    print(f"Categorías: {stats_finales['categorias']}")
    
    # ==================== RESUMEN ====================
    separador("RESUMEN DE PRUEBAS COMPLETADAS")
    
    print("""
    ✓ Sistema de Gestión de Biblioteca Digital implementado exitosamente
    
    Funcionalidades probadas:
    ✓ Agregar libros a la biblioteca
    ✓ Registrar usuarios
    ✓ Realizar préstamos de libros
    ✓ Devolver libros
    ✓ Buscar libros por título, autor y categoría
    ✓ Listar libros prestados por usuario
    ✓ Listar todos los libros
    ✓ Consultar estadísticas
    ✓ Validación de errores
    ✓ Dar de baja usuarios
    ✓ Remover libros
    
    Estructuras de datos utilizadas:
    ✓ Tuplas (autor, título) - Atributos inmutables del libro
    ✓ Listas - Libros prestados por usuario
    ✓ Diccionarios - Almacenamiento de libros y usuarios por clave
    ✓ Conjuntos - IDs de usuario únicos y categorías
    """)
    
    print("=" * 70)


if __name__ == "__main__":
    main()
