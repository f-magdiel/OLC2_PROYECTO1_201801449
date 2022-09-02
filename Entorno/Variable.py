class Variable:
    def __init__(self, tipo, nombre, valor, linea, mutable, capacidad=None):
        self.tipo = tipo
        self.nombre = nombre
        self.valor = valor
        self.linea = linea
        self.mutable = mutable
        self.capacidad = capacidad
