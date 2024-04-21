"""Escriba un programa que pida al usuario un entero de tres dígitos,
y entregue el número con los dígitos en orden inverso."""
while True:
    try:
        numero = input("Ingrese un número de tres dígitos: ")

        numero = int(numero[::-1])

        if numero > 99 and numero < 1000:
            print("El número con los dígitos en orden inverso es:", numero)
            break
        else:
            print("¡Ingrese un numero valido!")
    except ValueError:
        print("¡Ingrese un numero valido!")