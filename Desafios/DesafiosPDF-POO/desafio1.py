"""Desafío: Intenta crear una clase "Dado" que cumpla los siguientes requerimientos:
                - El dado debe tener un número de caras (por defecto 6).
                - Debe ser capaz de lanzarse y devolver un número aleatorio entre 1 el número de caras.
"""
import random

class Dado:
    def __init__(self, numero_caras):
        self.caras = numero_caras
    
    def tirarDado(self):
        resultado = random.randint(1, self.caras)
        return resultado
    
mi_dado = Dado(6)

resultado = mi_dado.tirarDado()

print(resultado)