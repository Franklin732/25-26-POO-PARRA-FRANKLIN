# Solución con Programación Tradicional (Estructurada)
# Este programa calcula el promedio de temperaturas de una semana

# Función para ingresar las temperaturas del usuario
def ingresar_temperaturas():
    """
    Pide al usuario que ingrese 7 temperaturas diarias.
    Retorna una lista con las temperaturas.
    """
    temperaturas = []
    
    print("=== Ingreso de Temperaturas Semanales ===")
    print("Por favor, ingresa la temperatura de cada día (en °C):\n")
    
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingresa un número válido.")
    
    return temperaturas


# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio con dos decimales.
    """
    suma = sum(temperaturas)
    cantidad = len(temperaturas)
    promedio = suma / cantidad
    
    return promedio


# Función para mostrar el resultado
def mostrar_resultado(promedio):
    """
    Muestra el promedio de temperaturas de forma formateada.
    """
    print("\n=== Resultado ===")
    print(f"Promedio de temperaturas semanal: {promedio:.2f}°C")


# Función principal que coordina todo el flujo
def main():
    """
    Función principal que controla el flujo del programa.
    Coordina la entrada de datos, cálculo y salida.
    """
    # Obtener las temperaturas del usuario
    temperaturas = ingresar_temperaturas()
    
    # Calcular el promedio
    promedio = calcular_promedio(temperaturas)
    
    # Mostrar el resultado
    mostrar_resultado(promedio)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
