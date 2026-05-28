n = int(input("Hasta qué fila deseas el triángulo de Floyd: "))

for fila in range(1, n + 1):
    for columna in range(1, fila + 1):
        print(columna, end=" ")
    print() # Salto de línea al terminar la fila