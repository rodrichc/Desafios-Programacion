"""1. Conversor de Monedas. Crea una clase Moneda que permita la conversión
   entre monedas (ej. dólares a pesos). Implementa los métodos __str__ y
   __add__ para mostrar la cantidad convertida y sumar cantidades en
 diferentes monedas."""


class Moneda:
    def __init__(self, dolares):
        self.dolares = float(dolares)
    
    def __str__(self):
        return f"Tu candidad de dolares es: {self.dolares} USD, equivalen a {round(self.dolares*1314.18, 2)} ARS"
    
    def __add__(self, cantidad):
        self.dolares += cantidad
        return Moneda(self.dolares)
    
cartera = Moneda(27.28)

print(cartera)

agregar_cartera = cartera + 12.37

print(agregar_cartera)
