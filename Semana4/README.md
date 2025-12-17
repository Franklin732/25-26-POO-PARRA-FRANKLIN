# Semana 4: Ejemplos del Mundo Real con POO

## 📋 Descripción

Este directorio contiene ejemplos prácticos de Programación Orientada a Objetos (POO) aplicados a situaciones del mundo real.

## 🏦 Sistema Bancario Básico

**Archivo:** `EjemplosMundoReal_POO/ejemplo_banco.py`

### Caso del Mundo Real
Sistema bancario simplificado que permite gestionar clientes y sus cuentas bancarias. Los clientes pueden tener múltiples cuentas y realizar operaciones básicas como depósitos y retiros.

### Clases Implementadas

#### `CuentaBancaria`
Representa una cuenta bancaria individual.
- **Atributos:**
  - `titular`: Nombre del dueño de la cuenta
  - `numero_cuenta`: Identificador único de la cuenta
  - `saldo`: Dinero disponible (inicia en 0.0)
  
- **Métodos:**
  - `depositar(cantidad)`: Agrega dinero al saldo
  - `retirar(cantidad)`: Retira dinero si hay fondos suficientes
  - `mostrar_saldo()`: Muestra el saldo actual

#### `Cliente`
Representa un cliente del banco.
- **Atributos:**
  - `nombre`: Nombre del cliente
  - `edad`: Edad del cliente
  - `cuentas`: Lista de cuentas bancarias del cliente
  
- **Métodos:**
  - `agregar_cuenta(cuenta)`: Asocia una cuenta al cliente
  - `mostrar_cuentas()`: Muestra todas las cuentas del cliente

## 🚀 Cómo ejecutar

```bash
python Semana4/EjemplosMundoReal_POO/ejemplo_banco.py
```

## 💡 Conceptos POO Aplicados

- ✅ **Clases y Objetos**: Modelado de entidades del mundo real
- ✅ **Atributos**: Características de cada objeto
- ✅ **Métodos**: Comportamientos y acciones
- ✅ **Encapsulamiento**: Datos y métodos organizados en clases
- ✅ **Interacción entre objetos**: Cliente gestiona múltiples CuentaBancaria

## 📚 Autor

Franklin Parra - Curso de Programación Orientada a Objetos
