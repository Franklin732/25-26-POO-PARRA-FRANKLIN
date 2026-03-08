"""
Sistema de Gestión de Biblioteca Digital

Este módulo implementa un sistema completo para gestionar una biblioteca digital,
incluyendo la administración de libros, usuarios y préstamos.

Clases principales:
- Libro: Representa un libro con atributos inmutables
- Usuario: Representa un usuario de la biblioteca
- Biblioteca: Gestiona la colección de libros, usuarios y préstamos
"""


class Libro:
    """
    Representa un libro en la biblioteca digital.
    
    Los atributos título y autor se almacenan en una tupla ya que son
    inmutables una vez creados.
    
    Atributos:
        autor_titulo (tuple): Tupla que contiene (autor, título)
        categoria (str): Categoría del libro
        isbn (str): ISBN único del libro
        disponible (bool): Indica si el libro está disponible para préstamo
    """
    
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un libro con sus atributos.
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            categoria (str): Categoría a la que pertenece
            isbn (str): ISBN único del libro
        """
        # Tupla inmutable para autor y título
        self.autor_titulo = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True
    
    @property
    def autor(self):
        """Retorna el autor del libro desde la tupla."""
        return self.autor_titulo[0]
    
    @property
    def titulo(self):
        """Retorna el título del libro desde la tupla."""
        return self.autor_titulo[1]
    
    def __str__(self):
        """Representación en string del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' - Autor: {self.autor} | ISBN: {self.isbn} | Categoría: {self.categoria} | Estado: {estado}"
    
    def __repr__(self):
        """Representación técnica del libro."""
        return f"Libro('{self.titulo}', '{self.autor}', '{self.categoria}', '{self.isbn}')"


