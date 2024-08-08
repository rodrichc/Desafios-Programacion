"""

15- Autores de Libros. Este problema apareció en el certamen 2 del segundo semestre de
2011 en el campus Vitacura.
Escriba las funciones necesarias para que el siguiente programa funcione:

"""
def obtener_autor(titulo, libros):
    for libro in libros:
        nombre, autor, anio = libro
        if nombre.lower() == titulo.lower():
            return autor, anio

def obtener_idioma(autor, autores):
    nacimiento, defuncion, idioma = autores[autor]
    return idioma, defuncion 

def calcular_anios_antes_de_morir(anio_publicacion, defuncion):
    anio, mes, dia = defuncion
    resultado = anio - anio_publicacion
    return resultado


libros = [
    ('Papelucho programador', 'Marcela Paz', 1983),
    ('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
    ('Raw_input y Julieta', 'William Shakespeare', 1597),
    ('La tuplamorfosis', 'Franz Kafka', 1915),
    # ...
]

autores = {
    # autor: nacimiento, defunción, idioma
    'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
    'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
    'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
    'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
    # ...
    }

titulo = input('Ingrese titulo del libro: ')

autor, anio_publicacion = obtener_autor(titulo, libros)
idioma, defuncion = obtener_idioma(autor, autores)
anios_antes_morir = calcular_anios_antes_de_morir(anio_publicacion, defuncion)

print (f"El libro fue escrito en {idioma} por {autor}." )
print (f"El autor fallecio {anios_antes_morir} años después de haber escrito el libro.")

    
