"""6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario. (IMAGEN)"""
while True:
    try:    
        numero = int(input("Ingrese cantidad de reglones: "))
        renglon = ""
        respaldo = 0
        if numero > 0:
            for i in range(1, numero + 1):
                respaldo = str(i*2) + " " + renglon
                renglon = respaldo
                print(renglon)
            break
        else:
            print("¡Introduzca un numero mayor a cero!")
    except ValueError:
        print("¡Introduzca un numero!")