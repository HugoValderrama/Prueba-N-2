capitales = {

    "Berlin": "Alemania",
    "Paris": "Francia",
    "Roma": "Italia",
    "Moscu": "Rusia",
    "Tokio": "Japon"

}

personas = {}

while True:

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