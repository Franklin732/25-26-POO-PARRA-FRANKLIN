# Constructores y Destructores en Python

Este ejemplo muestra el ciclo de vida de un objeto en Python usando `__init__` y `__del__`.

## Cómo ejecutarlo

```bash
python semana_7/main.py
```

## Qué se observa
- El constructor `__init__` inicializa atributos y emite un mensaje al crear el objeto.
- El método `use` simula el trabajo con el recurso.
- Se elimina la referencia con `del` y se fuerza la recolección con `gc.collect()` para mostrar el destructor `__del__`.

## Conceptos clave
- Constructor: se ejecuta al instanciar la clase y prepara el estado inicial.
- Destructor: se ejecuta cuando el objeto es recolectado; aquí imprime un mensaje que simula la liberación de recursos.
