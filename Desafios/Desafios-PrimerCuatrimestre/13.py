"""
El diccionario países asocia cada persona con el conjunto de los países que ha
visitado:
    paises = {
        'Pepito': {'Chile', 'Argentina'},
        'Yayita': {'Francia', 'Suiza', 'Chile'},
        'John': {'Chile', 'Italia', 'Francia', 'Peru'},
    }
Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
visitado la persona a y la persona b:

    cuantos_en_comun('Pepito', 'John')
        1
    cuantos_en_comun('John', 'Yayita')
        2
"""
def agregar_paises(personas_paises, persona):
    cantidad_paises = int(input(f"Ingrese en numero la cantidad de paises que ha visitado {persona}: "))
    for i in range (cantidad_paises):
        personas_paises[persona].append(input(f"Ingrese el {i + 1}° que ha visitado {persona}: ").lower())
    return personas_paises

def cuantos_en_comun (persona1, persona2, personas_paises):
    p1_set = set(personas_paises[persona1])
    p2_set = set(personas_paises[persona2])
    paises_comun = p1_set.intersection(p2_set)
    return f"Paises en común visitados: {paises_comun}"     

personas = input("Escribe separado por comas (',') las personas que quieras agregar a la comparación: ")

lista_personas = personas.split(',')
lista_personas = [persona.strip() for persona in lista_personas] #strip() elimina los espacios en blanco de una variable, en este caso el iterable persona toma el valor de cada uno de los elementos de la lista y por cosiguiente se eliminan los espacios en blanco.

personas_paises = {}

for persona in lista_personas:
    personas_paises[persona] = []

for persona in personas_paises.keys():
    personas_paises = agregar_paises(personas_paises, persona)

print("Elije la comparación entre las siguientes personas:")
for persona in personas_paises.keys():
        print(persona)
persona1 = input("Primera persona a comparar: ")
persona2 = input("Segunda persona a comparar: ")

paises_comun = cuantos_en_comun(persona1, persona2, personas_paises)

print(paises_comun)