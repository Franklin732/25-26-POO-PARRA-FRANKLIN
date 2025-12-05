# PROGRAMA PRINCIPAL: Demostración de las 4 Técnicas de POO
# Autor: Franklin Parra
# Asignatura: Programación Orientada a Objetos
# Este programa muestra ejemplos prácticos de Abstracción, Encapsulación, Herencia y Polimorfismo

# Importamos las clases y funciones necesarias de los otros módulos
from abstraccion.figura import Figura
from encapsulacion.cuenta_bancaria import CuentaBancaria
from polimorfismo.demo import demostrar_polimorfismo
import math

# Creamos una clase Circulo que hereda de la clase abstracta Figura
# Esto demuestra ABSTRACCIÓN porque estamos implementando la "plantilla" Figura
class Circulo(Figura):
    """
    Clase que representa un círculo.
    
    Hereda de la clase abstracta Figura e implementa el método calcular_area()
    de forma específica para un círculo.
    """
    
    def __init__(self, radio):
        """
        Constructor que inicializa un círculo con su radio.
        
        Args:
            radio: El radio del círculo (distancia del centro al borde)
        """
        self.radio = radio
    
    def calcular_area(self):
        """
        Implementación del método abstracto para calcular el área del círculo.
        
        Fórmula: área = π × radio²
        
        Returns:
            El área del círculo como un número decimal
        """
        return math.pi * self.radio ** 2

# Este bloque solo se ejecuta si el archivo se corre directamente
# (no si es importado por otro archivo)
if __name__ == "__main__":
    print("=== Técnicas de POO en Python ===\n")
    
    # ==========================================
    # DEMOSTRACIÓN 1: ABSTRACCIÓN
    # ==========================================
    # Creamos un círculo usando la clase que implementa la figura abstracta
    circulo = Circulo(5)
    print(f"Área del círculo: {circulo.calcular_area():.2f}")
    
    # ==========================================
    # DEMOSTRACIÓN 2: ENCAPSULACIÓN
    # ==========================================
    # Creamos una cuenta bancaria y realizamos operaciones
    # El saldo está protegido y solo se puede modificar con depositar() y retirar()
    cuenta = CuentaBancaria()
    cuenta.depositar(100)  # Agregamos $100 a la cuenta
    cuenta.retirar(30)     # Retiramos $30 de la cuenta
    print(f"Saldo actual: ${cuenta.saldo}\n")  # Consultamos el saldo de forma segura
    
    # ==========================================
    # DEMOSTRACIÓN 3 y 4: HERENCIA + POLIMORFISMO
    # ==========================================
    # La función demostrar_polimorfismo() muestra cómo diferentes animales
    # (que heredan de la clase Animal) responden al mismo método de formas diferentes
    demostrar_polimorfismo()