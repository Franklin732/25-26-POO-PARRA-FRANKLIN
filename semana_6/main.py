"""
Programa de Demostración de Programación Orientada a Objetos (POO)
Tema: Sistema de Gestión de Animales
Autor: Franklin Parra
Fecha: Enero 2026

Este programa demuestra los cuatro pilares fundamentales de la POO:
1. CLASES Y OBJETOS: Definición y creación de instancias
2. HERENCIA: Clases derivadas que heredan de una clase base
3. ENCAPSULACIÓN: Uso de atributos privados y métodos getter/setter
4. POLIMORFISMO: Métodos sobrescritos y comportamiento polimórfico
"""


# ============================================================================
# CLASE BASE - Demuestra ENCAPSULACIÓN y define la estructura base
# ============================================================================

class Animal:
    """
    Clase base Animal que demuestra ENCAPSULACIÓN.
    
    Esta clase utiliza atributos privados (con prefijo __) para proteger
    los datos internos y proporciona métodos públicos para acceder a ellos.
    """
    
    def __init__(self, nombre, edad, especie):
        """
        Constructor de la clase Animal.
        
        Parámetros:
            nombre (str): Nombre del animal
            edad (int): Edad del animal en años
            especie (str): Especie del animal
        """
        # ENCAPSULACIÓN: Atributos privados (con doble guión bajo)
        # Estos atributos NO deben ser accedidos directamente desde fuera de la clase
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
        self.__energia = 100  # Energía inicial del animal
    
    # ENCAPSULACIÓN: Métodos Getter - Permiten LEER los atributos privados
    def get_nombre(self):
        """Retorna el nombre del animal."""
        return self.__nombre
    
    def get_edad(self):
        """Retorna la edad del animal."""
        return self.__edad
    
    def get_especie(self):
        """Retorna la especie del animal."""
        return self.__especie
    
    def get_energia(self):
        """Retorna el nivel de energía del animal."""
        return self.__energia
    
    # ENCAPSULACIÓN: Métodos Setter - Permiten MODIFICAR los atributos privados de forma controlada
    def set_nombre(self, nuevo_nombre):
        """Modifica el nombre del animal con validación."""
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena no vacía")
    
    def set_edad(self, nueva_edad):
        """Modifica la edad del animal con validación."""
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: La edad debe ser un número entero positivo")
    
    # Métodos públicos que definen el comportamiento general de los animales
    def hacer_sonido(self):
        """
        Método base para hacer sonido.
        Este método será SOBRESCRITO en las clases derivadas (POLIMORFISMO).
        """
        return "El animal hace un sonido"
    
    def comer(self):
        """Método que simula que el animal come y recupera energía."""
        self.__energia = min(100, self.__energia + 20)
        return f"{self.__nombre} ha comido y ahora tiene {self.__energia}% de energía"
    
    def dormir(self):
        """Método que simula que el animal duerme y recupera energía."""
        self.__energia = 100
        return f"{self.__nombre} ha dormido y recuperó toda su energía"
    
    def jugar(self):
        """Método que simula que el animal juega y pierde energía."""
        self.__energia = max(0, self.__energia - 15)
        return f"{self.__nombre} ha jugado y ahora tiene {self.__energia}% de energía"
    
    def mostrar_info(self):
        """Muestra la información completa del animal."""
        return f"{self.__nombre} | Especie: {self.__especie} | Edad: {self.__edad} años | Energía: {self.__energia}%"


# ============================================================================
# CLASES DERIVADAS - Demuestran HERENCIA y POLIMORFISMO
# ============================================================================

