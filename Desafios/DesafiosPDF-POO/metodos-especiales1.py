"""1. Conversor de Monedas. Crea una clase Moneda que permita la conversión
   entre monedas (ej. dólares a pesos). Implementa los métodos __str__ y
   __add__ para mostrar la cantidad convertida y sumar cantidades en
 diferentes monedas."""


class Moneda:
    valor_moneda = {
        'USD': 1.0,
        'ARS': 1300.0,
        'EUR': 0.90
    }

    def __init__(self, cantidad, moneda = 'USD'):
        self.cantidad = float(cantidad)
        self.moneda = moneda
    
    def __str__(self):
        return f"{self.cantidad} {self.moneda}"
    
    def __add__(self, suma):
        if isinstance(suma, Moneda):
            if self.moneda == 'USD':
                convertir_moneda = round(suma.cantidad / Moneda.valor_moneda[suma.moneda], 2)
            else:
                convertir_moneda = round(suma.cantidad * Moneda.valor_moneda[self.moneda], 2)
            sumar_monedas = convertir_moneda + self.cantidad
            return Moneda(sumar_monedas, self.moneda)
        else:
            return "¡Solamente se puede sumar entre monedas!"    
        
dolares = Moneda(100)
pesos = Moneda(1300, 'ARS')

sumar_cartera = dolares + pesos

print(dolares)
print(pesos)
print(sumar_cartera)