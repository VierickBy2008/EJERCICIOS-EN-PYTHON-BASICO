n = int(input("Ingresa el valor de n para el número triangular: "))

# Opción A: Con bucle
suma = 0
for i in range(1, n + 1):
    suma += i

# Opción B: Con fórmula (más eficiente)
triangular = (n * (n + 1)) // 2

print(f"El {n}-ésimo número triangular es: {triangular}")