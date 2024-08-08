"""
14- Signo zodiacal. El signo zodiacal de una persona está determinado por su día de
nacimiento.

El diccionario de signos asocia a cada signo el período del año que le corresponde. Cada
período es una tupla con la fecha de inicio y la fecha de término, y cada fecha es una
tupla (mes, dia):
    signos = {
        'aries': (( 3, 21), ( 4, 20)),
        'tauro': (( 4, 21), ( 5, 21)),
        'geminis': (( 5, 22), ( 6, 21)),
        'cancer': (( 6, 22), ( 7, 23)),
        'leo': (( 7, 24), ( 8, 23)),
        'virgo': (( 8, 24), ( 9, 23)),
        'libra': (( 9, 24), (10, 23)),
        'escorpio': ((10, 24), (11, 22)),
        'sagitario': ((11, 23), (12, 21)),
        'capricornio': ((12, 22), ( 1, 20)),
        'acuario': (( 1, 21), ( 2, 19)),
        'piscis': (( 2, 20), ( 3, 20)),
    }

Por ejemplo, para que una persona sea de signo libra debe haber nacido entre el 24 de
septiembre y el 23 de octubre.

Escriba la función determinar_signo(fecha_de_nacimiento) que reciba como parámetro la fecha de nacimiento de una persona, representada como una tupla (año, mes, dia), y que retorne el signo zodiacal de la persona: 
    >>> determinar_signo((1990, 5, 7))
    'tauro'
    >>> determinar_signo((1904, 11, 24))
    'sagitario'
    >>> determinar_signo((1998, 12, 28))
    'capricornio'
    >>> determinar_signo((1999, 1, 11))
    'capricornio'
"""
def determinar_signo(fecha_nacimiento):
    
    signos = {
            'aries': (( 3, 21), ( 4, 20)),
            'tauro': (( 4, 21), ( 5, 21)),
            'geminis': (( 5, 22), ( 6, 21)),
            'cancer': (( 6, 22), ( 7, 23)),
            'leo': (( 7, 24), ( 8, 23)),
            'virgo': (( 8, 24), ( 9, 23)),
            'libra': (( 9, 24), (10, 23)),
            'escorpio': ((10, 24), (11, 22)),
            'sagitario': ((11, 23), (12, 21)),
            'capricornio': ((12, 22), ( 1, 20)),
            'acuario': (( 1, 21), ( 2, 19)),
            'piscis': (( 2, 20), ( 3, 20)),
        }

    mes, dia = fecha_nacimiento

    for signo, ((mes_inicio, dia_inicio),(mes_fin, dia_fin)) in signos.items():
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return signo

mes = int(input("Intruzca mes de nacimiento en numero (Ej. 2): "))
dia = int(input("Intruzca día de nacimiento en numero (Ej. 26): "))

fecha_nacimiento = (mes, dia)

resultado = determinar_signo(fecha_nacimiento)

print(f"Su signo es: {resultado}")