class Usuario:
    """
    Representa un usuario registrado en la biblioteca digital.
    
    Atributos:
        id_usuario (str): ID único del usuario
        nombre (str): Nombre del usuario
        libros_prestados (list): Lista de ISBN de libros actualmente prestados
    """
    
    def __init__(self, id_usuario, nombre):
        """
        Inicializa un usuario de la biblioteca.
        
        Args:
            id_usuario (str): ID único del usuario
            nombre (str): Nombre completo del usuario
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []  # Lista para almacenar ISBNs de libros prestados
    
    def agregar_prestamo(self, isbn):
        """
        Registra un préstamo de libro para el usuario.
        
        Args:
            isbn (str): ISBN del libro prestado
        """
        self.libros_prestados.append(isbn)
    
    def devolver_libro(self, isbn):
        """
        Remove un libro de la lista de préstamos del usuario.
        
        Args:
            isbn (str): ISBN del libro a devolver
            
        Returns:
            bool: True si se removió el libro, False si no estaba en la lista
        """
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)
            return True
        return False
    
    def tiene_prestamos(self):
        """
        Verifica si el usuario tiene libros prestados.
        
        Returns:
            bool: True si tiene libros prestados, False en caso contrario
        """
        return len(self.libros_prestados) > 0
    
    def __str__(self):
        """Representación en string del usuario."""
        num_prestamos = len(self.libros_prestados)
        return f"Usuario(ID: {self.id_usuario}, Nombre: {self.nombre}, Libros prestados: {num_prestamos})"
    
    def __repr__(self):
        """Representación técnica del usuario."""
        return f"Usuario('{self.id_usuario}', '{self.nombre}')"


class Biblioteca:
    """
    Gestiona la colección de libros, usuarios y préstamos de la biblioteca digital.
    
    Utiliza estructuras de datos optimizadas:
    - Diccionario para libros (ISBN como clave para búsquedas rápidas)
    - Diccionario para usuarios (ID de usuario como clave)
    - Conjunto para garantizar IDs de usuario únicos
    
    Atributos:
        libros (dict): Diccionario con ISBN como clave y objeto Libro como valor
        usuarios (dict): Diccionario con ID de usuario como clave y objeto Usuario como valor
        ids_usuarios (set): Conjunto de IDs de usuarios únicos registrados
        categorias (set): Conjunto de categorías disponibles
    """
    
    def __init__(self):
        """Inicializa la biblioteca con colecciones vacías."""
        self.libros = {}  # Diccionario: {ISBN: Libro}
        self.usuarios = {}  # Diccionario: {id_usuario: Usuario}
        self.ids_usuarios = set()  # Conjunto para IDs únicos
        self.categorias = set()  # Conjunto de categorías
    
    # ==================== GESTIÓN DE LIBROS ====================
    
    def agregar_libro(self, titulo, autor, categoria, isbn):
        """
        Añade un libro a la biblioteca.
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            categoria (str): Categoría del libro
            isbn (str): ISBN único del libro
            
        Returns:
            bool: True si se añadió exitosamente, False si el ISBN ya existe
        """
        if isbn in self.libros:
            print(f"❌ Error: El ISBN {isbn} ya existe en la biblioteca.")
            return False
        
        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro
        self.categorias.add(categoria)
        print(f"✓ Libro '{titulo}' añadido exitosamente.")
        return True
    
    def quitar_libro(self, isbn):
        """
        Quita un libro de la biblioteca.
        
        Args:
            isbn (str): ISBN del libro a quitar
            
        Returns:
            bool: True si se quitó exitosamente, False si no existe o está prestado
        """
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False
        
        libro = self.libros[isbn]
        if not libro.disponible:
            print(f"❌ Error: El libro '{libro.titulo}' está actualmente prestado.")
            return False
        
        del self.libros[isbn]
        print(f"✓ Libro '{libro.titulo}' removido de la biblioteca.")
        return True
    
    def obtener_libro(self, isbn):
        """
        Obtiene un libro por su ISBN.
        
        Args:
            isbn (str): ISBN del libro
            
        Returns:
            Libro: El objeto Libro si existe, None en caso contrario
        """
        return self.libros.get(isbn)
    
    # ==================== GESTIÓN DE USUARIOS ====================
    
    def registrar_usuario(self, id_usuario, nombre):
        """
        Registra un nuevo usuario en la biblioteca.
        
        Args:
            id_usuario (str): ID único para el usuario
            nombre (str): Nombre del usuario
            
        Returns:
            bool: True si se registró exitosamente, False si el ID ya existe
        """
        if id_usuario in self.ids_usuarios:
            print(f"❌ Error: El ID de usuario {id_usuario} ya está registrado.")
            return False
        
        usuario = Usuario(id_usuario, nombre)
        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)
        print(f"✓ Usuario '{nombre}' registrado exitosamente con ID: {id_usuario}")
        return True
    
    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja un usuario de la biblioteca.
        
        Args:
            id_usuario (str): ID del usuario a dar de baja
            
        Returns:
            bool: True si se dio de baja exitosamente, False si no existe o tiene préstamos
        """
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: El usuario con ID {id_usuario} no existe.")
            return False
        
        usuario = self.usuarios[id_usuario]
        if usuario.tiene_prestamos():
            print(f"❌ Error: El usuario '{usuario.nombre}' tiene {len(usuario.libros_prestados)} libro(s) sin devolver.")
            return False
        
        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"✓ Usuario '{usuario.nombre}' dado de baja exitosamente.")
        return True
    
    def obtener_usuario(self, id_usuario):
        """
        Obtiene un usuario por su ID.
        
        Args:
            id_usuario (str): ID del usuario
            
        Returns:
            Usuario: El objeto Usuario si existe, None en caso contrario
        """
        return self.usuarios.get(id_usuario)
    
    # ==================== GESTIÓN DE PRÉSTAMOS ====================
    
    def prestar_libro(self, id_usuario, isbn):
        """
        Realiza un préstamo de libro a un usuario.
        
        Args:
            id_usuario (str): ID del usuario
            isbn (str): ISBN del libro a prestar
            
        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario
        """
        # Validar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: El usuario con ID {id_usuario} no existe.")
            return False
        
        # Validar que el libro existe
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False
        
        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]
        
        # Validar que el libro está disponible
        if not libro.disponible:
            print(f"❌ Error: El libro '{libro.titulo}' no está disponible para préstamo.")
            return False
        
        # Realizar el préstamo
        libro.disponible = False
        usuario.agregar_prestamo(isbn)
        print(f"✓ '{libro.titulo}' prestado a {usuario.nombre}")
        return True
    
    def devolver_libro(self, id_usuario, isbn):
        """
        Registra la devolución de un libro por parte de un usuario.
        
        Args:
            id_usuario (str): ID del usuario
            isbn (str): ISBN del libro a devolver
            
        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario
        """
        # Validar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: El usuario con ID {id_usuario} no existe.")
            return False
        
        # Validar que el libro existe
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False
        
        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]
        
        # Validar que el usuario tiene este libro prestado
        if not usuario.devolver_libro(isbn):
            print(f"❌ Error: El usuario '{usuario.nombre}' no tiene prestado el libro '{libro.titulo}'.")
            return False
        
        # Registrar la devolución
        libro.disponible = True
        print(f"✓ '{libro.titulo}' devuelto por {usuario.nombre}")
        return True
    
    # ==================== BÚSQUEDAS ====================
    
    def buscar_por_titulo(self, titulo):
        """
        Busca libros por título (búsqueda parcial, insensible a mayúsculas).
        
        Args:
            titulo (str): Título o fragmento del título a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        titulo_lower = titulo.lower()
        resultados = [libro for libro in self.libros.values() 
                     if titulo_lower in libro.titulo.lower()]
        return resultados
    
    def buscar_por_autor(self, autor):
        """
        Busca libros por autor (búsqueda parcial, insensible a mayúsculas).
        
        Args:
            autor (str): Autor o fragmento del nombre del autor a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        autor_lower = autor.lower()
        resultados = [libro for libro in self.libros.values() 
                     if autor_lower in libro.autor.lower()]
        return resultados
    
    def buscar_por_categoria(self, categoria):
        """
        Busca libros por categoría (búsqueda parcial, insensible a mayúsculas).
        
        Args:
            categoria (str): Categoría a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        categoria_lower = categoria.lower()
        resultados = [libro for libro in self.libros.values() 
                     if categoria_lower in libro.categoria.lower()]
        return resultados
    
    # ==================== LISTADOS ====================
    
    def listar_libros_prestados_usuario(self, id_usuario):
        """
        Lista todos los libros prestados a un usuario específico.
        
        Args:
            id_usuario (str): ID del usuario
            
        Returns:
            list: Lista de objetos Libro o None si el usuario no existe
        """
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: El usuario con ID {id_usuario} no existe.")
            return None
        
        usuario = self.usuarios[id_usuario]
        libros = [self.libros[isbn] for isbn in usuario.libros_prestados 
                 if isbn in self.libros]
        return libros
    
    def listar_todos_libros(self, solo_disponibles=False):
        """
        Lista todos los libros en la biblioteca.
        
        Args:
            solo_disponibles (bool): Si True, solo lista libros disponibles
            
        Returns:
            list: Lista de objetos Libro
        """
        libros = list(self.libros.values())
        if solo_disponibles:
            libros = [libro for libro in libros if libro.disponible]
        return libros
    
    def listar_usuarios(self):
        """
        Lista todos los usuarios registrados.
        
        Returns:
            list: Lista de objetos Usuario
        """
        return list(self.usuarios.values())
    
    def listar_categorias(self):
        """
        Lista todas las categorías disponibles.
        
        Returns:
            set: Conjunto de categorías
        """
        return self.categorias
    
    # ==================== ESTADÍSTICAS ====================
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas generales de la biblioteca.
        
        Returns:
            dict: Diccionario con estadísticas
        """
        total_libros = len(self.libros)
        libros_disponibles = sum(1 for libro in self.libros.values() if libro.disponible)
        libros_prestados = total_libros - libros_disponibles
        total_usuarios = len(self.ids_usuarios)
        
        return {
            'total_libros': total_libros,
            'libros_disponibles': libros_disponibles,
            'libros_prestados': libros_prestados,
            'total_usuarios': total_usuarios,
            'categorias': len(self.categorias)
        }