class Perro(Animal):
    """
    Clase Perro que HEREDA de Animal.
    
    HERENCIA: Esta clase obtiene todos los atributos y métodos de Animal
    y puede agregar funcionalidad específica o modificar comportamientos.
    """
    
    def __init__(self, nombre, edad, raza):
        """
        Constructor de Perro.
        
        Parámetros:
            nombre (str): Nombre del perro
            edad (int): Edad del perro
            raza (str): Raza del perro
        """
        # HERENCIA: Llamamos al constructor de la clase padre (Animal)
        super().__init__(nombre, edad, "Perro")
        self.__raza = raza  # ENCAPSULACIÓN: Atributo privado específico de Perro
    
    def get_raza(self):
        """Retorna la raza del perro."""
        return self.__raza
    
    # POLIMORFISMO: Sobrescritura del método hacer_sonido()
    def hacer_sonido(self):
        """
        Sobrescribe el método hacer_sonido() de la clase Animal.
        Este es un ejemplo de POLIMORFISMO - mismo método, diferente implementación.
        """
        return f"{self.get_nombre()} dice: ¡Guau guau!"
    
    # Método específico de la clase Perro
    def traer_pelota(self):
        """Comportamiento específico de los perros."""
        return f"{self.get_nombre()} corre feliz a traer la pelota"


class Gato(Animal):
    """
    Clase Gato que HEREDA de Animal.
    
    HERENCIA: Demuestra cómo diferentes clases pueden heredar de la misma clase base.
    """
    
    def __init__(self, nombre, edad, color_pelaje):
        """
        Constructor de Gato.
        
        Parámetros:
            nombre (str): Nombre del gato
            edad (int): Edad del gato
            color_pelaje (str): Color del pelaje del gato
        """
        # HERENCIA: Llamamos al constructor de la clase padre
        super().__init__(nombre, edad, "Gato")
        self.__color_pelaje = color_pelaje  # ENCAPSULACIÓN: Atributo privado
    
    def get_color_pelaje(self):
        """Retorna el color del pelaje del gato."""
        return self.__color_pelaje
    
    # POLIMORFISMO: Sobrescritura del método hacer_sonido()
    def hacer_sonido(self):
        """
        Implementación específica para gatos.
        POLIMORFISMO: Mismo nombre de método, comportamiento diferente.
        """
        return f"{self.get_nombre()} dice: ¡Miau miau!"
    
    # Método específico de la clase Gato
    def ronronear(self):
        """Comportamiento específico de los gatos."""
        return f"{self.get_nombre()} ronronea contento"


class Pajaro(Animal):
    """
    Clase Pajaro que HEREDA de Animal.
    
    HERENCIA: Tercera clase derivada que demuestra la extensibilidad de la herencia.
    """
    
    def __init__(self, nombre, edad, puede_volar):
        """
        Constructor de Pajaro.
        
        Parámetros:
            nombre (str): Nombre del pájaro
            edad (int): Edad del pájaro
            puede_volar (bool): Indica si el pájaro puede volar
        """
        # HERENCIA: Llamamos al constructor de la clase padre
        super().__init__(nombre, edad, "Pájaro")
        self.__puede_volar = puede_volar  # ENCAPSULACIÓN: Atributo privado
    
    def puede_volar(self):
        """Retorna si el pájaro puede volar."""
        return self.__puede_volar
    
    # POLIMORFISMO: Sobrescritura del método hacer_sonido()
    def hacer_sonido(self):
        """
        Implementación específica para pájaros.
        POLIMORFISMO: Cada animal tiene su propio sonido.
        """
        return f"{self.get_nombre()} dice: ¡Pío pío!"
    
    # Método específico de la clase Pajaro
    def volar(self):
        """Comportamiento específico de los pájaros."""
        if self.__puede_volar:
            return f"{self.get_nombre()} vuela alto en el cielo"
        else:
            return f"{self.get_nombre()} no puede volar, pero camina feliz"


# ============================================================================
# FUNCIONES QUE DEMUESTRAN POLIMORFISMO
# ============================================================================

