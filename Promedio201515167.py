def main():
    notas = []
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")

if __name__ == "__main__":
    main()