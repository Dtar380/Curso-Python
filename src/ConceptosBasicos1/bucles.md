# Bucles

## ¿Qué son?
Como indica su nombre, un bucle es una parte del código que se repetirá. Hay dos tipos de bucles en programación, los bucles `while`{l=python} y los bucles `for`{l=python}, ambos comparten la propiedad de que el bucle tenga una duración determinada por una condición o variable, pero se tratan de manera diferente y su eficacia varia dependiendo de como se implementen.

## ¿Cómo se usan?
Un bucle se inicia declarando que tipo de bucle va a ser y seguido de la condición que se tiene que cumplir para que siga funcionando.

Aquí un ejemplo de bucle while con python:
```{code-block} python
var = 1

while var < 2:
  # Ejecutar bucle mientras que var sea menor que 2
```

En los bucles for en python no se usa una condición, si no una variable iterable, esto puede ser un string, una lista o un diccionario.<br>
Aquí un ejemplo de un bucle for con python:
```{code-block} python
var = ["a","b","c"]

for i in var:
  # Este código se ejecutara 3 veces y la i tendrá el valor del elemento de la lista en ese punto
```
