"""Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es un numero primo o no"""

numero = int(input("Ingrese un numero entero: "))

es_primo = True
for n in range(2, numero):
    if numero % n == 0:
        es_primo = False

if es_primo == True:
    print("Es Primo")
else:
    print("No es primo")