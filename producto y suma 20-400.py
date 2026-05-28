suma_pares = 0
producto_pares = 1

for a in range(20, 401, 2):
        suma_pares += a
        producto_pares *= a
    
print(f"la suma de pares entre 20 y 400 es: {suma_pares}")
print(f"\nProducto de los pares (es un numero muy grande): \n {producto_pares}")