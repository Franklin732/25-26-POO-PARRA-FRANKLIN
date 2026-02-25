# Sistema Avanzado de Gestión de Inventario

## Descripción

Un sistema completo de gestión de inventario para tiendas que implementa conceptos avanzados de Programación Orientada a Objetos (POO), colecciones de datos y almacenamiento persistente en archivos.

## Características

- ✅ **Gestión de Productos**: Crear, leer, actualizar y eliminar productos
- ✅ **Colecciones Optimizadas**: Uso de diccionarios para búsquedas rápidas (O(1))
- ✅ **Almacenamiento Persistente**: Serialización/deserialización JSON
- ✅ **Búsqueda Avanzada**: Búsqueda por ID y por nombre (parcial)
- ✅ **Estadísticas**: Información sobre el estado del inventario
- ✅ **Interfaz Interactiva**: Menú en consola fácil de usar

## Estructura del Proyecto

```
semana_11/
├── producto.py          # Clase Producto
├── inventario.py        # Clase Inventario
├── main.py              # Interfaz de usuario (UI)
├── inventario.json      # Base de datos del inventario (generado automáticamente)
└── README.md            # Este archivo
```

## Requisitos del Sistema

- Python 3.7 o superior
- No requiere dependencias externas

## Instalación

1. Clonar el repositorio o descargar los archivos
2. Navegar a la carpeta `semana_11`
3. Ejecutar el programa: `python main.py`

## Uso

Al ejecutar el programa, se mostrará un menú interactivo con las siguientes opciones:

```
1. Añadir nuevo producto
2. Eliminar producto
3. Actualizar cantidad de producto
4. Actualizar precio de producto
5. Buscar producto por nombre
6. Mostrar todos los productos
7. Ver estadísticas del inventario
8. Ver producto por ID
9. Guardar inventario
0. Salir
```

### Ejemplo de Uso

#### 1. Añadir un Producto
```
Opción: 1
Nombre del producto: Laptop
Cantidad: 5
Precio unitario: 1299.99
✓ Producto añadido exitosamente con ID: 1
```

#### 2. Buscar por Nombre
```
Opción: 5
Ingrese el nombre del producto a buscar: Laptop
✓ Se encontraron 1 producto(s):
1. ID: 1 | Nombre: Laptop | Cantidad: 5 | Precio: $1299.99 | Valor Total: $6499.95
```

#### 3. Ver Estadísticas
```
Opción: 7
Cantidad de productos diferentes: 3
Cantidad total de items: 12
Valor total del inventario: $5299.97
Precio promedio por producto: $799.99
```

## Describción Técnica de las Clases

### Clase Producto

Representa un item individual del inventario.

**Atributos privados:**
- `_id` (int): Identificador único del producto
- `_nombre` (str): Nombre del producto
- `_cantidad` (int): Cantidad disponible
- `_precio` (float): Precio unitario

**Métodos principales:**
- `__init__()`: Constructor
- Propiedades (@property): Getters para acceso de lectura
- Setters: Establecimiento de valores con validación
- `obtener_valor_total()`: Calcula cantidad × precio
- `a_diccionario()`: Convierte el producto a diccionario
- `desde_diccionario()`: Crea un producto desde diccionario

### Clase Inventario

Gestiona una colección de productos usando un diccionario.

**Atributos privados:**
- `_productos` (Dict[int, Producto]): Diccionario de productos (clave: ID)
- `_ruta_archivo` (str): Ruta del archivo JSON
- `_siguiente_id` (int): Contador para IDs únicos

**Métodos principales:**

| Método | Descripción | Complejidad |
|--------|-------------|-----------|
| `añadir_producto()` | Añade un nuevo producto | O(1) |
| `eliminar_producto()` | Elimina por ID | O(1) |
| `actualizar_cantidad()` | Actualiza cantidad | O(1) |
| `actualizar_precio()` | Actualiza precio | O(1) |
| `buscar_por_id()` | Busca por ID | O(1) |
| `buscar_por_nombre()` | Busca por nombre (parcial) | O(n) |
| `obtener_todos_productos()` | Retorna lista de productos | O(1) |
| `obtener_estadisticas()` | Calcula estadísticas | O(n) |
| `guardar_en_archivo()` | Serializa a JSON | O(n) |
| `cargar_desde_archivo()` | Deserializa desde JSON | O(n) |

