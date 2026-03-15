"""
Strategy es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.

O sea, un familia de problemas tiene varas soluciones que se adecuan a diferentes situaciones o circunstancias
ejemplo: el calculo de área de figuras geometricas.
"""

from abc import ABC, abstractmethod
import math

# Estrategia
class AreaStrategy(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


# Estrategia concreta 1
class AreaCirculo(AreaStrategy):

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2


# Estrategia concreta 2
class AreaCuadrado(AreaStrategy):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


# Contexto
class CalculadoraArea:

    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self):
        return self.estrategia.calcular_area()


# Programa principal
circulo = CalculadoraArea(AreaCirculo(5))
cuadrado = CalculadoraArea(AreaCuadrado(4))

print("Área del círculo:", circulo.calcular())
print("Área del cuadrado:", cuadrado.calcular())
