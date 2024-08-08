"""6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario. (IMAGEN)"""
no_cumple = True

while no_cumple:
    numero = input("Ingrese cantidad de reglones: ")
    renglon = ""
    respaldo = 0
    
    if numero.isnumeric() and int(numero) > 0:
        numero = int(numero)
        for i in range(1, numero + 1):
            respaldo = str(i*2) + " " + renglon
            renglon = respaldo
            print(renglon)
        no_cumple = False
    else:
        print("¡Introduzca un numero mayor a cero!")