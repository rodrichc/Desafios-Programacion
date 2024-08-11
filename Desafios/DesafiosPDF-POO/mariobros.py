"""
MarioBros:
        1. Crear una clase base llamada “Personaje”: esta clase contendrá los atributos
    y métodos comunes a todos los personajes del juego. Por ej. los atributos
    podrían ser nombre, vidas y poder. Los métodos podrían ser: mover, saltar y
    caer.
        2. Crea clases derivadas para cada personaje específico. Estas clases heredarán
    de la clase base “Personaje” y podrán tener atributos y métodos adicionales.
    Por ej. la clase Mario podría tener un método adicional lanzar_fuego()
    mientras que la clase Luigi podría tener un método adicional usar_hongo().
        3. Crea clases base para los enemigos. Esta clase contendrá los atributos y
    métodos comunes a todos los enemigos. Por ejemplo, los métodos podrían ser
    tipo, daño y, los métodos podrían ser mover, atacar, etc.
        4. Crear clases derivadas de la clase enemigo. Estas clases heredarán de la clase
    base “Enemigo” y podrán tener atributos y métodos adicionales. Por ej. la
    clase “Koopa Troopa” podría tener un método adicional usar_casco(),
    mientras que la clase “Goomba” podría tener un método esconder()
    Nota: Para la implementación de los métodos simplemente imprime en pantalla un
    texto que explique lo que haría el personaje.
"""

class Personaje:
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida 
        self.poder = poder

    def mover(self):
        return f"¡{self.nombre} se ha movido!"
    
    def saltar(self):
        return f"¡{self.nombre} ha saltado!"
    
    def caer(self):
        return f"¡{self.nombre} ha caido!"
    
class Mario(Personaje):
    def __init__(self, vida, poder, nombre = "Mario"):
        super().__init__(nombre, vida, poder)
    
    def lanzar_fuego(self):
        return f"¡{self.nombre} ha lanzado fuego!"
    
class Luigi(Personaje):
    def __init__(self, vida, poder, nombre = "Luigi"):
        super().__init__(nombre, vida, poder)
    
    def usar_hongo(self):
        return f"¡{self.nombre} ha usado el hongo!"
    

class Enemigo(Personaje):
    def __init__(self, nombre, vida, poder, tipo):
        super().__init__(nombre, vida, poder)
        self.tipo = tipo

    def atacar(self):
        return f"{self.nombre} te esta atacando."
    
class KoopaTroopa(Enemigo):
    def __init__(self, vida, poder, tipo, nombre = "Koopa Troopa"):
        super().__init__(nombre, vida, poder, tipo)

    def usar_casco(self):
        return f"¡{self.nombre} ha usado casco!"
    

class Goomba(Enemigo):
    def __init__(self, vida, poder, tipo, nombre = "Goomba"):
        super().__init__(nombre, vida, poder, tipo)

    def esconder(self):
        return f"¡{self.nombre} se ha escondido!"
    


mario = Mario(10, 10)

luigi = Luigi(8, 8)

koopa_troopa = KoopaTroopa(5, 5, "tortuga")
goomba = Goomba(5, 5, "hongo")

print(mario.caer())
mario.lanzar_fuego()

print(luigi.mover())
print(luigi.usar_hongo())

print(koopa_troopa.atacar())
print(koopa_troopa.usar_casco())

print(goomba.mover())
print(goomba.esconder())