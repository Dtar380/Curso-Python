# Condicionales

## ¿Qué son?
Como indica el nombre, las operaciones condicionales son un tipo se operacion que ejecuta bajo una condición dada. Entonces, tenemos una declaración de la condición en la que diríamos que condición tiene que cumplirse, y luego dentro de la condición, escribiríamos el código que queremos que se ejecute si esa condición se cumple.

## ¿Cómo se usan?
Una sentencia condicional en programación puede usarse de varias maneras, pero siempre con los bloques `if`{l=python},`elif`{l=python} y `else`{l=python}, if es la condición que se probara primero, si esta resulta no cumplirse se buscaria si hay otra condición en consecuencia de la anterior, para esto se usa `elif`{l=python} que es la contraccion de else y if, esto se repite hasta que se terminan los bloques `elif`{l=python} y entonces al final se ejecutaria si o si el bloque `else`{l=python} si es que lo hay.

Aquí un ejemplo con python de una sentencia condicional:
```{code-block} python
var = 1

if var == 2:
  # si la variable vale 2 ejecutar esto
elif var > 2:
  # si la variable vale mas que 2 ejecutar esto
else:
  # si ninguna de las condiciones anteriores se cumple ejecutar esto
```
