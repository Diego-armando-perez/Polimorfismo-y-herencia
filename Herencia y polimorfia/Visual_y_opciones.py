from Leon import Leon
from Mono import Mono
from Perro import Perro
from Pinguino import Pinguino


class Prueba:
    def __init__(self):
        self.mostrar_opciones()
        self.elegir_animal()
        
        
    def mostrar_opciones(self):
        print("Bienvenido a la prueba de animales, se tienen 4 animales que se pueden probar, porfavor eliga una opcion \n1- Perro \n2- Mono \n3- Leon \n4- Pinguino")
        
    def elegir_animal(self):
        self.eleccion = 0
        self.eleccion = int(input("Eliga su animal: "))
        if self.eleccion == 1:
            self.crear_perro()
        elif self.eleccion == 2:
            self.crear_mono()
        elif self.eleccion == 3:
            self.crear_leon()
        elif self.eleccion == 4:
            self.crear_pinguino()
            
                
    def crear_perro(self):
        self.perro1 = Perro(input("Eliga el nombre de su perro: "), 0, "Mamifero", input("Cual es el nombre del dueño?: "))
        self.opciones_perro()    
                    
    def opciones_perro(self):
        self.eleccion_perro = 0
        print(f"Usted a elegido al perro {self.perro1.nombre}, ahora porfavor seleccione una opcion para realizar \n1- Ladrar \n2- moverse \n3- Ver agresividad \n4- morder \n5- Dejar ir al perro")
        while self.eleccion_perro == 0:
            self.eleccion_perro = int(input("Eliga su opcion: "))
            if self.eleccion_perro == 1:
                self.perro1.hacer_sonido()
                self.eleccion_perro = 0
            elif self.eleccion_perro == 2:
                self.perro1.moverse()
                self.eleccion_perro = 0
            elif self.eleccion_perro == 3:
                self.perro1.mostrar_agresividad()
                self.eleccion_perro = 0
            elif self.eleccion_perro == 4:
                self.perro1.morder()
                self.eleccion_perro = 0
            if self.eleccion_perro == 5:
                print("El perro se aleja en el horizonte")
                
    def crear_mono(self):
        self.mono1 = Mono(input("Eliga el nombre del mono: "), 0, "Mamifero", input("Donde habita el mono?: "))
        self.opciones_mono()            
                
    def opciones_mono(self):
        self.eleccion_mono = 0
        print(f"Usted a elegido al mono {self.mono1.nombre}, ahora porfavor seleccione una opcion para realizar \n1- Gritar \n2- moverse \n3- Ver agresividad \n4- morder \n5- Revisar habitat \n6- Dejar ir al mono")
        while self.eleccion_mono == 0:
            self.eleccion_mono = int(input("Eliga su opcion: "))
            if self.eleccion_mono == 1:
                self.mono1.hacer_sonido()
                self.eleccion_mono = 0
            elif self.eleccion_mono == 2:
                self.mono1.moverse()
                self.eleccion_mono = 0
            elif self.eleccion_mono == 3:
                self.mono1.mostrar_agresividad()
                self.eleccion_mono = 0
            elif self.eleccion_mono == 4:
                self.mono1.morder()
                self.eleccion_mono = 0
            elif self.eleccion_mono == 5:
                self.mono1.revisar_habitat()
                self.eleccion_mono = 0
            if self.eleccion_mono == 6:
                print("El mono se aleja en por el arbol")
                
                
    def crear_leon(self):
        self.leon1 = Leon(input("Eliga el nombre del leon: "), 0, "Mamifero", input("Donde habita el leon?: "))
        self.opciones_leon()            
                
    def opciones_leon(self):
        self.eleccion_leon = 0
        print(f"Usted a elegido al leon {self.leon1.nombre}, ahora porfavor seleccione una opcion para realizar \n1- Rugir \n2- moverse \n3- Ver agresividad \n4- morder \n5- Revisar habitat \n6- Dejar ir al leon")
        while self.eleccion_leon == 0:
            self.eleccion_leon = int(input("Eliga su opcion: "))
            if self.eleccion_leon == 1:
                self.leon1.hacer_sonido()
                self.eleccion_leon = 0
            elif self.eleccion_leon == 2:
                self.leon1.moverse()
                self.eleccion_leon = 0
            elif self.eleccion_leon == 3:
                self.leon1.mostrar_agresividad()
                self.eleccion_leon = 0
            elif self.eleccion_leon == 4:
                self.leon1.morder()
                self.eleccion_leon = 0
            elif self.eleccion_leon == 5:
                self.leon1.revisar_habitat()
                self.eleccion_leon = 0
            if self.eleccion_leon == 6:
                print("El leon se aleja en por su habitat")            
                


    def crear_pinguino(self):
        self.pinguino1 = Pinguino(input("Eliga el nombre del pinguino: "), 0, "Mamifero", input("Donde habita el pinguino?: "))
        self.opciones_pinguino()            
                
    def opciones_pinguino(self):
        self.eleccion_pinguino = 0
        print(f"Usted a elegido al leon {self.pinguino1.nombre}, ahora porfavor seleccione una opcion para realizar \n1- Graznar \n2- moverse \n3- Ver agresividad \n4- morder \n5- Revisar habitat \n6- Dejar ir al pnguino")
        while self.eleccion_pinguino == 0:
            self.eleccion_pinguino = int(input("Eliga su opcion: "))
            if self.eleccion_pinguino == 1:
                self.pinguino1.hacer_sonido()
                self.eleccion_pinguino = 0
            elif self.eleccion_pinguino == 2:
                self.pinguino1.moverse()
                self.eleccion_pinguino = 0
            elif self.eleccion_pinguino == 3:
                self.pinguino1.mostrar_agresividad()
                self.eleccion_pinguino = 0
            elif self.eleccion_pinguino == 4:
                self.pinguino1.morder()
                self.eleccion_pinguino = 0
            elif self.eleccion_pinguino == 5:
                self.pinguino1.revisar_habitat()
                self.eleccion_pinguino = 0
            if self.eleccion_pinguino == 6:
                print("El punguino trata de volar, pero al final solo se va corriendo")