"""Escriba un programa que pregunte al usuario
la hora actual (t) del reloj y un numero entero de horas (h),
que indique qué hora marcara dentro de h horas."""

t = int(input("Indique que hora es: "))
h = int(input("¿Cuantas horas le queres agregar a la hora actual? "))

hora = t
contador = 0

while contador < h:
    contador += 1
    hora += 1
    if hora == 24:
        hora = 0

print(f"Van a ser las {hora} horas, si a las {t} se le agregan {h} horas")