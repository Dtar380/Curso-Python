# Configuración
Una vez que ya esta todo instalado, todavía no estamos listos, tenemos que preparar nuestro espacio de trabajo para poder trabajar lo mas fluido posible.<br>
Ahora abrimos VsCode, y lo primero que sale es la pantalla de la ayuda a la configuración, pero le vamos a dar a `Mark Done` abajo a la izquierda, ya que no queremos seguir el tutorial proporcionado por el editor por que no es suficientemente completo.

## Extensiones
Para poder sacarle todo el partido a VsCode vamos a hacer uso de su ecosistema de extensiones, asi que pulsaremos `ctrl+shift+x` para abrir el panel de extensiones.

Una vez abierto instalaremos las siguientes extensiones:
- Better Comments
- Error Lens
- IntelliCode
- Python
- PyLint
- MyPy
- Spanish Language Pack
- Toggle Excluded Files

## Apariencia
Ahora en el mismo panel de extensiones buscaremos las siguientes extensiones:
- Material Icon Theme
- Material Product Icons
Al instalarse estas extensiones saldrá una opción en la parte central superior de la pantalla, darle al enter, es para establecer el tema de la extension como la por defecto.

Despues de instalar estas dos extensiones usaremos el atajo `ctrl+n`, una vez dentro del nuevo archivo haremos `ctrl+k m` y buscaremos en la barra que nos sale `Python`, y lo seleccionamos.
Ahora copiareis el siguiente código a este nuevo archivo:
```{code-block} python
def main(name: str):
    print(f"Hello {name}!")

if __name__ == "__main__":
    main("Algo")
```
Una vez copiado el código al archivo nuevo usaremos `ctrl+k ctrl+t`, y aquí se nos abrirá una pantalla de selección del tema del editor de código, seleccionaremos examinar temas de color adicionales, y en esta nueva selección podemos movernos con las flechas y los colores del editor van a ir cambiando, añadido a eso, también podemos buscar temas por nombre que no aparezcan en esta lista, mi favorito es One Dark Pro Flat de binaryify, y también puedo recomendaros Catppuccin hechos por Catppuccin, todo esto ya es preferencia personal y aquí podéis elegir el que mas os guste.

## Configuración
Una vez que ya hemos instalado las extensiones que necesitamos y hemos cambiado la apariencia de VsCode a nuestro gusto podemos empezar a tocar la configuración.<br>
Para abrir la configuración usaremos el atajo `ctrl+,`, ahora se nos abrirá una pagina con todas las opciones, pero vamos a pasar de esta pagina y vamos a hacer click en la rueda que sale arriba a la derecha, eso nos abrirá el archivo de configuración.<br>
Aquí dentro deberia haber muy pocas cosas, todo lo que haya probablemente se quede igual, asi que no vamos a tocar nada de lo existente, pero si vamos a añadir, y empezaremos por añadir lo siguiente:
```{code-block} json
  "workbench.settings.editor": "json",
```
Esto hara que ahora cuando hagamos uso de `ctrl+,` se habra directamente el archivo de configuración en vez de la pagina.<br>

Ahora os dejo aquí todas las configuraciones mas importantes de vscode con una corta descripción para copiar y pegar las que queráis, recordar que siempre podeis copiarla y cambiar los el parametro un poco.<br><br>

```{note} Nota
Las siguiente configuración es obligatoria
```

Obligatorio:
```{code-block} json
  // *** FONT ***

  // Font family
  "editor.fontFamily": "FiraCode Nerd Font",
  "scm.inputFontFamily": "FiraCode Nerd Font",
  "terminal.integrated.fontFamily": "FiraCode Nerd Font",
  "chat.editor.fontFamily": "FiraCode Nerd Font",
  "debug.console.fontFamily": "FiraCode Nerd Font",
  "editor.codeLensFontFamily": "FiraCode Nerd Font",
  "notebook.output.fontFamily": "FiraCode Nerd Font",
  "markdown.preview.fontFamily": "FiraCode Nerd Font",
  "editor.inlayHints.fontFamily": "FiraCode Nerd Font",
  "editor.inlineSuggest.fontFamily": "FiraCode Nerd Font",
  "errorLens.fontFamily": "FiraCode Nerd Font",
  "apc.font.family": "FiraCode Nerd Font",
  "apc.monospace.font.family": "FiraCode Nerd Font",

  "editor.fontLigatures": true,
  "editor.fontVariations": true,

  // Font size
  "editor.fontSize": 13,
  "editor.fontWeight": "100",
  "terminal.integrated.fontSize": 13,
  "terminal.integrated.fontWeight": "100",
  "terminal.integrated.lineHeight": 1.2,

  // *** FILES ***

  // Saving
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.trimFinalNewlines": true,

  // Toggle excluded files
  "files.exclude": {
    "**/.git": false,
    "**/.gitignore": false,
    "**/.github": false,
    "**/.gitattributes": false,
    "**/.svn": false,
    "**/.hg": false,
    "**/CVS": false,
    "**/.DS_Store": false,
    "**/Thumbs.db": false,
    "**/.vscode": false,
    "**/dist": false,
    "**/.todo.md": false,
    "**/.secrets": false,
    "**/cspell.json": false,
    "**/LICENSE": false,
    "**/.venv": false,
    "**/*.pyc": false,
    "**/__pycache__": false,
    "**/.mypy_cache": false,
    "**/*.egg-info": false
  },

  // *** IDENTATION ***

  // Default identation
  "editor.detectIndentation": true,
  "editor.tabSize": 4,
  "prettier.tabWidth": 4,
  "editor.indentSize": "tabSize",

  "[json]": {
    "editor.tabSize": 2,
    "prettier.tabWidth": 2,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // *** ERROR LENS ***
  "codeium.enableCodeLens": false,
  "errorLens.enabledDiagnosticLevels": [
    "error",
    "warning"
  ],
```
<br>

