# Sistema de Gestión de Biblioteca Digital

## Descripción General

Este proyecto implementa un **Sistema completo de Gestión de Biblioteca Digital** desarrollado en Python con programación orientada a objetos (POO). El sistema permite administrar libros, usuarios, categorías y préstamos de una biblioteca de forma eficiente y estructurada.

## Objetivo

Desarrollar un sistema integral que demuestre el uso avanzado de estructuras de datos de Python (tuplas, listas, diccionarios y conjuntos) combinadas con principios de POO para crear una solución robusta y escalable.

## Características Implementadas

### 1. **Gestión de Libros**
- ✅ Agregar nuevos libros a la biblioteca
- ✅ Quitar libros de la biblioteca
- ✅ Validación de ISBN único
- ✅ Seguimiento de disponibilidad

### 2. **Gestión de Usuarios**
- ✅ Registrar nuevos usuarios
- ✅ Dar de baja usuarios
- ✅ Validación de ID único
- ✅ Prevención de baja de usuarios con préstamos pendientes

### 3. **Sistema de Préstamos**
- ✅ Prestar libros a usuarios
- ✅ Devolver libros prestados
- ✅ Validación de disponibilidad
- ✅ Seguimiento de histórico de préstamos

### 4. **Búsquedas y Filtros**
- ✅ Búsqueda por título (parcial, case-insensitive)
- ✅ Búsqueda por autor
- ✅ Búsqueda por categoría
- ✅ Listado de libros disponibles

### 5. **Reportes y Estadísticas**
- ✅ Estadísticas generales de la biblioteca
- ✅ Listar todos los usuarios registrados
- ✅ Listar libros prestados por usuario
- ✅ Listar categorías disponibles

## Estructura del Proyecto

```
semana_12/
├── biblioteca.py          # Clases principales (Libro, Usuario, Biblioteca)
├── main.py               # Programa principal con pruebas completas
├── test_biblioteca.py    # Suite de pruebas unitarias
├── README.md             # Esta documentación
└── __pycache__/          # Caché de Python
```

## Clases Principales

### Clase `Libro`

Representa un libro individual en la biblioteca.

**Atributos:**
- `autor_titulo` (tupla): Tupla inmutable contiene (autor, título)
- `categoria` (str): Categoría del libro
- `isbn` (str): ISBN único del libro
- `disponible` (bool): Estado de disponibilidad

**Métodos:**
- `__init__(titulo, autor, categoria, isbn)`: Constructor
- `@property autor`: Accede al autor desde la tupla
- `@property titulo`: Accede al título desde la tupla
- `__str__()`: Representación formateada
- `__repr__()`: Representación técnica

**Justificación de tupla:** Se utiliza una tupla para autor y título porque estos atributos nunca cambian una vez creado el libro, proporcionando inmutabilidad y eficiencia.

### Clase `Usuario`

Representa un usuario registrado en la biblioteca.

**Atributos:**
- `id_usuario` (str): ID único del usuario
- `nombre` (str): Nombre del usuario
- `libros_prestados` (list): Lista de ISBNs de libros actualmente prestados

**Métodos:**
- `__init__(id_usuario, nombre)`: Constructor
- `agregar_prestamo(isbn)`: Registra un préstamo
- `devolver_libro(isbn)`: Registra una devolución
- `tiene_prestamos()`: Verifica si hay préstamos pendientes
- `__str__()`: Representación con información del usuario
- `__repr__()`: Representación técnica

**Justificación de lista:** Se usa lista para `libros_prestados` porque necesita:
- Acceso flexible a múltiples elementos
- Capacidad de agregar/remover elementos dinámicamente
- Mantener el orden de préstamos

### Clase `Biblioteca`

Gestiona toda la colección de libros, usuarios y préstamos.

**Atributos:**
- `libros` (dict): `{ISBN: Objeto Libro}` - Diccionario para búsquedas O(1)
- `usuarios` (dict): `{ID Usuario: Objeto Usuario}` - Acceso rápido
- `ids_usuarios` (set): Conjunto de IDs para validar unacidad
- `categorias` (set): Conjunto de categorías disponibles

**Métodos principales:**

#### Gestión de Libros
```python
agregar_libro(titulo, autor, categoria, isbn)      # Añade libro
quitar_libro(isbn)                                  # Quita libro
obtener_libro(isbn)                                 # Obtiene libro por ISBN
```

#### Gestión de Usuarios
```python
registrar_usuario(id_usuario, nombre)              # Registra usuario
dar_baja_usuario(id_usuario)                       # Da de baja usuario
obtener_usuario(id_usuario)                        # Obtiene usuario por ID
```

#### Gestión de Préstamos
```python
prestar_libro(id_usuario, isbn)                    # Realiza préstamo
devolver_libro(id_usuario, isbn)                   # Registra devolución
```

#### Búsquedas
```python
buscar_por_titulo(titulo)                          # Búsqueda parcial
buscar_por_autor(autor)                            # Búsqueda por autor
buscar_por_categoria(categoria)                    # Búsqueda por categoría
```

