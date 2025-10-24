from Animal import Animal


class Perro(Animal):
    def __init__(self, nombre, edad, especie, dueño):
        super().__init__(nombre, edad, especie)
        self.dueño = dueño

    def hacer_sonido(self):
        print ("Wan wan...")

    def moverse(self):
        print("Lentamente en cuatro patas el perro se mueve en el pasto.")
    
    def mostrar_agresividad(self):
        print("El perro tiene una agresividad de 3/10.")

    def morder(self):
        print(f"El perro se encuentra mordiendo a {self.dueño} de forma juguetona")

