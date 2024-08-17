"""
2. Área y Perímetro. Crea una clase Rectángulo que permita calcular su área y su
perímetro. Además, crea en una aplicación de consola que permita al usuario crear
un objeto Perímetro y realizar los cálculos.

"""

class Rectangulo:
    def __init__(self, base, altura):
         self.base = base
         self.altura = altura
         self.perimetro = None
         self.area = None

    def calcular_area(self):
         self.area = self.base * self.altura
         return self.area
    
    def calcular_perimetro(self):
         self.perimetro = 2 * (self.base + self.altura)
         return self.perimetro
    

def ejecutar():
     print("\nCALCULAR ÁREA Y PERÍMETRO DE UN RECTÁNGULO \n\n")

     base = float(input("Ingrese la base del rectángulo: "))
     altura = float(input("Ingrese la altura del rectángulo: "))
     
     rectangulo = Rectangulo(base, altura)

     area = rectangulo.calcular_area()
     perimetro = rectangulo.calcular_perimetro()

     print(f"\n\n El area del rectángulo es: {area}(unidad) cuadrados.")
     print(f"El perimetro del rectángulo es: {perimetro}(unidad).")

if __name__ == "__main__":
     ejecutar()