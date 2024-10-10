# Instalación
Antes de comenzar con el curso tendremos que comprobar si tenemos instalados los requisitos para el mismo, asi que eso es lo que haremos a continuación.<br>
Para toda esta parte necesitaremos disponer de una Terminal, en MAX esta se llama terminal, y en Windows depende, puede ser que la app Terminal este o no, en caso de que no estuviera abririamos el CMD (o Simbolo de Sistema), la manera mas rapida de abrirlo seria haciendo `win + r` y escribiendo dentro `powershell` o si el anterior no funcionara `cmd` y le daríamos al enter.
Una vez que tenemos la terminal abierta ya podemos empezar a comprobar todo.

## Python 3.12
En este curso vamos a estar usando la version de python 3.12

### Comprobar si esta instalada
Para comprobar si Python 3.12 esta instalado escribiremos en la terminal el comando `python --version`, y este nos tendrá que devolver una respuesta diciendo la version que esta instalada, y tendria que verse del modo `Python 3.12.X`.

### Instalar Python 3.12
En caso de que Python no estuviera instalado, en la misma terminal ejecutariamos el siguiente comando:
- En windows:
  - Primero instalamos python usando `winget install Python.Python.3.12`
  - Despues escribimos `set PATH=%PATH%;'%userprofile%\AppData\Local\Programs\Python\Python312'`
- En MAX:
  - Primero instalamos python usando `sudo apt install python3.12`
  - Despues escribimos `export PATH:"/usr/bin/python3$PATH"`

## VsCode
Para programar siempre necesitamos una herramienta en la que podamos escribir código de manera sencilla y nos pueda proporcionar ayudas a la hora de hacerlo, y yo personalmente recomiendo VsCode, asi que como es con lo que estoy mas familiarizado y es también el más común utilizaremos este editor de código.

### Comprobar si esta instalada
Para comprobar si VsCode esta instalado escribiremos en la terminal el comando `code --version`, y este nos tendrá que devolver la version que esta instalada, y el resultado seria algo como:
```
1.9X.X
Cadena de texto
x64 (o x32)
```

### Instalar VsCode
En caso de que VsCode no estuviera instalado, en la terminal ejecutariamos el siguiente comando:
- En Windows: `winget install Microsoft.VisualStudioCode`
- En MAX:
  - Primero usaremos el comando `sudo apt update`
  - Despues usaremos el comando `sudo apt install snapd`
  - Por ultimo instalaremos VsCode con el comando `sudo snap install --classic code`

## Fuente de texto
Iremos a [Nerd Fonts](https://www.nerdfonts.com/font-downloads) y elegiremos `Fira Code`.<br>
Una vez descargada iremos a la carpeta de descargas, extraeremos el archivo .zip y entraremos a la carpeta y abriremos he instalaremos todas las que se llamen `FiraCodeNerdFont-X.ttf`
