"""

12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis.
Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
ganador de cada partido avanza a la ronda siguiente.
El programa debe continuar preguntando ganadores de partidos hasta que quede un
único jugador, que es el campeón del torneo.

"""
def hacer_cruces(tenistas, cruces):
    for i in range(0, len(tenistas), 2):
        cruces.append([tenistas[i], tenistas[i+1]])
    return cruces

def elegir_ganador(cruces):
    for i in range(len(cruces)):
        print(f"1.{cruces[i][0]} vs. 2.{cruces[i][1]}")
        del cruces[i][int(input("Introduzca el número del jugador que ha ganado: ")) - 2]
    return cruces

total_tenistas = 1
tenistas = []

while total_tenistas <= 8:
    tenistas.append(input(f"{total_tenistas}. Introduzca un tenista a participar: "))
    total_tenistas += 1

cuartos = []
cuartos = hacer_cruces(tenistas, cuartos)
semis_cruce = elegir_ganador(cuartos)
semis = []
semis = hacer_cruces(semis_cruce, semis)
final_cruce = elegir_ganador(semis)
final = []
final = hacer_cruces(final_cruce, final)
ganador = elegir_ganador(final)

print(f"El ganador fue: {ganador[0][0][0]}")