"""
9 - Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama.
"""

word1 = input("Escriba una palabra: ")
list1=[]
while True:
    word2 = input("Escriba otra palabra: ")
    list2=[]
    if len(word2) != len(word1):
        print(f"Introduzca una palabra de {len(word1)} caracteres.")
    else:
        break

for i in word1:
    list1.append(i)
for i in word2:
    list2.append(i)

if set(list1) == set(list2):
    print(True)
else:
    print(False)

