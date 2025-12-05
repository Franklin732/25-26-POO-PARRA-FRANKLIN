# Importamos ABC (Abstract Base Class) para crear clases abstractas
# y abstractmethod para definir métodos que deben ser implementados por las clases hijas
from abc import ABC, abstractmethod

# TÉCNICA: ABSTRACCIÓN
# Esta clase representa una figura geométrica de forma general
# Al ser abstracta, no se puede crear un objeto de esta clase directamente
# Solo sirve como "plantilla" para crear otras figuras específicas
class Figura(ABC):
    """
    Clase abstracta que representa una figura geométrica.
    
    La abstracción nos permite definir las características comunes de todas las figuras
    sin tener que especificar los detalles de cada una.
    Cada figura que herede de esta clase deberá implementar su propia forma de calcular el área.
    """
    
    @abstractmethod
    def calcular_area(self):
        """
        Método abstracto para calcular el área de la figura.
        
        Este método DEBE ser implementado por todas las clases que hereden de Figura.
        Si una clase hija no lo implementa, Python mostrará un error.
        Esto garantiza que todas las figuras tengan una forma de calcular su área.
        """
        pass