def hacer_sonar_animal(animal):
    """
    Función que demuestra POLIMORFISMO.
    
    Esta función puede recibir cualquier objeto que sea de tipo Animal
    (o sus clases derivadas) y llamará al método hacer_sonido() correspondiente.
    
    POLIMORFISMO: La función no necesita saber qué tipo específico de animal es,
    simplemente llama al método y cada clase ejecuta su propia implementación.
    
    Parámetros:
        animal (Animal): Cualquier instancia de Animal o sus clases derivadas
    """
    print(animal.hacer_sonido())


def presentar_animal(animal):
    """
    Función que demuestra POLIMORFISMO al aceptar diferentes tipos de animales.
    
    Parámetros:
        animal (Animal): Cualquier instancia de Animal o sus clases derivadas
    """
    print("\n" + "="*60)
    print(animal.mostrar_info())
    print(animal.hacer_sonido())
    
    # Comportamientos específicos según el tipo de animal
    if isinstance(animal, Perro):
        print(animal.traer_pelota())
    elif isinstance(animal, Gato):
        print(animal.ronronear())
    elif isinstance(animal, Pajaro):
        print(animal.volar())
    print("="*60)


# ============================================================================
# PROGRAMA PRINCIPAL - DEMOSTRACIÓN DE TODOS LOS CONCEPTOS
# ============================================================================

