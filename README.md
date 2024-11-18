# Sopa de Letras - Buscador de Palabras
### AUTOR:  JUAN DAVID TABARES PEREZ
## Descripción

Este proyecto consiste en una implementación de un programa para buscar palabras dentro de una sopa de letras, en general, el programa lee un archivo .txt que contiene la sopa de letras y una lista de palabras a buscar, luego, verifica si esas palabras se encuentran en la sopa en varias direcciones, de izquierda a derecha, de derecha a izquierda, de arriba hacia abajo, de abajo hacia arriba, y en las diagonales.

Al Final, genera un reporte en formato `.json` que indica si cada palabra fue encontrada o no.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- **`main.py`**: El archivo principal que gestiona la entrada de datos, invoca las funciones de búsqueda y genera el reporte en formato `.json`.
- **`functions.py`**: Contiene funciones que ayudan a generar el reporte de palabras encontradas.
- **`soup_funcions.py`**: Contiene las funciones que buscan palabras en la sopa de letras en diferentes direcciones.
- **`input.txt`**: Archivo de texto de entrada donde se almacenan la sopa de letras y las palabras a buscar.
- **`report.json`**: Archivo de salida donde se almacenan los resultados de la búsqueda.
- **`file_operation.py`**: Lee el archivo input.txt y separa la sopa de letras y las palabras a buscar.
- **`requirements.txt`**: Son los requerimientos que se deben de instalar para poder correr correctamente el programa.
## Requisitos

- Python 3
- No se requieren dependencias adicionales.

## Instalación

Para instalar y ejecutar el proyecto, se debe tener Python 3 instalado, luego, se sigue estos pasos:

1. Clonar este repositorio o descargar los archivos.
   
2. Coloca el archivo `input.txt` en la misma carpeta que los archivos del proyecto.

3. Ejecuta el archivo `main.py` en la terminal o línea de comandos con el siguiente comando:

   ```bash
   python main.py
