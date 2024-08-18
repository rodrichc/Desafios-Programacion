"""
   3. Baraja de Cartas. Crea una clase Carta que represente una carta de la baraja.
Implementa los métodos __str__ y __getitem__ para mostrar la carta y
acceder a sus atributos (por ejemplo, palo y valor)
"""

class Carta:
   def __init__(self, valor, palo):
      self.valor = valor
      self.palo = palo

   def __str__(self):
      return f"Tu carta es: {self.valor} de {self.palo}"
   
   def __getitem__(self, item):
      carta = {"valor": self.valor, "palo": self.palo}
      return carta[item]
   

mi_carta = Carta(4, "Basto")

print(mi_carta)
print(mi_carta["valor"])
print(mi_carta["palo"])