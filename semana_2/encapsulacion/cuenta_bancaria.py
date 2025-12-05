# TÉCNICA: ENCAPSULACIÓN
# La encapsulación nos permite proteger los datos de una clase
# para que no puedan ser modificados directamente desde fuera
class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria básica.
    
    La encapsulación protege el saldo de la cuenta para que solo pueda ser modificado
    a través de los métodos depositar() y retirar(), evitando que se pueda cambiar
    el saldo de forma incorrecta desde fuera de la clase.
    """
    
    def __init__(self):
        """
        Constructor que inicializa una cuenta bancaria.
        
        El saldo comienza en 0 y se marca como privado usando '__' al inicio del nombre.
        Esto significa que no se puede acceder directamente desde fuera de la clase.
        """
        self.__saldo = 0  # El doble guion bajo (__) hace que el atributo sea privado

    @property
    def saldo(self):
        """
        Propiedad que permite consultar el saldo de forma segura.
        
        Aunque el saldo es privado, esta propiedad permite que otros puedan
        VER el saldo, pero NO modificarlo directamente.
        Es como una ventana de solo lectura.
        """
        return self.__saldo

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta.
        
        Args:
            monto: Cantidad de dinero a depositar (debe ser positiva)
            
        Este método valida que el monto sea positivo antes de agregarlo al saldo.
        Es la ÚNICA forma correcta de aumentar el saldo de la cuenta.
        """
        if monto > 0:
            self.__saldo += monto
        else:
            print("Error: El monto debe ser positivo.")

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta.
        
        Args:
            monto: Cantidad de dinero a retirar
            
        Returns:
            True si el retiro fue exitoso, False si no había suficiente dinero
            
        Este método verifica que haya suficiente dinero antes de permitir el retiro.
        Es la ÚNICA forma correcta de disminuir el saldo de la cuenta.
        """
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            return True
        print("Error: Fondos insuficientes o monto inválido.")
        return False
