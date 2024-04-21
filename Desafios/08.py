"""
8-Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.
"""

price_products = {"A": 270, "B": 340, "C": 390}
list_coins = [10, 50, 100]
total_coins = 0
price = 0

print("¡Bienvenido! Tiene 3 opciones de producto: ")
print(price_products)
print("")

while True:
    product = input("Ingrese A, B o C para elegir un producto: ").upper() 

    if product in price_products:
        price = price_products[product]
        print(f"El producto vale ${price}")
        print("")
        break
    else: 
        print("¡Ingrese correctamente el producto!")

print("Puede pagar con monedas de $10, $50 y $100")

while total_coins < price:
    coins = int(input("Ingrese una moneda: "))

    if coins in list_coins:
         total_coins += coins
         print(f"Ha ingresado ${total_coins}, le falta ${price - total_coins}") 
    else:
     print("Ingrese una moneda valida")

if total_coins == price:
    print("El pago ha sido exacto. ¡Muchas gracias!")
else:
    change = total_coins - price
    print(f"Su vuelto es ${change}. Sus monedas: ")
    for change_coins in list_coins:
        while total_coins > price:
            print(f"${change_coins}")
            total_coins -= change_coins