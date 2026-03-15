""" 
Factory Method es un patrón de diseño creacional que proporciona una interfaz para crear objetos en una superclase, mientras permite a las subclases alterar el tipo de objetos que se crearán
"""

from abc import ABC, abstractmethod

# Clase base
class Vehiculo(ABC):

    @abstractmethod
    def mostrar_caracteristicas(self):
        pass


# Clases concretas
class Automovil(Vehiculo):

    def mostrar_caracteristicas(self):
        print("Automóvil - Marca: Toyota, Modelo: Corolla, Velocidad Max: 180 km/h")


class Bicicleta(Vehiculo):

    def mostrar_caracteristicas(self):
        print("Bicicleta - Marca: Trek, Modelo: X-Caliber, Velocidad Max: 40 km/h")


class Motocicleta(Vehiculo):

    def mostrar_caracteristicas(self):
        print("Motocicleta - Marca: Yamaha, Modelo: R3, Velocidad Max: 200 km/h")


# Factory
class VehiculoFactory:

    @staticmethod
    def crear_vehiculo(tipo):

        if tipo == "auto":
            return Automovil()

        elif tipo == "bicicleta":
            return Bicicleta()

        elif tipo == "moto":
            return Motocicleta()

        else:
            return None


# Programa principal
v1 = VehiculoFactory.crear_vehiculo("auto")
v2 = VehiculoFactory.crear_vehiculo("bicicleta")
v3 = VehiculoFactory.crear_vehiculo("moto")

v1.mostrar_caracteristicas()
v2.mostrar_caracteristicas()
v3.mostrar_caracteristicas()