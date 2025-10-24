from Animal import Animal


class Pinguino(Animal):
    def __init__(self, nombre, edad, especie, habitat):
        super().__init__(nombre, edad, especie)
        self.habitat = habitat

    def hacer_sonido(self):
        print ("SQUAWK SQUAWK")

    def moverse(self):
        print("El pinguino camina lentamente con sus dos patas")
    
    def mostrar_agresividad(self):
        print("Que lindo pinguino!, su agresividad es de 0/10.")

    def morder(self):
        print("El pinguino no muerde, es muy amigable")

    def revisar_habitat(self):
        print(f"El pinguino se encuentra en {self.habitat}")

