# Dashboard POO - Semana 8

## Descripcion General

Este proyecto es una adaptacion personalizada del Dashboard de Programacion Orientada a Objetos basado en el repositorio original de [snogales-uea](https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS).

El Dashboard ha sido adaptado especialmente para gestionar, organizar y ejecutar proyectos y scripts relacionados con la materia de Programacion Orientada a Objetos.

## Estudiante
**Nombre:** Franklin Parra  
**Materia:** Programacion Orientada a Objetos  
**Semestre:** 2025-2026  
**Semana:** 8

## Caracteristicas Principales

### 1. **Exploracion Jerarquica**
   - Navega por semanas disponibles en el proyecto
   - Accede a carpetas y archivos organizados
   - Estructura clara e intuitiva

### 2. **Visualizacion de Codigo**
   - Visualiza el codigo de archivos Python antes de ejecutarlos
   - Interfaz clara con separadores visuales
   - Soporta multiples archivos

### 3. **Ejecucion de Scripts**
   - Ejecuta scripts Python en nuevas ventanas
   - Compatible con Windows, Linux y macOS
   - Manejo de errores integrado

### 4. **Gestion de Proyectos**
   - Lista todos los proyectos disponibles
   - Visualiza informacion de archivos
   - Acceso rapido a multiples semanas

### 5. **Documentacion Integrada**
   - Acceso directo a documentacion dentro del dashboard
   - Informacion de version y autor
   - Guia de uso incluida

## Cambios y Adaptaciones Realizadas

### Mejoras de Codigo

#### 1. **Orientacion a Objetos**
```python
class DashboardPOO:
    """Clase para gestionar el dashboard de proyectos POO"""
```
- Se implemento la logica dentro de una clase para mejor organizacion
- Metodos especificos para cada funcionalidad
- Uso de atributos de instancia para mantener estado

#### 2. **Mejora en la Interfaz de Usuario**
- Etiquetas de texto claras y profesionales
- Separadores visuales consistentes
- Mensajes de error claros y descriptivos
- Menus mas intuitivos

#### 3. **Nuevas Funcionalidades**
- **Listar Proyectos:** Visualiza todas las semanas y contenidos disponibles
- **Informacion de Archivo:** Muestra detalles del archivo (tamano, fecha modificacion)
- **Documentacion:** Acceso integrado a informacion sobre el dashboard
- **Acerca de:** Informacion sobre el creador y adaptaciones

#### 4. **Mejor Manejo de Errores**
- Try-except blocks en operaciones de archivo
- Validacion de entrada de usuario
- Mensajes de error descriptivos
- Prevencion de excepciones no capturadas

#### 5. **Codificacion UTF-8**
```python
with open(ruta_absoluta, 'r', encoding='utf-8') as archivo:
```
- Soporte completo para caracteres especiales
- Compatibilidad mejorada con diferentes sistemas

#### 6. **Documentacion del Codigo**
- Docstrings para todas las clases y metodos
- Comentarios explicativos
- Archivo README.md con instrucciones completas

### Estructura del Proyecto

```
semana_8/
├── Dashboard.py          # Dashboard adaptado y mejorado
├── README.md             # Este archivo
├── test_dashboard.py     # Pruebas unitarias
└── (Mas archivos segun sea necesario)
```

## Requisitos

- **Python:** 3.6 o superior
- **Sistema Operativo:** Windows, Linux o macOS
- **Modulos:** Solo modulos estandar (os, subprocess, sys, datetime, pathlib)

## Instalacion y Uso

### 1. Clonar o descargar el repositorio
```bash
git clone https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS temporal_poo
```

### 2. Navegar al directorio semana_8
```bash
cd 25-26-POO-PARRA-FRANKLIN/semana_8
```

### 3. Ejecutar el Dashboard
```bash
python Dashboard.py
```

### 4. Usar el Dashboard
- Selecciona la opcion deseada del menu principal
- Navega por las semanas y archivos
- Visualiza codigo o ejecuta scripts segun sea necesario

## Menu Principal

```
DASHBOARD POO - SEMANA 8
============================================================
Opciones disponibles:
1 - Explorar Semanas
2 - Listar todos los Proyectos
3 - Ver Documentacion
4 - Acerca del Dashboard
0 - Salir
```

## Ejemplos de Uso

### Ejemplo 1: Explorar una Semana
```
Selecciona una opcion: 1
[Se muestra lista de semanas]
Selecciona una semana: 2
[Se muestra contenido de semana 2]
```

### Ejemplo 2: Visualizar Codigo de un Script
```
Selecciona una opcion: 1
Selecciona una semana: 2
Selecciona una carpeta: 1 (abstraccion)
Selecciona un script: 1 (figura.py)
Selecciona una opcion: 1 (Ver Codigo)
[Se muestra el codigo del archivo]
```

### Ejemplo 3: Ejecutar un Script
```
Selecciona una opcion: 1
[... navega hasta un script ...]
Selecciona una opcion: 2 (Ejecutar Script)
[OK] Script ejecutado exitosamente
```

## Funciones Principales

### `__init__`
Inicializa el dashboard y obtiene las semanas disponibles

### `mostrar_codigo(ruta_script)`
Muestra el contenido de un archivo Python

### `ejecutar_codigo(ruta_script)`
Ejecuta un script Python en una nueva ventana

### `listar_proyectos()`
Lista todos los proyectos y semanas disponibles

### `mostrar_semanas()`
Menu para seleccionar y explorar semanas

### `procesar_archivo(ruta_archivo)`
Procesa las opciones disponibles para un archivo

### `mostrar_info_archivo(ruta_archivo)`
Muestra informacion detallada del archivo

## Adaptaciones Futuras

Este dashboard puede ser ampliado con:

1. **Base de datos:** Para guardar favoritos o historial
2. **Busqueda avanzada:** Para encontrar archivos rapidamente
3. **Soporte para otros lenguajes:** Ademas de Python
4. **Interfaz grafica:** Version con GUI usando tkinter o PyQt
5. **Sistema de etiquetas:** Para organizar scripts por tema
6. **Estadisticas:** Informacion sobre progreso en el curso

## Notas Importantes

- El dashboard es completamente independiente de la red
- Funciona con la estructura local del proyecto
- Los cambios en archivos se reflejan automaticamente
- Se recomienda ejecutar desde el directorio raiz del proyecto

## Autor

**Franklin Parra**  
Estudiante de Programacion Orientada a Objetos  
2025-2026

## Licencia

Este proyecto es una adaptacion del trabajo original de [snogales-uea](https://github.com/snogales-uea/2525-PROGRAMACION-ORIENTADA-A-OBJETOS) y se proporciona bajo la misma licencia.

## Contacto y Soporte

Para reportar problemas o sugerencias:
1. Verifica que Python este correctamente instalado
2. Asegurate de estar en el directorio correcto
3. Comprueba que los archivos tengan permisos de lectura

---

**Ultima actualizacion:** 2025-01-26  
**Version:** 1.0
