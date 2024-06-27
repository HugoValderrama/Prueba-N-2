notas = []
lista_menor_4 = []
lista_mayor_4 = []

while True:
    nota = float(input("Ingrese nota (Ingrese 0 para finalizar): "))

    if nota == 0:
        break

    notas.append(nota)

    if nota <= 3.9:
        lista_menor_4.append(nota)
    elif nota >= 4.0:
        lista_mayor_4.append(nota)

cantidad = len(notas)
suma = sum(notas)
promedio = suma / cantidad 

print("Cantidad de notas:", cantidad)
print("Promedio de notas:", promedio)
print("Cantidad de notas menores a 4.0:", len(lista_menor_4))
print("Cantidad de notas mayores o iguales a 4.0:", len(lista_mayor_4))