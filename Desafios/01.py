"""Escriba un programa que pida al usuario un entero de tres dígitos,
y entregue el número con los dígitos en orden inverso."""
numero = int(input("Ingrese un número de tres dígitos: "))

if numero > 99 and numero < 1000:
    unidad = numero // 100
    decena = (numero % 100) // 10
    centena = numero % 10

    print(f"El número con los dígitos en orden inverso es: {centena}{decena}{unidad}")
else:
    print("¡Ingrese un numero valido!")
