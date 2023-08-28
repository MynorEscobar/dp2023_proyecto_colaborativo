suma=0
print("Las notas deben de ser números enteros")
for i in range(5):
    numero=int(input(f"Ingrese la nota número {i+1}: " ))
    suma+=numero
promedio=suma/5
print("El promedio de los números es: ", promedio)