import sqlite3
import database

class Sqlite_db:

    def __init__(self):
        self.conexion = sqlite3.connect("gestor_clientes.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (dni varchar(3) PRIMARY KEY UNIQUE,
                    nombre varchar(30) NOT NULL,
                    apellido varchar(30) NOT NULL)
            ''')
        self.conexion.commit()
 
    def crear_cliente_sqlite(self, dni, nombre, apellido):
        try:
            self.cursor.execute("INSERT INTO clientes (dni, nombre, apellido) VALUES (?, ?, ?)", (dni, nombre, apellido))
            self.conexion.commit()
            print("Cliente dado de alta correctamente en base de datos.")
        except sqlite3.IntegrityError:
            print("El cliente ya existe o hubo un error con la base de datos.")
        finally:
            self.cerrar_conexion()

    def editar_cliente_sqlite(self, dni, nombre, apellido):
        try:
            self.cursor.execute("UPDATE clientes SET nombre = ?, apellido = ? WHERE dni = ?", (nombre, apellido, dni))
            self.conexion.commit()
            print("Cliente modificado correctamente en base de datos.")
        except sqlite3.IntegrityError:
            print("No se ha podido modificar el cliente o hubo un error con la base de datos.")
        finally:
            self.cerrar_conexion()

    def borrar_cliente_sqlite(self, dni):
        try:
            self.cursor.execute("DELETE FROM clientes WHERE dni = ?", (dni,))
            self.conexion.commit()
            print("Cliente borrado correctamente en base de datos.")
        except sqlite3.IntegrityError:
            print("No se ha podido borrar el cliente o hubo un error con la base de datos.")
        finally:
            self.cerrar_conexion()

    def cerrar_conexion(self):
        self.conexion.close()