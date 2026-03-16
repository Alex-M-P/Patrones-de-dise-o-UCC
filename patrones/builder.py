"""
Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. 
El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.
"""

class Pizza:

    def __init__(self):
        self.tamano = None
        self.ingredientes = []

    def mostrar_pizza(self):
        print("Tamaño:", self.tamano)
        print("Ingredientes:", ", ".join(self.ingredientes))


class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()

    def agregar_tamano(self, tamano):
        self.pizza.tamano = tamano
        return self

    def agregar_ingrediente(self, ingrediente):
        self.pizza.ingredientes.append(ingrediente)
        return self

    def construir(self):
        return self.pizza


# Programa principal
builder = PizzaBuilder()

pizza = (
    builder
    .agregar_tamano("Grande")
    .agregar_ingrediente("Queso")
    .agregar_ingrediente("Pepperoni")
    .agregar_ingrediente("Champiñones")
    .construir()
)

pizza.mostrar_pizza()
