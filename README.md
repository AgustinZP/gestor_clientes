
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


