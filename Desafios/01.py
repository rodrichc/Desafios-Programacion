"""Escriba un programa que pida al usuario un entero de tres dígitos,
y entregue el número con los dígitos en orden inverso."""
try:
    numero = int(input("Ingrese un número de tres dígitos: "))

    if numero > 99 and numero < 1000:
        primer_num = str(numero // 100)
        segundo_num = str((numero % 100) // 10)
        tercer_num = str(numero % 10)

        print("El número con los dígitos en orden inverso es:", tercer_num + segundo_num + primer_num)
    else:
        print("¡Ingrese un numero valido!")
except ValueError:
    print("¡Ingrese un numero valido!")