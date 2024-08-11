"""
    2. Registro de Tareas. Crea una clase Tarea que almacene información sobre
tareas pendientes. Implementa los métodos __str__ y __len__ para mostrar
detalles de la tarea y contar cuántas tareas hay en la lista.
"""

class Tarea:
    def __init__(self, actividad, descripcion):
        self.actividad = actividad
        self.descripcion = descripcion

    def __str__(self):
        return f"Tarea: {self.actividad} Detalle: {self.descripcion}"
    

class ListaTareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, tarea):
        self.lista_tareas.append(tarea)
        return lista_tareas
    def __len__(self):
        return len(self.lista_tareas)

tarea1 = Tarea("Compras", "Comprar pan y hierba")
tarea2 = Tarea("Estudiar", "Repasar todo lo visto en la clase")

lista_tareas = ListaTareas()

lista_tareas.agregar_tarea(tarea1)
lista_tareas.agregar_tarea(tarea2)

print(tarea1)
print(len(lista_tareas))

