"""
Persona. crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
    a. Un constructor, donde los datos pueden estar vacíos.
    b. Los setters y getters para cada uno de los atributos. Hay que validar las
  entradas de datos.
    c. mostrar(): Muestra los datos de la persona.
    d. esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
  Además, crea en una aplicación de consola que permita al usuario crear un objeto
  Persona y evaluar si es mayo o menor de edad..

"""
class Persona:
    def __init__(self, nombre = None, edad = None, dni = None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni


  # GETTERS
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad

    def get_dni(self):
        return self._dni
    
  #SETTERS
    def set_nombre(self, nombre):
        if nombre.isalpha() and len(nombre) < 10:
            self.nombre = nombre
        else:
            print("Introduzca un nombre válido.")

    def set_edad(self, edad):
        if edad.isnumeric() and (0 <= int(edad) <= 100):
            self.edad = edad
        else:
            print("Introduzca una edad válida.")

    def set_dni(self, dni):
        if dni.isnumeric() and len(str(dni)) == 8:
            self.dni = dni
        else:
            print("Introduzca un DNI válido.")


  # Mostrar datos
    def mostrar(self):
        print("---DATOS DE LA PERSONA---\n")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

  #Verificación si es mayor o no
    def es_mayor(self):
        if int(self.edad) >= 18:
            print("Es mayor de edad.")
        else: 
            print("Es menor de edad.")



print("Crear persona:")

nombre = input("Ingrese el nombre: \n")
edad = input("Ingrese la edad: \n")
dni = input("Ingrese el DNI: \n")

persona = Persona()
persona.set_nombre(nombre)
persona.set_edad(edad)
persona.set_dni(dni)

persona.mostrar()

persona.es_mayor()