#### Listados
```python
listar_libros_prestados_usuario(id_usuario)        # Libros de un usuario
listar_todos_libros(solo_disponibles=False)        # Todos los libros
listar_usuarios()                                   # Todos los usuarios
listar_categorias()                                # Todas las categorías
```

#### Estadísticas
```python
obtener_estadisticas()                             # Stats generales
```

**Justificación de estructuras:**
- **Diccionario para libros**: Permite búsqueda O(1) por ISBN
- **Diccionario para usuarios**: Acceso directo por ID
- **Conjunto para IDs**: Valida unacidad automáticamente
- **Conjunto para categorías**: Evita duplicados automáticamente

## Uso del Programa

### Ejecución Principal

```bash
python main.py
```

Este script ejecuta una demostración completa del sistema incluyendo:
1. Creación de biblioteca
2. Agregación de 10 libros de diferentes géneros
3. Registro de 5 usuarios
4. Realización de 7 préstamos
5. Intentos de préstamo con errores
6. Listado de préstamos por usuario
7. Búsquedas por diferentes criterios
8. Devoluciones de libros
9. Listado completo de catálogo
10. Consulta de estadísticas
11. Manejo de errores en baja de usuarios
12. Remoción de libros

### Ejecución de Pruebas

```bash
python -m unittest test_biblioteca.py
```

O de forma más detallada:

```bash
python -m unittest test_biblioteca.py -v
```

### Suite de Pruebas Unitarias

El archivo `test_biblioteca.py` contiene 32 pruebas unitarias que validan:

**TestLibro (4 pruebas)**
- Creación correcta de libros
- Disponibilidad inicial
- Inmutabilidad de tupla
- Representación en string

**TestUsuario (7 pruebas)**
- Creación de usuarios
- Agregación de préstamos
- Devolución de libros
- Validación de préstamos múltiples
- Método `tiene_prestamos()`

**TestBiblioteca (21 pruebas)**
- Agregación/remoción de libros
- Validación de ISBN duplicado
- Registro/baja de usuarios
- Validación de ID duplicado
- Préstamos exitosos y con errores
- Devoluciones
- Búsquedas por título, autor y categoría
- Listados
- Estadísticas
- Validación de errores

## Ejemplo de Uso Interactivo

```python
from biblioteca import Biblioteca

# Crear biblioteca
bib = Biblioteca()

# Agregar libros
bib.agregar_libro("1984", "George Orwell", "Ciencia Ficción", "978-8499896755")
bib.agregar_libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-8418802002")

# Registrar usuarios
bib.registrar_usuario("U001", "Juan García")
bib.registrar_usuario("U002", "María López")

# Prestar libro
bib.prestar_libro("U001", "978-8499896755")

# Buscar libros
libros = bib.buscar_por_titulo("1984")
print(libros)

# Listar libros prestados
prestados = bib.listar_libros_prestados_usuario("U001")
print(prestados)

# Devolver libro
bib.devolver_libro("U001", "978-8499896755")

# Obtener estadísticas
stats = bib.obtener_estadisticas()
print(stats)
```

## Conceptos de POO Utilizados

### Encapsulación
- Atributos privados implícitos
- Métodos públicos bien definidos
- Propiedades para acceso controlado

### Validación y Manejo de Errores
- Validación de entrada en cada método
- Retorno de booleanos para indicar éxito/fracaso
- Mensajes de error descriptivos

### Estructuras de Datos Eficientes
- **Tuplas**: Para datos inmutables (autor, título)
- **Listas**: Para colecciones dinámicas (libros prestados)
- **Diccionarios**: Para acceso rápido por clave (libros, usuarios)
- **Conjuntos**: Para unicidad garantizada (IDs, categorías)

### Documentación
- Docstrings en todas las clases
- Docstrings en todos los métodos públicos
- Comentarios en secciones clave
- Ejemplos de uso

## Complejidad Temporal

| Operación | Complejidad | Justificación |
|-----------|-------------|---------------|
| Buscar libro por ISBN | O(1) | Acceso directo a diccionario |
| Buscar libro por título/autor/categoría | O(n) | Iteración completa de libros |
| Registrar usuario | O(1) | Acceso a diccionario |
| Prestar libro | O(1) | Acceso a diccionario + append lista |
| Devolver libro | O(m) | m = número de préstamos del usuario |
| Listar todos los libros | O(n) | n = número total de libros |

## Validaciones Implementadas

✅ ISBN único (no duplicados)
✅ ID de usuario único
✅ Validación de disponibilidad antes de prestar
✅ Validación de propiedad del libro antes de devolver
✅ Prevención de baja de usuarios con préstamos
✅ Prevención de remoción de libros prestados
✅ Validación de existencia de usuario/libro

## Mejoras Futuras

- [ ] Sistema de multas por retrasos
- [ ] Reserva de libros
- [ ] Historial completo de transacciones
- [ ] Sistema de califcaciones/reseñas
- [ ] Persistencia en base de datos
- [ ] API REST para acceso remoto
- [ ] Interfaz gráfica (GUI)

## Autor

Sistema desarrollado como tarea de Programación Orientada a Objetos.

## Licencia

Código libre para uso educativo.

---

**Nota**: Este sistema sirve como base educativa para entender POO, estructuras de datos y desarrollo de aplicaciones en Python.
