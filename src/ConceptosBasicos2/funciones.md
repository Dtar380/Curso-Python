# Funciones

## ¿Qué son?
Una función es un trozo de código que se define en un punto de nuestro programa para poder usarlo mas adelante en el mismo. Las funciones no ayudan a no tener que escribir la misma funcionalidad del código dos veces si la vamos a reutilizar.<br>

## ¿Cómo se usan?
Una función cuando es declarada se le asigna un nombre y unos parametros que podrá usar dentro de la misma. Cuando posteriormente se llame a la función, se le tendran que pasar los parametros obligatorios. Una función puede simplemente ejecutar código, pero también puede devolver un valor.

Aquí un ejemplo de una función en python:
```{code-block} python
def func(obligatorio: int, opcional: str = '') -> list:
    return [opcional] * obligatorio

func(2)
>>> ['','']

func(3, 'abc')
>>> ['abc','abc','abc']
```
