from Animal import Animal


class Mono(Animal):
    def __init__(self, nombre, edad, especie, habitat):
        super().__init__(nombre, edad, especie)
        self.habitat = habitat

    def hacer_sonido(self):
        print ("UU-AA-UU-AA")

    def moverse(self):
        print("El mono escala un arbol con sus manos.")
    
    def mostrar_agresividad(self):
        print("El mono es extremadamente agresivo, 10/10.")

    def morder(self):
        print("El mono mordio a la persona que se le acerco demasiado")

    def revisar_habitat(self):
        print(f"El mono se encuentra viviendo en {self.habitat}")

