# Importamos las clases Perro y Gato desde el módulo de herencia
from herencia.animal import Perro, Gato

# TÉCNICA: POLIMORFISMO
# El polimorfismo permite que objetos de diferentes clases respondan
# al mismo método de formas diferentes

def demostrar_polimorfismo():
    """
    Función que demuestra el concepto de polimorfismo.
    
    El polimorfismo significa "muchas formas". En este caso, el mismo método
    hacer_sonido() se comporta de forma diferente dependiendo del tipo de animal.
    
    Aunque tanto Perro como Gato tienen el método hacer_sonido(),
    cada uno lo ejecuta de manera distinta (uno ladra, el otro maúlla).
    Esto es polimorfismo: mismo método, diferentes comportamientos.
    """
    
    # Creamos una lista con diferentes tipos de animales
    # Aunque son de clases diferentes, todos son tratados como "Animal"
    animales = [
        Perro("Firulais"),  # Un perro llamado Firulais
        Gato("Michi")       # Un gato llamado Michi
    ]
    
    # Recorremos la lista y llamamos al mismo método para todos
    # AQUÍ está el polimorfismo: mismo código (animal.hacer_sonido())
    # pero cada animal responde de forma diferente según su tipo
    for animal in animales:
        animal.hacer_sonido()  # Cada animal hará su sonido específico
