import math

p = int(input("¿Cuántos números naturales deseas procesar?: "))

print(f"{'Num':<5} | {'Cuadrado':<10} | {'Cubo':<10} | {'Raíz':<10}")
print("-" * 40)

for i in range(1, p + 1):
    cuadrado = i ** 2
    cubo = i ** 3
    raiz = math.sqrt(i) # O i ** 0.5
    print(f"{i:<5} | {cuadrado:<10} | {cubo:<10} | {raiz:<10.2f}")