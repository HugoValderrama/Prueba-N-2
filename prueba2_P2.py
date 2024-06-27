precios = []
precios_usd = []
cont = 0
valor_dolar = 950

while cont < 10:
    producto = int(input("Ingrese valor de producto (CLP): $"))
    precios.append(producto)
    cont = cont + 1

print("Lista original con precios en Pesos Chilenos: ")
print(precios)
print()

for precio in precios:
    precio_usd = precio / valor_dolar
    precios_usd.append(precio_usd)

print("Lista nueva con precios en Dólares Estadounidenses: ")
print(precios_usd)