Opcional:
```{code-block} json
  // *** APPEARANCE ***

  // Editor
  "window.commandCenter": false, // Busqueda central
  "window.zoomLevel": 0.10, // Zoom de la ventana
  "breadcrumbs.enabled": false, // Los breadcrumbs nos dicen en que profundidad nos encontramos dentro del código

  "workbench.editor.enablePreview": false, // Si se activa, al abrir un archivo se abrirá en formato preview
  "workbench.editor.showTabs": "single", // Cuantos Tabs se muestran (cada Tab es un archivo que tengamos abierto)
  "workbench.activityBar.location": "hidden", // La barra de actividades es la que tiene los iconos grandes
  "workbench.sideBar.location": "right", // Esta es la barra que contiene el árbol de archivos

  "editor.rulers": [90], // Se trazara una fina linea en el editor a la distancia de los caracteres especificados
  "editor.stickyScroll.enabled": true, // Si se activa, se quedara arriba del todo al hacer scroll en un archivo la ultima keyword usada
  "editor.glyphMargin": false, // Una parte del gutter (zona donde se ven las lineas numeradas del código) podran colorearse
  "editor.bracketPairColorization.enabled": true, // Hace que los brackets y parentesis vayan cambiando de color a medida que se apilan
  "editor.guides.bracketPairs": true, // Hace que se vea resaltado el donde empieza y acaba el bracket o parentesis
  "editor.hover.delay": 1500, // Tiempo en milisegundos que tardara en salir la información de algo por lo que pasamos el cursor por encima
  "editor.hover.enabled": true, // Habilita el hover
  "editor.minimap.enabled": false, // Deshabilita el minimapa del código que sale al lado de la barra de scroll
  "editor.scrollbar.vertical": "hidden", // Deshabilita la barra de scroll
  "editor.overviewRulerBorder": false, // Quita el borde que hay entre la barra de scroll y el editor
  "editor.hideCursorInOverviewRuler": false, // Habilita la visibilidad del cursor al pasar por encima del barra de scroll
  "editor.scrollbar.horizontal": "hidden", // Deshabilita la barra de scroll horizontal

  // Cursor
  "editor.cursorBlinking": "smooth", // Tipo de parpadeo del cursor
  "editor.cursorSmoothCaretAnimation": "on", // Animacion del cursor para cuando lo movemos de linea
  "editor.cursorWidth": 2, // Ancho del cursor

  "terminal.integrated.cursorBlinking": true, // Parpadeo del cursor en la terminal
  "terminal.integrated.cursorStyle": "line", // Tipo de cursor en la terminal
  "terminal.integrated.cursorWidth": 2, // Ancho del cursor en la terminal
  "terminal.integrated.cursorStyleInactive": "none", // Estilo del cursor cuando la terminal no esta seleccionada
```

## Atajos de teclado
Una vez que hemos acabado de configurar el editor, vamos a crear unos atajos de teclado extras, para ello, tenemos primero que abrir el archivo con los ajustes de los atajos de teclado usando `ctrl+shift+p` y escribiremos `Open Keyboard Sortcuts (JSON)`, y una vez aquí, podemos empezar a añadir los atajos de teclado que queramos.

Estos son los atajos de teclado que vamos a usar:
```{code-block} json
  // Open keybindings
  {
    "key": "ctrl+k ctrl+s",
    "command": "workbench.action.openGlobalKeybindingsFile",
  },
  // Switch profile
  {
    "key": "ctrl+s p",
    "command": "workbench.profiles.actions.switchProfile",
    "when": "profiles.enabled"
  },
  // Auto focus file explorer when opening it
  {
    "key": "ctrl+shift+e",
    "command": "workbench.action.toggleSidebarVisibility",
  },
  {
    "key": "ctrl+shift+e",
    "command": "workbench.files.action.focusFilesExplorer",
    "when": "editorTextFocus"
  },
  // Toggle hidden files
  {
    "key": "ctrl+s f",
    "command": "toggleexcludedfiles.toggle",
    "when": "!inputFocus"
  },
  // File explorer extras
  {
    "key": "n",
    "command": "explorer.newFile",
    "when": "filesExplorerFocus && !inputFocus"
  },
  {
    "key": "d",
    "command": "deleteFile",
    "when": "filesExplorerFocus && !inputFocus"
  },
  {
    "key": "r",
    "command": "renameFile",
    "when": "filesExplorerFocus && !inputFocus"
  },
  {
    "key": "c",
    "command": "filesExplorer.copy",
    "when": "filesExplorerFocus && !inputFocus"
  },
  {
    "key": "p",
    "command": "filesExplorer.paste",
    "when": "filesExplorerFocus && !inputFocus"
  }
```
