"""
   4. Agenda de Contactos. Crea una clase Contacto que almacene información
sobre personas en una agenda. Implementa los métodos __str__ y
__setitem__ para mostrar detalles del contacto y modificar sus atributos (por
ejemplo, número de teléfono)
"""

class Contacto:
   def __init__(self, nombre, apellido, telefono):
      self.nombre = nombre
      self.apellido = apellido
      self.telefono = telefono
   
   def __str__(self):
      return f"Detalles de Contacto: \n Nombre: {self.nombre} \n Apellido: {self.apellido} \n Teléfono: {self.telefono}"
   
   def __setitem__(self, item, valor_actualizado):
      
      if item == "nombre":
         self.nombre = valor_actualizado
      if item == "apellido":
         self.apellido = valor_actualizado
      if item == "telefono":
         self.telefono = valor_actualizado
      
      else:
         return "¡ERROR! \nPara cambiar la información. Ingrese: nombre, apellido o telefono."


nuevo_contacto = Contacto("Rodrigo", "Chavez", "+54 351 2222222")

print(nuevo_contacto)

nuevo_contacto["apellido"] = "Cuffa"

print(nuevo_contacto)
               