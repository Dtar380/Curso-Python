# Clases y Objetos

## ¿Qué son?
Un objeto es un componente del código que posee sus atributos y metodos unicos y una clase es un constructor de objetos, es decir, es lo que vamos a utilizar para crear objetos del mismo tipo.<br>
Para ejemplificar un poco con cosas que nos rodean, un objeto podria ser cualquier cosa, por ejemplo, un coche, tiene sus atributos como puedan ser el tamaño, la potencia, el color etc, y unos metodos, en este caso funciones, que seria desplazarse. La clase en este ejemplo podria ser la clase Coche, aunque esto podria ser a su vez una sub clase de Vehículo Automotriz (Aunque no vamos a dar herencias en este curso).<br>

## ¿Cómo se usan?
Las clases y los objetos en python (y en muchos otros lenguajes) es en lo que se basan las variables que hemos estado creando todo este tiempo. Un int seria un objeto creado por la clase int, que tiene sus atributos (en este caso solo uno que seria el valor) y sus metodos, la suma, la multiplicación, la resta, etc.<br>
En python para crear una clase se hace de la siguiente manera:
```{code-block} python
class Coche:

    def __init__(self, color: str, potencia: int, par: int) -> None:
        self.color = color
        self.potencia = potencia
        self.par = par

    def pintar(self, new_color: str) -> None:
        self.color = new_color
```

Para crear un objeto y utilizarlo lo hariamos de la siguiente manera:
```{code-block} python
coche1 = Coche(color="azul", potencia=50, par=150)
coche1.pintar(new_color="rojo")
```
