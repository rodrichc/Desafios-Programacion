"""
9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama.
"""
list1=[]
list2=[]
word1 = input("Escriba una palabra: ")

aux_true = True
while aux_true:
    word2 = input("Escriba otra palabra: ")

    if len(word2) != len(word1) or word1 == word2:
        print(f"Introduzca palabras de misma longitud, pero no iguales.")
    else:
        aux_true = False

for i in word1:
    list1.append(i)
for i in word2:
    list2.append(i)

if set(list1) == set(list2):
    print(True)
else:
    print(False)

