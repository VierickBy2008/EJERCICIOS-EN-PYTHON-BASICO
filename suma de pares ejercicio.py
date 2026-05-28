limite = int(input("Introduce un número entero: "))

suma_pares = 0
suma_impares = 0
suma_multiplos_5 = 0

for i in range(1, limite + 1):
    
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
        
    if i % 5 == 0:
        suma_multiplos_5 += i

print(f"\nResultados hasta el {limite}:")
print(f"Total suma de pares: {suma_pares}")
print(f"Total suma de impares: {suma_impares}")
print(f"Total suma de múltiplos de 5: {suma_multiplos_5}")