# Variables y Constantes

## ¿Qué son?
Lo primero que se aprende al programar, siempre, es el uso de variables y constantes. Una variable es un dato o conjunto de datos que pueden variar, pueden ser alterados, una constante es un dato o conjunto de datos fijo, no puede variar.<br>
Cabe destacar que en Python no existen las constantes, solo las variables, pero hay una convención de nomenclatura, y es que para determinar que una variable se tiene que tratar como constante se tiene que declarar utilizando solo mayúsculas.

Aquí un ejemplo de declaraciones de variables y constantes:
```{code-block} python
variable1 = 12
variable2 = ['a','b','c']
CONSTANTE = 'Hola'
```

## ¿Cómo se usan?
Una variable o una constante se pueden utilizar para infinidad de cosas, al final es la forma que tiene un programa de guardar los datos que esta manejando, por lo que con las variables podemos jugar como queramos, podemos operar con ellas, re-declaralas, alterarlas y un largo etcetera.

Aquí unos ejemplos de operaciones con variables en python:
```{code-block} python
var1 = 1
var2 = 2

var1 + var2
>>> 3
```
```{code-block} python
var1 = 'hello'
var2 = 'world'

var1 + var2
>>> 'hello world'
```
```{code-block} python
var = [2] * 4
>>> [2,2,2,2]
```

## Tipos de variables
Como habréis visto en el ultimo ejemplo, ahi cada variable, detrás del igual tienen cosas distintas, eso es por que las variables tienen distintos tipos.
Los tipos mas comunes de variables son:
- integer: Numero entero
- float: Numero de coma flotante (decimal)
- string: Texto
- boolean: Valor booleano (verdadero o falso)
- list: Lista de elementos, la cual puede contener en su interior cualquiera de las anteriores
- dictionary: Lista de elementos organizada por claves

En python estos tipos de variables se usan de la siguiente manera:
```{code-block} python
entero: int = 1
decimal: float = 2.1
string: str = 'abc'
booleano: bool = False
lista: list = ['a', 1, True]
diccionario: dict = {
  "clave1": "valor1",
  "clave2": 2
}
```

En este ejemplo se puede ver algo diferente al primero, y es el uso de la notacion `name: type`{l=python}, eso es algo opcional, pero que se usa a menudo para saber de que tipo es cada variable, asi también veis como se llama cada tipo dentro de python.

Aquí entran en juego también nuevas funciones con respecto a los tipos de variables:
- int
- float:
  - round(): redondea un numero al numero de decimales especificado
- [str](https://www.w3schools.com/python/python_ref_string.asp)
- bool
- [list](https://www.w3schools.com/python/python_ref_list.asp)
- [dict](https://www.w3schools.com/python/python_ref_dictionary.asp)

Todos los tipos de variables comparten una funcion y esa es:
`tipo_de_variable()`{l=python}
Esta función transforma una variable en su homologa en el tipo especificado, por ejemplo:
```{code-block} python
var: float = 1.6
int(var)
>>> 1
```
