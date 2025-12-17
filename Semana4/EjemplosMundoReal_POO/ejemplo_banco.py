# Este programa modela un sistema bancario básico usando POO.
# Es parte de la tarea de la Semana 4 del curso de Programación Orientada a Objetos.

"""
En este archivo se implementa un ejemplo sencillo de POO.
La idea es representar cuentas bancarias y clientes de forma básica,
utilizando clases, atributos y métodos sin conceptos avanzados.
"""


class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria muy simple.
    Atributos principales:
    - titular: nombre del dueño de la cuenta (str)
    - numero_cuenta: identificador de la cuenta (str o int)
    - saldo: dinero disponible (float), inicia en 0.0
    """

    def __init__(self, titular: str, numero_cuenta):
        # Guardamos el nombre del titular y el número de cuenta
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        # El saldo comienza en 0.0 por defecto
        self.saldo = 0.0

    def depositar(self, cantidad: float):
        """
        Suma dinero al saldo de la cuenta.
        Si la cantidad es menor o igual a 0, se informa al usuario.
        """
        if cantidad is None:
            print("No se puede depositar un valor vacío.")
            return
        if cantidad <= 0:
            print("La cantidad a depositar debe ser mayor que 0.")
            return
        # Sumamos al saldo actual
        self.saldo += float(cantidad)
        print(f"Depósito exitoso de ${cantidad:.2f} en la cuenta {self.numero_cuenta}.")

    def retirar(self, cantidad: float):
        """
        Resta dinero del saldo de la cuenta, solo si hay suficiente.
        Si no hay fondos suficientes o la cantidad no es válida, se informa al usuario.
        """
        if cantidad is None:
            print("No se puede retirar un valor vacío.")
            return
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que 0.")
            return
        if cantidad > self.saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
            return
        # Restamos del saldo actual
        self.saldo -= float(cantidad)
        print(f"Retiro exitoso de ${cantidad:.2f} en la cuenta {self.numero_cuenta}.")

    def mostrar_saldo(self):
        """
        Muestra el saldo disponible en la cuenta.
        """
        print(f"Saldo actual de la cuenta {self.numero_cuenta} (Titular: {self.titular}): ${self.saldo:.2f}")


class Cliente:
    """
    Clase que representa a un cliente del banco.
    Atributos principales:
    - nombre: nombre del cliente (str)
    - edad: edad del cliente (int)
    - cuentas: lista de objetos CuentaBancaria que pertenecen al cliente
    """

    def __init__(self, nombre: str, edad: int):
        # Guardamos los datos básicos del cliente
        self.nombre = nombre
        self.edad = edad
        # El cliente puede tener varias cuentas, iniciamos con una lista vacía
        self.cuentas = []  # type: list[CuentaBancaria]

    def agregar_cuenta(self, cuenta: CuentaBancaria):
        """
        Agrega una cuenta bancaria a la lista de cuentas del cliente.
        """
        # Verificamos que lo que se intenta añadir sea una CuentaBancaria
        if not isinstance(cuenta, CuentaBancaria):
            print("Solo se pueden agregar objetos de tipo CuentaBancaria.")
            return
        self.cuentas.append(cuenta)
        print(f"Cuenta {cuenta.numero_cuenta} agregada al cliente {self.nombre}.")

    def mostrar_cuentas(self):
        """
        Muestra un resumen de todas las cuentas del cliente.
        """
        if len(self.cuentas) == 0:
            print(f"El cliente {self.nombre} no tiene cuentas registradas.")
            return

        print(f"\nCuentas del cliente {self.nombre}:")
        for idx, cuenta in enumerate(self.cuentas, start=1):
            print(f"  {idx}. Cuenta: {cuenta.numero_cuenta} | Titular: {cuenta.titular} | Saldo: ${cuenta.saldo:.2f}")


if __name__ == "__main__":
    # Ejemplo de uso simple del sistema bancario
    # 1) Creamos un cliente
    cliente1 = Cliente(nombre="Ana Pérez", edad=20)

    # 2) Creamos una cuenta bancaria para ese cliente
    cuenta_ahorros = CuentaBancaria(titular="Ana Pérez", numero_cuenta="0001-ABC")

    # 3) Asociamos la cuenta al cliente
    cliente1.agregar_cuenta(cuenta_ahorros)

    # 4) Mostramos las cuentas del cliente
    cliente1.mostrar_cuentas()

    # 5) Realizamos un depósito y luego un retiro
    cuenta_ahorros.depositar(150.0)  # Depositar $150.00
    cuenta_ahorros.retirar(40.0)     # Retirar $40.00

    # 6) Mostramos el saldo final
    cuenta_ahorros.mostrar_saldo()
