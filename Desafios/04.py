"""4- Tiempo de viaje: Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0."""
total_duration = 0
while True:
    duration_section = int(input("Ingrese duracion en minutos del tramo, 0 para terminar: "))

    if duration_section != 0:
        total_duration += duration_section
    else:
        break

hours = total_duration // 60
minutes = total_duration % 60

if minutes < 10:
    print(f"Duracion total del viaje: {hours}:0{minutes}hs")
else:
    print(f"Duracion total del viaje: {hours}:{minutes}hs")