def main():
    """
    Función principal que ejecuta el programa y demuestra todos los conceptos de POO.
    """
    print("\n" + "PROGRAMA DE DEMOSTRACIÓN DE POO EN PYTHON".center(70))
    print("=" * 70)
    print("\nEste programa demuestra los siguientes conceptos:")
    print("✓ CLASES Y OBJETOS: Definición de clases e instanciación")
    print("✓ HERENCIA: Clases derivadas (Perro, Gato, Pajaro) heredan de Animal")
    print("✓ ENCAPSULACIÓN: Atributos privados con getters/setters")
    print("✓ POLIMORFISMO: Métodos sobrescritos y comportamiento polimórfico")
    print("=" * 70)
    
    # ========================================================================
    # CREACIÓN DE OBJETOS (INSTANCIAS DE LAS CLASES)
    # ========================================================================
    
    print("\n\nCREANDO OBJETOS (INSTANCIAS)...")
    print("-" * 70)
    
    # Creando instancias de Perro
    perro1 = Perro("Max", 3, "Labrador")
    perro2 = Perro("Luna", 2, "Husky")
    
    # Creando instancias de Gato
    gato1 = Gato("Whiskers", 4, "Naranja")
    gato2 = Gato("Shadow", 1, "Negro")
    
    # Creando instancias de Pajaro
    pajaro1 = Pajaro("Tweety", 1, True)
    pajaro2 = Pajaro("Pingu", 5, False)  # Un pingüino que no vuela
    
    print("✓ Se han creado 6 objetos: 2 perros, 2 gatos y 2 pájaros")
    
    # ========================================================================
    # DEMOSTRACIÓN DE ENCAPSULACIÓN
    # ========================================================================
    
    print("\n\nDEMOSTRANDO ENCAPSULACIÓN...")
    print("-" * 70)
    print("La encapsulación protege los datos usando atributos privados")
    print("y proporciona acceso controlado mediante getters/setters.\n")
    
    # Accediendo a atributos privados mediante getters
    print(f"Usando GETTER: El nombre del perro es '{perro1.get_nombre()}'")
    print(f"Usando GETTER: La edad del perro es {perro1.get_edad()} años")
    print(f"Usando GETTER: La raza del perro es {perro1.get_raza()}")
    
    # Modificando atributos mediante setters (con validación)
    print("\nUsando SETTER: Cambiando el nombre de 'Max' a 'Maximus'...")
    perro1.set_nombre("Maximus")
    print(f"Nuevo nombre: {perro1.get_nombre()}")
    
    print("\nIntentando establecer un nombre inválido (cadena vacía)...")
    perro1.set_nombre("")  # Esto mostrará un error de validación
    print(f"El nombre se mantiene como: {perro1.get_nombre()}")
    
    # ========================================================================
    # DEMOSTRACIÓN DE HERENCIA
    # ========================================================================
    
    print("\n\nDEMOSTRANDO HERENCIA...")
    print("-" * 70)
    print("Todas las clases (Perro, Gato, Pajaro) HEREDAN de la clase Animal.")
    print("Heredan sus atributos y métodos, pero pueden agregar funcionalidad propia.\n")
    
    # Los objetos heredados pueden usar métodos de la clase padre
    print("Métodos heredados de la clase Animal:")
    print(perro1.mostrar_info())
    print(perro1.comer())
    print(perro1.jugar())
    print(perro1.dormir())
    
    # ========================================================================
    # DEMOSTRACIÓN DE POLIMORFISMO
    # ========================================================================
    
    print("\n\nDEMOSTRANDO POLIMORFISMO...")
    print("-" * 70)
    print("El POLIMORFISMO permite que diferentes clases implementen el mismo método")
    print("de formas distintas. Observa cómo cada animal hace su propio sonido:\n")
    
    # Lista de animales de diferentes tipos
    animales = [perro1, perro2, gato1, gato2, pajaro1, pajaro2]
    
    # POLIMORFISMO: Llamamos al mismo método en diferentes tipos de objetos
    print("Llamando al método hacer_sonido() en cada animal:")
    for animal in animales:
        hacer_sonar_animal(animal)  # La función polimórfica
    
    # ========================================================================
    # DEMOSTRACIÓN INTERACTIVA COMPLETA
    # ========================================================================
    
    print("\n\nPRESENTACIÓN COMPLETA DE CADA ANIMAL...")
    print("-" * 70)
    
    # Presentamos cada animal usando la función polimórfica
    for animal in animales:
        presentar_animal(animal)
    
    # ========================================================================
    # DEMOSTRANDO INTERACCIONES Y ESTADOS
    # ========================================================================
    
    print("\n\nSIMULANDO ACTIVIDADES CON LOS ANIMALES...")
    print("-" * 70)
    
    print(f"\n{perro1.get_nombre()} va a jugar:")
    print(perro1.mostrar_info())
    print(perro1.jugar())
    print(perro1.jugar())
    print(perro1.mostrar_info())
    print("\n" + perro1.comer())
    print(perro1.mostrar_info())
    
    print(f"\n\n{gato1.get_nombre()} va a descansar:")
    print(gato1.mostrar_info())
    print(gato1.dormir())
    print(gato1.mostrar_info())
    
    # ========================================================================
    # RESUMEN FINAL
    # ========================================================================
    
    print("\n\n" + "=" * 70)
    print("RESUMEN DE CONCEPTOS DEMOSTRADOS".center(70))
    print("=" * 70)
    print("""
✓ CLASES Y OBJETOS:
  - Se definieron 4 clases: Animal (base), Perro, Gato, Pajaro (derivadas)
  - Se crearon 6 objetos (instancias) de diferentes tipos
  
✓ HERENCIA:
  - Perro, Gato y Pajaro heredan de la clase Animal
  - Heredan atributos (__nombre, __edad, __especie, __energia)
  - Heredan métodos (comer, dormir, jugar, mostrar_info)
  - Agregan sus propios atributos y métodos específicos
  
✓ ENCAPSULACIÓN:
  - Atributos privados (con __ al inicio)
  - Métodos getter para leer atributos: get_nombre(), get_edad(), etc.
  - Métodos setter para modificar atributos: set_nombre(), set_edad()
  - Validación de datos en los setters
  
✓ POLIMORFISMO:
  - Método hacer_sonido() sobrescrito en cada clase derivada
  - Funciones polimórficas: hacer_sonar_animal() y presentar_animal()
  - Mismo método, diferentes implementaciones según la clase
    """)
    print("=" * 70)
    print("PROGRAMA FINALIZADO CON ÉXITO".center(70))
    print("=" * 70 + "\n")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el script se ejecuta directamente
    (no cuando se importa como módulo).
    """
    main()
