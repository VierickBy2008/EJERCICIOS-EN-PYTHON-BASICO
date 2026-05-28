n = int(input("¿Cuántos términos de Fibonacci deseas?: "))

f1, f2 = 1, 1

for i in range(n):
    print(f1, end=", " if i < n-1 else "")
    # Actualizamos los valores: f1 pasa a ser f2, y f2 la suma de ambos
    f1, f2 = f2, f1 + f2