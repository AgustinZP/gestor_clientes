class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return "({self.dni}) {self.nombre} {self.apellido}"
    
class Clientes:

    lista = []

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
            
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                return cliente
            
    @staticmethod
    def borrar(dni):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                return Clientes.lista.pop(indice)