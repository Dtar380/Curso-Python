# Modularización

## ¿Qué es?
La modularización es una de las claves fundamentales de python y por lo que es tremendamente exitoso, y que quiere decir, pues como su nombre indica, modularizar el código, es decir, dividirlo en pequeñas partes que se puedan reutilizar multiples veces para tener que repetir la minima cantidad de código posible (metodología DRY)<br>
Gracias al sistema de importación de python, podemos crear nuestros propios módulos muy fácilmente, lo que hace que podamos reutilizar todo nuestro código desde cualquier parte de nuestro proyecto y así ahorrandonos tiempo de trabajo y futuros quebraderos de cabeza intentando averiguar la solución para algo que ya resolvimos.

## ¿Cuándo y cómo usar?
La modularización se puede usar siempre, y de hecho es recomendable, y esto ya es preferencia personal, pero yo suelo seguir el método de 1C1F (1 class 1 file), que es una manera sencilla de mantener el código organizado y limpio.<br>
Para hacerlo es muy sencillo, simplemente tenemos que crear una carpeta con el nombre de nuestro modulo, y dentro creariamos un archivo llamado `__init__.py`, el árbol de nuestro código sería tal que así:
```
|--- main.py
|--- modulo /
     |--- __init__.py
     |--- main.py
```

Una vez creada esa estructura, dentro de nuestra carpeta podriamos añadir cualquier cosa que quisiéramos que el modulo tuviera, y para importarla se haria de la manera:
```{code-block} python
import modulo
```

o
```{code-block} python
from modulo.main import func
```
