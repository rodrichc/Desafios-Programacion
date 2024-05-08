"""
7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
● La sucesión termina al llegar a uno.
Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
"""
aux_true = True
while aux_true:
    collatz = input("Ingrese un numero: ")
    numero = int(collatz)
    if numero > 1:
        while numero > 1:
            if (numero % 2) == 0:
                numero = int (numero / 2)
                collatz += " " + str(numero) 
            else:
                numero = int((numero * 3) + 1)
                collatz += " " + str(numero)
        print(collatz)
        aux_true = False
    else:
        print("¡Ingrese un numero mayor a 1!")