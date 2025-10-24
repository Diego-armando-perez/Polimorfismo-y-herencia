class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def hacer_sonido(self):
        pass
    
    def moverse(self):
        pass

    def mostrar_agresividad(self):
        pass

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad 