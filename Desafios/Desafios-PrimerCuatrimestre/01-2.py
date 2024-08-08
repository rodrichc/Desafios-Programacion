"""Escriba un programa que pida al usuario un entero de tres dígitos,
y entregue el número con los dígitos en orden inverso."""
no_cumple = True
while no_cumple:
    numero = input("Ingrese un número de tres dígitos: ")
    if numero.isnumeric() and int(numero)> 99 and int(numero) < 1000:
        numero = int(numero[::-1])
        print("El número con los dígitos en orden inverso es:", numero)
        no_cumple = False
    else:
        print("¡Ingrese un numero valido!")
