factura = input("Ingresa numero de factura: ")
print ("Los productos y sus precios \n" "1. Huevos: $100.000 \n"  "2. Leche: $20.000 \n" "3. Chocolate: $30.000 \n" "4. Salchicha: $10.000 \n"  "5. Pan: $40.000 \n"  )
productos = {1:100000, 2:20000, 3: 300000, 4:10000, 5:40000}

prc1 = int(input("Ingresa el numero del producto 1: "))
cant1 = int(input("Ingresa la cantidad del producto 1: "))
prc2 = int(input("Ingresa el numero del producto 2: "))
cant2 = int(input("Ingresa la cantidad del producto 2: "))
prc3 = int(input("Ingresa el numero del producto 3: "))
cant3 = int(input("Ingresa la cantidad del producto 3: "))
prc4 = int(input("Ingresa el numero del producto 4: "))
cant4 = int(input("Ingresa la cantidad del producto 4: "))
prc5 = int(input("Ingresa el numero del producto 5: "))
cant5 = int(input("Ingresa la cantidad del producto 5: "))

total1 = int(productos.get(prc1, 0) * cant1)
total2 = int(productos.get(prc2, 0) * cant2)
total3 = int(productos.get(prc3, 0) * cant3)
total4 = int(productos.get(prc4 ,0) * cant4)
total5 = int(productos.get(prc5, 0) * cant5)


total = int(total1 + total2 + total3 + total4 + total5)
print(f"La suma de los productos es: {total}")

if (total > 100000):
    descuento = (total * 10) /100
    tcd = int(total - descuento)
    print(f"El total con el 10% descuento es: {tcd}")
else:
    print("NO APLICA EL DESCUENTO")
