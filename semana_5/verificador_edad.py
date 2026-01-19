"""
VERIFICADOR DE EDAD PARA ACCESO A EVENTO

Propósito:
Este programa verifica si una persona puede acceder a un evento restringido
para mayores de edad (18 años o más). Solicita el nombre y edad del usuario,
luego determina si tiene permiso de acceso y muestra un mensaje informativo.

Tipos de Datos Utilizados:
- str (string): Para almacenar el nombre del usuario
- int (integer): Para almacenar la edad del usuario
- bool (boolean): Para determinar si tiene acceso (True/False)
- float: Para la versión del sistema

Identificadores:
Todos los identificadores siguen la convención snake_case de Python.

Cumplimiento de la Tarea:
Uso de diferentes tipos de datos (int, float, string, boolean)
Identificadores descriptivos en snake_case
Comentarios explicativos en el código
Programa funcional sin errores

Autor: Franklin Parra
Curso: Programación Orientada a Objetos
"""

# ============================================================================
# CONFIGURACIÓN DEL SISTEMA
# ============================================================================

# Variable que almacena la versión actual del sistema (tipo float)
version_sistema = 1.0

# ============================================================================
# MENSAJE DE BIENVENIDA
# ============================================================================

print("=" * 60)
print("VERIFICADOR DE EDAD - ACCESO A EVENTO RESTRINGIDO")
print(f"Versión del Sistema: {version_sistema}")
print("=" * 60)
print()

# ============================================================================
# ENTRADA DE DATOS DEL USUARIO
# ============================================================================

# Solicitar el nombre del usuario (tipo string)
nombre_usuario = input("Ingrese su nombre completo: ")

# Solicitar la edad del usuario (tipo integer)
# Se convierte el input (que es string) a entero con int()
edad_usuario = int(input("Ingrese su edad: "))

# ============================================================================
# VERIFICACIÓN DE ACCESO
# ============================================================================

# Determinar si el usuario tiene acceso al evento (tipo boolean)
# La condición edad_usuario >= 18 retorna True o False
tiene_acceso = edad_usuario >= 18

# ============================================================================
# MENSAJE CONDICIONAL SEGÚN EL ACCESO
# ============================================================================

print()
print("=" * 60)
print("RESULTADO DE LA VERIFICACIÓN")
print("=" * 60)

# Mostrar información del usuario
print(f"Nombre: {nombre_usuario}")
print(f"Edad: {edad_usuario} años")
print(f"Acceso permitido: {tiene_acceso}")
print(f"Versión del sistema: {version_sistema}")
print("-" * 60)

# Mostrar mensaje personalizado según si tiene acceso o no
if tiene_acceso:
    # Mensaje para mayores de edad
    print(f"Bienvenido {nombre_usuario}!")
    print("  Usted cumple con la edad mínima requerida.")
    print("  Puede acceder al evento sin restricciones.")
else:
    # Mensaje para menores de edad
    print(f"Lo sentimos, {nombre_usuario}.")
    print("  Usted no cumple con la edad mínima requerida (18 años).")
    print("  No puede acceder a este evento en este momento.")

print("=" * 60)
print("Gracias por usar nuestro sistema de verificación.")
print("=" * 60)
