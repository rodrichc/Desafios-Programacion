"""11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra."""
def ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
        return "¡Ganador Jugador 1!"
    elif (jugador2 == "piedra" and jugador1 == "tijera") or (jugador2 == "tijera" and jugador1 == "papel") or (jugador2 == "papel" and jugador1 == "piedra"):
        return "¡Ganador Jugador 2!"
    else: 
        return "¡ERROR! Uno de los jugadores hizo una jugada invalida."

jugador1 = input("Jugador 1, elija entre: Piedra, Papel o Tijera: ").lower()
jugador2 = input("Jugador 2, elija entre: Piedra, Papel o Tijera: ").lower()

resultado = ganador(jugador1, jugador2)

print(resultado)