capitales = {}
personas = {}
cont = 0

while True:
    
    capital = input("Ingrese ciudad capital: ")
    pais = input("Ingrese país: ")
    print()
    capitales[capital] = pais
    cont = cont + 1

    if cont >= 5:
        break

while True:

    print()
    nombre = input("Ingrese nombre del turista: ")
    capital = input("Ingrese capital de procedencia: ")

    if nombre.isalpha():

        if capital in capitales:
            pais = capitales[capital]
            personas[nombre] = pais
            break

        else:
            print()
            print("Capital desconocida")

    else:
        print()
        print("Nombre no valido")

for nombre in personas:
    pais = personas[nombre]
    print()
    print("El turista con el nombre", nombre, "viene de la capital", capital, "y su país es", pais)