### Clase GestorInventarioUI

Proporciona la interfaz de usuario interactiva.

**Métodos principales:**
- `mostrar_menu_principal()`: Muestra el menú
- `obtener_opcion()`: Valida la opción del usuario
- `añadir_producto()`: Interfaz para añadir
- `eliminar_producto()`: Interfaz para eliminar
- `buscar_por_nombre()`: Interfaz para búsqueda
- `mostrar_estadisticas()`: Muestra estadísticas
- `ejecutar()`: Bucle principal del programa

## Uso de Colecciones

### Diccionario para Almacenamiento Principal
```python
self._productos: Dict[int, Producto] = {}
```

**Ventajas:**
- Búsqueda por ID en O(1) (tiempo constante)
- Fácil eliminación por ID
- Actualización eficiente de valores

### Listas para Operaciones Secundarias
```python
productos_encontrados: List[Producto] = [...]
```

**Ventajas:**
- Facilita iteración sobre productos
- Permite búsqueda por nombre
- Ideal para mostrar resultados ordenados

### JSON para Serialización
```json
{
  "productos": [
    {
      "id": 1,
      "nombre": "Laptop",
      "cantidad": 5,
      "precio": 1299.99
    }
  ],
  "siguiente_id": 2
}
```

## Almacenamiento en Archivos

El sistema utiliza **JSON** para la persistencia de datos:

### Ventajas de JSON
- Formato legible por humanos
- Fácil de serializar/deserializar en Python
- Compatible con múltiples lenguajes
- Flexible para futuras ampliaciones

### Métodos de Serialización

#### Guardar (Serialización)
```python
def guardar_en_archivo(self):
    # Convierte objetos Producto a diccionarios
    # Escribe en formato JSON indentado
    # Manejo de excepciones para errores de I/O
```

#### Cargar (Deserialización)
```python
def cargar_desde_archivo(self):
    # Lee el archivo JSON
    # Convierte diccionarios a objetos Producto
    # Restaura el estado del inventario
```

## Validaciones y Manejo de Errores

- ✅ Validación de valores negativos en cantidad y precio
- ✅ Evita IDs duplicados
- ✅ Búsqueda tolerante a mayúsculas/minúsculas
- ✅ Manejo de excepciones en operaciones de archivo
- ✅ Confirmación antes de eliminar productos
- ✅ Validación de entrada del usuario

## Decisiones de Diseño

1. **Uso de propiedades (@property)**: Proporciona acceso encapsulado a atributos privados
2. **Métodos de conversión**: Facilitan la serialización/deserialización
3. **Diccionarios para almacenamiento**: Optimiza búsquedas frecuentes
4. **Métodos de estadísticas**: Proporciona información agregada sin modificar datos
5. **UI separada**: Mantiene la lógica de negocio independiente de la presentación

## Ejemplos de Ejecución

### Agregar productos y buscar

```python
# Crear inventario
inv = Inventario()

# Añadir productos
id1 = inv.añadir_producto("Mouse", 50, 25.99)
id2 = inv.añadir_producto("Teclado", 30, 49.99)

# Buscar
producto = inv.buscar_por_id(id1)
print(producto)  # ID: 1 | Nombre: Mouse | Cantidad: 50 | Precio: $25.99 | Valor Total: $1299.50

# Actualizar
inv.actualizar_cantidad(id1, 35)

# Estadísticas
stats = inv.obtener_estadisticas()
print(f"Valor total: ${stats['valor_total_inventario']:.2f}")
```

## Notas Importantes

- El archivo `inventario.json` se crea automáticamente al guardar
- Si el archivo existe, se carga automáticamente al iniciar
- Los cambios se guardan explícitamente (opción 9 o al salir)
- El programa valida todas las entradas del usuario

## Mejoras Futuras

- [ ] Interfaz gráfica (PyQt/Tkinter)
- [ ] Base de datos (SQLite/PostgreSQL)
- [ ] Reportes y exportación (PDF/Excel)
- [ ] Sistema de usuarios y permisos
- [ ] Código de barras para productos
- [ ] Historial de cambios

## Autor

Desarrollado como parte de la tarea de Semana 11 - POO

## Licencia

Este proyecto es de código abierto y está disponible bajo licencia MIT.
