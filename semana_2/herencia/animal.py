# TÉCNICA: HERENCIA
# La herencia permite que una clase "hija" reciba características de una clase "padre"
# Es como cuando los hijos heredan características de sus padres

class Animal:
    """
    Clase padre que representa un animal genérico.
    
    Esta es la clase base que contiene las características comunes a todos los animales.
    Otras clases específicas (como Perro o Gato) heredarán de esta clase.
    """
    
    def __init__(self, nombre):
        """
        Constructor que inicializa un animal con su nombre.
        
        Args:
            nombre: El nombre del animal
            
        Este atributo será heredado por todas las clases hijas,
        es decir, todos los animales tendrán un nombre.
        """
        self.nombre = nombre

    def hacer_sonido(self):
        """
        Método que define el sonido genérico de un animal.
        
        Este método puede ser sobrescrito (reemplazado) por las clases hijas
        para que cada tipo de animal tenga su propio sonido específico.
        """
        print("El animal hace un sonido.")

# La palabra (Animal) entre paréntesis indica que Perro HEREDA de Animal
class Perro(Animal):
    """
    Clase hija que representa un perro específico.
    
    Esta clase hereda el atributo 'nombre' y el método '__init__' de Animal,
    pero redefine el método 'hacer_sonido' para que sea específico de un perro.
    """
    
    def hacer_sonido(self):
        """
        Método que redefine el sonido de un perro.
        
        Este método REEMPLAZA el método hacer_sonido() de la clase padre Animal.
        Ahora, cuando un perro hace sonido, dirá "¡Guau!" en lugar del mensaje genérico.
        """
        print(f"{self.nombre} dice: ¡Guau!")

# La palabra (Animal) entre paréntesis indica que Gato HEREDA de Animal
class Gato(Animal):
    """
    Clase hija que representa un gato específico.
    
    Esta clase hereda el atributo 'nombre' y el método '__init__' de Animal,
    pero redefine el método 'hacer_sonido' para que sea específico de un gato.
    """
    
    def hacer_sonido(self):
        """
        Método que redefine el sonido de un gato.
        
        Este método REEMPLAZA el método hacer_sonido() de la clase padre Animal.
        Ahora, cuando un gato hace sonido, dirá "¡Miau!" en lugar del mensaje genérico.
        """
        print(f"{self.nombre} dice: ¡Miau!")
