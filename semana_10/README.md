# Sistema de Gestion de Inventarios Mejorado

## Objetivo
Este proyecto implementa un sistema de gestion de inventarios con persistencia en archivos JSON. El inventario se guarda en un archivo de texto y se reconstruye automaticamente al iniciar el programa.

## Requisitos cumplidos
- Almacenamiento inmediato de altas, bajas y actualizaciones en un archivo JSON.
- Recuperacion automatica del inventario desde el archivo.
- Manejo de excepciones especificas para `FileNotFoundError` y `PermissionError`.
- Creacion automatica del archivo cuando no existe.
- Deteccion y manejo de archivo corrupto con respaldo.
- Interfaz de consola que informa el resultado de operaciones de archivo.

## Estructura de archivos
- [semana_10/main.py](semana_10/main.py)
- [semana_10/inventario.py](semana_10/inventario.py)
- [semana_10/producto.py](semana_10/producto.py)
- [semana_10/inventario.txt](semana_10/inventario.txt) (se crea automaticamente)

## Como ejecutar
1. Abra una terminal en la carpeta `semana_10`.
2. Ejecute:

```bash
python main.py
```

## Como ejecutar pruebas
1. Abra una terminal en la carpeta `semana_10`.
2. Ejecute:

```bash
python -m unittest test_inventario.py
```

## Persistencia del inventario
El archivo `inventario.txt` guarda una lista JSON de productos. Cada producto incluye:
- `id`
- `nombre`
- `cantidad`
- `precio`

Ejemplo de contenido:

```json
[
    {
        "id": 1,
        "nombre": "Lapiz",
        "cantidad": 50,
        "precio": 1.25
    }
]
```

## Manejo de errores
- Si el archivo no existe, se crea uno nuevo vacio.
- Si hay permisos insuficientes, el sistema informa el problema sin detenerse.
- Si el archivo esta corrupto, se respalda y se crea uno nuevo para continuar.

## Pruebas
- Ejecutar el programa con el archivo inexistente para validar la creacion automatica.
- Editar el archivo manualmente con JSON invalido para verificar el respaldo.
- Cambiar permisos del archivo para simular error de escritura.
- Pruebas automatizadas en [semana_10/test_inventario.py](semana_10/test_inventario.py) que cubren:
- Creacion automatica del archivo.
- Carga desde JSON valido.
- Persistencia en altas, bajas y actualizaciones.
- Respaldo ante archivo corrupto.
- Manejo de `PermissionError` en lectura y escritura usando mocks.

## Evidencia de ejecucion
Comando y resultado:

```text
python -m unittest test_inventario.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.073s

OK
```
