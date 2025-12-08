# Solución con Programación Orientada a Objetos (POO)
# Este programa calcula el promedio de temperaturas de una semana

class ClimaSemanal:
    """
    Clase que representa el clima de una semana.
    Gestiona el ingreso, almacenamiento y cálculo de temperaturas.
    """
    
    def __init__(self):
        """
        Inicializa la clase con una lista vacía para almacenar temperaturas.
        """
        # Atributo privado para almacenar las 7 temperaturas diarias
        self.__temperaturas = []
    
    
    def ingresar_temperaturas(self):
        """
        Método que pide al usuario las temperaturas de cada día de la semana.
        Valida que los valores ingresados sean números.
        """
        print("=== Ingreso de Temperaturas Semanales ===")
        print("Por favor, ingresa la temperatura de cada día (en °C):\n")
        
        for dia in range(1, 8):
            while True:
                try:
                    temp = float(input(f"Día {dia}: "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Error: Ingresa un número válido.")
    
    
    def calcular_promedio(self):
        """
        Calcula el promedio semanal de temperaturas.
        Retorna el promedio con dos decimales.
        """
        if len(self.__temperaturas) == 0:
            return 0.0
        
        suma = sum(self.__temperaturas)
        cantidad = len(self.__temperaturas)
        promedio = suma / cantidad
        
        return promedio
    
    
    def mostrar_resultado(self):
        """
        Muestra el promedio de temperaturas de forma formateada.
        """
        promedio = self.calcular_promedio()
        
        print("\n=== Resultado ===")
        print(f"Promedio de temperaturas semanal: {promedio:.2f}°C")


# Función principal que gestiona la ejecución del programa
def main():
    """
    Función principal que crea una instancia de ClimaSemanal
    y coordina el flujo del programa.
    """
    # Crear una instancia de la clase ClimaSemanal
    clima = ClimaSemanal()
    
    # Ingresar las temperaturas
    clima.ingresar_temperaturas()
    
    # Mostrar el resultado
    clima.mostrar_resultado()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
