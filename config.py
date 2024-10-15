import os
import sys

# Obtener el path del archivo .csv
def resource_path(relative_path):
    """ Devuelve la ruta absoluta al archivo `archivo.csv`, considerando si el programa está empaquetado o no """
    try:
        # Si el programa está empaquetado con PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Si el programa está en modo desarrollo sin empaquetar
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Usar la función para el archivo .csv
DATABASE_PATH = resource_path(os.path.join('res', 'clientes.csv'))


# DATABASE_PATH = "clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"