from Animal import Animal
import random

class Leon(Animal):
    def __init__(self, nombre, edad, especie, habitat):
        super().__init__(nombre, edad, especie)
        self.habitat = habitat

    def hacer_sonido(self):
        print ("Rawr")

    def moverse(self):
        print("El leon corre al rededor buscando una presa en 4 patas")
    
    def mostrar_agresividad(self):
        print("El leon esta domesticado por lo que no es tan agresivo, 5/10.")

    def morder(self):
        x = random.randint(1,10)
        if x > 5:
            print("El leon ha mordido muy fuertemente, ouch")
        else:
            print("El leon muerde amigablemente")

    def revisar_habitat(self):
        print(f"El leon corre libremente en {self.habitat}")

