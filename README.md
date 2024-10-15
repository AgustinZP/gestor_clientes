# Aplicación de Gestión de Clientes

## Descripción

Esta aplicación de escritorio está diseñada para la gestión de clientes, permitiendo a los usuarios dar de alta, editar o borrar clientes de manera sencilla. La aplicación almacena los datos de los clientes tanto en un archivo CSV como en una base de datos SQLite, asegurando que la información esté organizada y accesible.

## Funcionalidades

- **Alta de Clientes**: Permite agregar nuevos clientes a la base de datos y al archivo CSV.
- **Edición de Clientes**: Posibilidad de modificar la información de clientes existentes.
- **Borrado de Clientes**: Opción para eliminar clientes de la base de datos y del archivo CSV.
- **Validación de Datos**: A medida que el usuario completa los formularios, se valida que los datos introducidos cumplan con el formato y longitud correctos. 
  - Si un campo contiene datos incorrectos, el fondo del campo de entrada se vuelve rojo.
  - Si los datos son correctos, el fondo se vuelve verde.
- **Inactivación de Botones**: Los botones de crear y modificar permanecen inactivos hasta que todos los campos requeridos están correctamente llenos.
  
## Requisitos

- Python 3.11.4
- Bibliotecas: `tkinter`, `sqlite3`, `csv`, `os`, `platform`, `re`

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/tu-usuario/gestion-clientes.git
    cd gestion-clientes
    ```

2. Instala las dependencias necesarias si deseas ejecutar el código desde el entorno Python:
    ```bash
    pip install tk
    ```

3. Ejecuta la aplicación directamente con Python:
    ```bash
    python gestor_clientes.py
    ```

## Ejecutable para Windows

Si prefieres no trabajar con el entorno Python, puedes utilizar el **ejecutable para Windows** que ya he generado. No necesitas instalar Python ni las bibliotecas requeridas para utilizar la aplicación.

1. Descarga el ejecutable desde el siguiente enlace: [Descargar Ejecutable](https://github.com/AgustinZP/gestor_clientes/tree/main/dist)
2. Descomprime el archivo descargado.
3. Ejecuta `gestor_clientes.exe` para iniciar la aplicación.

## Uso

Una vez que ejecutes la aplicación, podrás:

- **Añadir Clientes**: Rellena los campos del formulario y pulsa el botón "Crear" para agregar un nuevo cliente.
- **Editar Clientes**: Selecciona un cliente de la lista, modifica los datos y pulsa "Modificar".
- **Eliminar Clientes**: Selecciona un cliente de la lista y pulsa "Borrar" para eliminarlo de la base de datos y el archivo CSV.

La información se guarda automáticamente tanto en la base de datos SQLite como en un archivo CSV.

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.11.4
- **GUI**: Tkinter
- **Almacenamiento**: SQLite y CSV
- **Ejecutable**: PyInstaller para la creación de la versión ejecutable de Windows

## Autor

Desarrollado por Agustín Zaragoza Pérez - [agusdev.es](https://www.agusdev.es)
