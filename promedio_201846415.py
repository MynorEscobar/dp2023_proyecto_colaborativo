def calcular_promedio():
    suma = 0

    for i in range(1, 6):
        while True: 
            try:
                nota = float(input(f"Introduce la nota {i}: "))
                if 0 <= nota <= 10:  
                    suma += nota
                    break 
                else:
                    print("Nota inválida. Introduce un valor entre 0 y 10.")
            except ValueError:  
                print("Por favor, introduce un número válido.")
 
    promedio = suma / 5
   
    print(f"El promedio de las 5 notas es: {promedio:.2f}")


calcular_promedio()
