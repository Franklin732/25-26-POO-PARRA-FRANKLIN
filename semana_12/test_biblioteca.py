"""
Pruebas unitarias para el Sistema de Gestión de Biblioteca Digital
"""

import unittest
from biblioteca import Libro, Usuario, Biblioteca


class TestLibro(unittest.TestCase):
    """Pruebas para la clase Libro."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.libro = Libro("Harry Potter", "J.K. Rowling", "Fantasía", "978-8498385755")
    
    def test_creacion_libro(self):
        """Prueba la creación correcta de un libro."""
        self.assertEqual(self.libro.titulo, "Harry Potter")
        self.assertEqual(self.libro.autor, "J.K. Rowling")
        self.assertEqual(self.libro.categoria, "Fantasía")
        self.assertEqual(self.libro.isbn, "978-8498385755")
    
    def test_disponibilidad_inicial(self):
        """Prueba que un libro nuevo está disponible."""
        self.assertTrue(self.libro.disponible)
    
    def test_tupla_inmutable(self):
        """Prueba que la tupla autor_titulo es inmutable."""
        with self.assertRaises(TypeError):
            self.libro.autor_titulo[0] = "Otro Autor"
    
    def test_representacion_string(self):
        """Prueba la representación en string del libro."""
        str_libro = str(self.libro)
        self.assertIn("Harry Potter", str_libro)
        self.assertIn("J.K. Rowling", str_libro)
        self.assertIn("Disponible", str_libro)


class TestUsuario(unittest.TestCase):
    """Pruebas para la clase Usuario."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.usuario = Usuario("U001", "Juan García")
    
    def test_creacion_usuario(self):
        """Prueba la creación correcta de un usuario."""
        self.assertEqual(self.usuario.id_usuario, "U001")
        self.assertEqual(self.usuario.nombre, "Juan García")
        self.assertEqual(len(self.usuario.libros_prestados), 0)
    
    def test_agregar_prestamo(self):
        """Prueba agregar un préstamo al usuario."""
        self.usuario.agregar_prestamo("978-8498385755")
        self.assertIn("978-8498385755", self.usuario.libros_prestados)
        self.assertEqual(len(self.usuario.libros_prestados), 1)
    
    def test_devolver_libro_existente(self):
        """Prueba devolver un libro que el usuario tiene prestado."""
        self.usuario.agregar_prestamo("978-8498385755")
        resultado = self.usuario.devolver_libro("978-8498385755")
        self.assertTrue(resultado)
        self.assertEqual(len(self.usuario.libros_prestados), 0)
    
    def test_devolver_libro_inexistente(self):
        """Prueba devolver un libro que el usuario no tiene prestado."""
        resultado = self.usuario.devolver_libro("978-9999999999")
        self.assertFalse(resultado)
    
    def test_tiene_prestamos(self):
        """Prueba el método tiene_prestamos."""
        self.assertFalse(self.usuario.tiene_prestamos())
        self.usuario.agregar_prestamo("978-8498385755")
        self.assertTrue(self.usuario.tiene_prestamos())
    
    def test_multiples_prestamos(self):
        """Prueba que un usuario puede tener múltiples préstamos."""
        self.usuario.agregar_prestamo("978-8498385755")
        self.usuario.agregar_prestamo("978-8498385762")
        self.usuario.agregar_prestamo("978-8445076330")
        self.assertEqual(len(self.usuario.libros_prestados), 3)


