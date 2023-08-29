print("ingrese 4 números")
lista_numeros = []

for i in range(4):
    numero=int(input(f"Ingrese el número {i+1}: "))
    lista_numeros.append(numero)

mayor = max(lista_numeros)

print("El número mayor es: ", mayor)
