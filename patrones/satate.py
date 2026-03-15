"""
State es un patrón de diseño de comportamiento que permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara su clase.
"""

from abc import ABC, abstractmethod


class EstadoBombilla(ABC):

    @abstractmethod
    def presionar_interruptor(self, bombilla):
        pass


class Encendida(EstadoBombilla):

    def presionar_interruptor(self, bombilla):
        print("Apagando la bombilla...")
        bombilla.estado = Apagada()


class Apagada(EstadoBombilla):

    def presionar_interruptor(self, bombilla):
        print("Encendiendo la bombilla...")
        bombilla.estado = Encendida()


class Bombilla:

    def __init__(self):
        self.estado = Apagada()

    def presionar(self):
        self.estado.presionar_interruptor(self)


# Programa principal
bombilla = Bombilla()

bombilla.presionar()
bombilla.presionar()
bombilla.presionar()