class TestBiblioteca(unittest.TestCase):
    """Pruebas para la clase Biblioteca."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.biblioteca = Biblioteca()
        self.biblioteca.agregar_libro("Harry Potter", "J.K. Rowling", "Fantasía", "978-8498385755")
        self.biblioteca.agregar_libro("1984", "George Orwell", "Ciencia Ficción", "978-8499896755")
        self.biblioteca.registrar_usuario("U001", "Juan García")
        self.biblioteca.registrar_usuario("U002", "María López")
    
    def test_agregar_libro_exitoso(self):
        """Prueba agregar un libro exitosamente."""
        resultado = self.biblioteca.agregar_libro("Fundación", "Isaac Asimov", "Ciencia Ficción", "978-8435906228")
        self.assertTrue(resultado)
        self.assertIn("978-8435906228", self.biblioteca.libros)
    
    def test_agregar_libro_isbn_duplicado(self):
        """Prueba que no se puede agregar un libro con ISBN duplicado."""
        resultado = self.biblioteca.agregar_libro("Otro Título", "Otro Autor", "Otra Categoría", "978-8498385755")
        self.assertFalse(resultado)
    
    def test_quitar_libro_exitoso(self):
        """Prueba quitar un libro exitosamente."""
        resultado = self.biblioteca.quitar_libro("978-8498385755")
        self.assertTrue(resultado)
        self.assertNotIn("978-8498385755", self.biblioteca.libros)
    
    def test_quitar_libro_no_existe(self):
        """Prueba quitar un libro que no existe."""
        resultado = self.biblioteca.quitar_libro("978-9999999999")
        self.assertFalse(resultado)
    
    def test_registrar_usuario_exitoso(self):
        """Prueba registrar un usuario exitosamente."""
        resultado = self.biblioteca.registrar_usuario("U003", "Carlos López")
        self.assertTrue(resultado)
        self.assertIn("U003", self.biblioteca.ids_usuarios)
    
    def test_registrar_usuario_id_duplicado(self):
        """Prueba que no se puede registrar un usuario con ID duplicado."""
        resultado = self.biblioteca.registrar_usuario("U001", "Otro Nombre")
        self.assertFalse(resultado)
    
    def test_prestar_libro_exitoso(self):
        """Prueba prestar un libro exitosamente."""
        resultado = self.biblioteca.prestar_libro("U001", "978-8498385755")
        self.assertTrue(resultado)
        self.assertFalse(self.biblioteca.libros["978-8498385755"].disponible)
        self.assertIn("978-8498385755", self.biblioteca.usuarios["U001"].libros_prestados)
    
    def test_prestar_libro_no_disponible(self):
        """Prueba que no se puede prestar un libro no disponible."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        resultado = self.biblioteca.prestar_libro("U002", "978-8498385755")
        self.assertFalse(resultado)
    
    def test_prestar_a_usuario_inexistente(self):
        """Prueba prestar a un usuario que no existe."""
        resultado = self.biblioteca.prestar_libro("U999", "978-8498385755")
        self.assertFalse(resultado)
    
    def test_prestar_libro_inexistente(self):
        """Prueba prestar un libro que no existe."""
        resultado = self.biblioteca.prestar_libro("U001", "978-9999999999")
        self.assertFalse(resultado)
    
    def test_devolver_libro_exitoso(self):
        """Prueba devolver un libro exitosamente."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        resultado = self.biblioteca.devolver_libro("U001", "978-8498385755")
        self.assertTrue(resultado)
        self.assertTrue(self.biblioteca.libros["978-8498385755"].disponible)
        self.assertNotIn("978-8498385755", self.biblioteca.usuarios["U001"].libros_prestados)
    
    def test_devolver_libro_no_prestado(self):
        """Prueba devolver un libro que el usuario no tiene prestado."""
        resultado = self.biblioteca.devolver_libro("U001", "978-8498385755")
        self.assertFalse(resultado)
    
    def test_buscar_por_titulo(self):
        """Prueba buscar libros por título."""
        resultados = self.biblioteca.buscar_por_titulo("Harry")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "Harry Potter")
    
    def test_buscar_por_autor(self):
        """Prueba buscar libros por autor."""
        resultados = self.biblioteca.buscar_por_autor("Orwell")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].autor, "George Orwell")
    
    def test_buscar_por_categoria(self):
        """Prueba buscar libros por categoría."""
        resultados = self.biblioteca.buscar_por_categoria("Ciencia Ficción")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "1984")
    
    def test_buscar_sin_resultados(self):
        """Prueba buscar con criterios que no retornen resultados."""
        resultados = self.biblioteca.buscar_por_titulo("Inexistente")
        self.assertEqual(len(resultados), 0)
    
    def test_listar_libros_prestados_usuario(self):
        """Prueba listar libros prestados de un usuario."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        self.biblioteca.prestar_libro("U001", "978-8499896755")
        libros = self.biblioteca.listar_libros_prestados_usuario("U001")
        self.assertEqual(len(libros), 2)
    
    def test_listar_libros_disponibles(self):
        """Prueba listar solo libros disponibles."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        libros_disponibles = self.biblioteca.listar_todos_libros(solo_disponibles=True)
        self.assertEqual(len(libros_disponibles), 1)
        self.assertEqual(libros_disponibles[0].isbn, "978-8499896755")
    
    def test_dar_baja_usuario_exitoso(self):
        """Prueba dar de baja a un usuario sin préstamos."""
        resultado = self.biblioteca.dar_baja_usuario("U002")
        self.assertTrue(resultado)
        self.assertNotIn("U002", self.biblioteca.ids_usuarios)
    
    def test_dar_baja_usuario_con_prestamos(self):
        """Prueba que no se puede dar de baja a un usuario con préstamos."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        resultado = self.biblioteca.dar_baja_usuario("U001")
        self.assertFalse(resultado)
        self.assertIn("U001", self.biblioteca.ids_usuarios)
    
    def test_obtener_estadisticas(self):
        """Prueba obtener estadísticas de la biblioteca."""
        self.biblioteca.prestar_libro("U001", "978-8498385755")
        stats = self.biblioteca.obtener_estadisticas()
        self.assertEqual(stats['total_libros'], 2)
        self.assertEqual(stats['libros_disponibles'], 1)
        self.assertEqual(stats['libros_prestados'], 1)
        self.assertEqual(stats['total_usuarios'], 2)


if __name__ == '__main__':
    unittest.main()
