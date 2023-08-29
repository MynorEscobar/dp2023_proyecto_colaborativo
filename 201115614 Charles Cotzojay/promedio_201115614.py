suma=0
print("Las notas deben debe ser un número entero")
for i in range(5):
    numero=int(input(f"Ingrese la nota  {i+1}: " ))
    suma+=numero
promedio=suma/5
print("El promedio de los números es: ", promedio)
