# Excepciones

## ¿Qué son?
Como bien indica su nombre, una excepción es una parte del código que se ejecuta al surgir una excepción. Este tipo de condicionales se usan principalmente para sortear los errores en el código sin tener que arreglarlo, ya sea por que es imposible de arreglar, o sea a proposito o no tengamos tiempo para resolverlo en ese momento.

## ¿Cómo se usan?
Como mencionado anteriormente, se usan como una condicional, pero al ser una condicional que puede manejar errores (cosa que el IF no puede) se usa otra palabra, en python estas son `try`{l=python}, `except`{l=python} y `else`{l=python}.

Aquí un ejemplo de un try, except para capturar un error de tipado:
```{code-block} python
i = "100"

try:
  print(i/100)
except TypeError:
  print("No se puede dividir un string")
```
