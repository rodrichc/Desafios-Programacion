"""
3. Producto. Crea una clase Producto con los siguientes atributos: Nombre, Precio y
Stock siendo obligatorios sólo los atributos Nombre y Precio. El Stock debe comenzar
con 0. Define métodos para actualizar el stock, para calcular el total del inventario y
para ver los datos. Además, escribe una aplicación de consola que permita al usuario:
1- actualizar el stock y 2- calcular inventario hasta que decida detenerse. Al finalizar
deberá mostrar los datos del producto, stock e inventario final.

"""
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            print("No hay suficiente stock")
        else:
            self.stock += cantidad

    def calcular_inventario(self):
        return self.stock * self.precio
    
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}\nValor del inventario: {self.calcular_inventario()}"

def crear_producto():
    print("\n INGRESAR NUEVO PRODUCTO \n\n")

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))

    producto = Producto(nombre, precio)

    return producto

def consultar_producto(producto):
    print(f"\n\n-{producto.nombre}:")
    
    while True:
        print("\n1. Actualizar stock.")
        print("2. Calcular inventario.")
        print("3. Mostrar datos.")
        print("4. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        if opcion == 1:
            cantidad = int(input("\n Cantidad: "))
            producto.actualizar_stock(cantidad)
            print("\n ¡Stock actualizado!\n")
        
        elif opcion == 2:
            print(f"\n Valor del inventario: ${producto.calcular_inventario()}")
        
        elif opcion == 3:
            print(f"\n {producto.mostrar_datos()}")
        
        elif opcion == 4:
            print("\n Saliendo...")
            break
        
        else: 
            print("¡Seleccione una opción correcta!")

def ejecutar():
    producto = crear_producto()
    
    consultar_producto(producto)

if __name__ == "__main__":
    ejecutar()
