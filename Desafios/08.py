"""
8-Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.
"""

list_products = {"A": 270, "B": 340, "C": 390}
list_coins = [100, 50, 10]
total_paid = 0

print("¡Bienvenido! Tiene 3 opciones de producto: ")
print(list_products)
print("")

while True:
    product = input("Ingrese A, B o C para elegir un producto: ").upper() 

    if product in list_products:
        price = list_products[product]
        print(f"El producto vale ${price}")
        print("")
        break
    else: 
        print("¡Ingrese correctamente el producto!")

print("Puede pagar con monedas de $10, $50 y $100")

while total_paid < price:
    coins = int(input("Ingrese una moneda: "))

    if coins in list_coins:
         total_paid += coins
    else:
     print("Ingrese una moneda valida")

if total_paid == price:
    print("El pago ha sido exacto. ¡Muchas gracias!")
else:
    change = total_paid - price
    print(f"Ha ingresado ${total_paid}, su vuelto es ${change}. Sus monedas: ")
    for change_coins in list_coins:
        while total_paid > price:
            if change_coins <= change:
                total_paid -= change_coins
                change -= change_coins
                print(f"${change_coins}")
            else: 
                break