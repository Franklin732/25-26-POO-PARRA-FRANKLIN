# Comparación: Programación Tradicional vs Programación Orientada a Objetos (POO)

## Objetivo
Este documento compara dos enfoques diferentes para resolver el mismo problema: calcular el promedio semanal de temperaturas. Uno utiliza programación tradicional (estructurada) y el otro utiliza programación orientada a objetos.

---

## Análisis Comparativo

### 1. **Enfoque de Programación Tradicional**

#### Características:
- Funciones independientes que procesan datos
- Datos separados de las funciones que los manipulan
- Flujo secuencial: entrada → procesamiento → salida
- No hay encapsulamiento de datos

#### Estructura del código:
```python
def ingresar_temperaturas():
    # Retorna una lista de temperaturas
    
def calcular_promedio(temperaturas):
    # Recibe datos y retorna resultado
    
def mostrar_resultado(promedio):
    # Muestra el resultado
    
def main():
    # Coordina el flujo
```

#### Ventajas:
**Fácil de entender** para principiantes  
**Código simple y directo**  
**Menos líneas de código**  
**Ideal para programas pequeños**  

#### Desventajas:
**Datos dispersos** en el programa  
**Difícil de mantener** si crece el proyecto  
**Sin protección de datos** (cualquier función puede modificarlos)  
**Reutilización limitada** de código  

---

### 2. **Enfoque de Programación Orientada a Objetos (POO)**

#### Características:
- **Clase `ClimaSemanal`** que encapsula datos y comportamiento
- **Datos y métodos unidos** dentro de la clase
- **Atributo privado** (`__temperaturas`) protegido
- **Métodos** que operan sobre los datos internos

#### Estructura del código:
```python
class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []  # Dato privado
    
    def ingresar_temperaturas(self):
        # Modifica datos internos
    
    def calcular_promedio(self):
        # Opera sobre datos propios
    
    def mostrar_resultado(self):
        # Accede a datos privados
```

#### Ventajas:
**Encapsulamiento**: datos protegidos con `__`  
**Organización**: datos y métodos juntos  
**Mantenibilidad**: código más fácil de actualizar  
**Reutilización**: se puede heredar o extender  
**Seguridad**: control sobre cómo se accede a los datos  

#### Desventajas:
**Más líneas de código**  
**Curva de aprendizaje mayor**  
**Puede ser excesivo** para programas muy simples  
**Requiere entender conceptos** como clases y objetos  

---

## Tabla Comparativa

| Aspecto | Tradicional | POO |
|--------|------------|-----|
| **Complejidad** | Baja | Media-Alta |
| **Mantenibilidad** | Difícil (proyecto crece) | Fácil |
| **Encapsulamiento** | No | Sí |
| **Protección de datos** | No | Sí |
| **Organización** | Por funciones | Por clases/objetos |
| **Reutilización** | Limitada | Excelente |
| **Líneas de código** | Menos | Más |
| **Ideal para** | Programas simples | Proyectos grandes |

---

## Flujo de Ejecución

### Programación Tradicional:
```
main()
  └─→ ingresar_temperaturas() → lista de temperaturas
       └─→ calcular_promedio(lista) → valor numérico
            └─→ mostrar_resultado(promedio) → imprime en pantalla
```

### Programación Orientada a Objetos:
```
main()
  └─→ clima = ClimaSemanal()  (crear objeto)
       └─→ clima.ingresar_temperaturas()  (modificar atributo privado)
            └─→ clima.mostrar_resultado()  (acceder a datos privados)
                 └─→ calcular_promedio()  (operación interna)
```

---

## Implementación en Este Proyecto

### Archivo: `programacion_tradicional.py`
**Enfoque**: Estructurado y funcional
- Tres funciones principales + función coordinadora `main()`
- Las temperaturas se pasan entre funciones como parámetros
- El programa fluye de manera lineal y secuencial
- **Ideal para aprender los conceptos básicos de programación**

### Archivo: `programacion_poo.py`
**Enfoque**: Orientado a Objetos
- Una clase `ClimaSemanal` que encapsula toda la lógica
- Los datos se guardan en un atributo privado (`__temperaturas`)
- Los métodos acceden y manipulan estos datos internamente
- Mayor control y seguridad sobre los datos
- **Preparación para proyectos más complejos**

---

## Conclusiones

### ¿Cuándo usar Programación Tradicional?
- Scripts simples y puntuales
- Automatizaciones pequeñas
- Aprendizaje inicial de programación
- Problemas que se resuelven rápido

### ¿Cuándo usar Programación Orientada a Objetos?
- Proyectos grandes y complejos
- Trabajo en equipo (código más organizado)
- Sistemas que requieren expansión futura
- Cuando necesitas reutilizar código frecuentemente
- Aplicaciones que manejan múltiples "entidades" (usuarios, productos, etc.)

### En Este Caso:
Ambos enfoques **resuelven el mismo problema correctamente**, pero:
- La versión **tradicional** es más directa y fácil de seguir
- La versión **POO** demuestra mejor estructura y preparación para proyectos mayores

**El paradigma elegido depende del contexto y los requisitos del proyecto.**

---

## Conceptos POO Aplicados

### 1. **Encapsulamiento**
```python
self.__temperaturas = []  # Privado (no accesible desde afuera)
```
Los datos se protegen dentro de la clase, evitando accesos no autorizados.

### 2. **Abstracción**
La clase oculta la complejidad interna. El usuario solo interactúa con métodos simples.

### 3. **Modularidad**
Cada método tiene una responsabilidad clara y específica.

---

## Requisitos Cumplidos

-  Implementación en programación tradicional (funciones)
-  Implementación en POO (clase con encapsulamiento)
-  Ambos programas resuelven el mismo problema
-  Código con comentarios claros
-  Documento comparativo explicativo
-  Buenas prácticas de programación en ambos

---

**Autor**: Franklin Parra  
**Fecha**: 8 de diciembre de 2025  
**Curso**: Programación Orientada a Objetos - Segundo Semestre
