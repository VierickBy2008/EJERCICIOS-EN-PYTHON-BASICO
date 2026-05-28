n = 1.0
print(f"{'N':<10} | {'N^2':<10} | {'N^0.5':<10}")
print("-" * 35)

while n <= 1.1001: # El .0001 es para evitar errores de redondeo
    cuadrado = n ** 2
    raiz = n ** 0.5
    print(f"{n:<10.3f} | {cuadrado:<10.4f} | {raiz:<10.4f}")
    n += 0.001