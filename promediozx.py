# 1. Leemos el número como texto (string)
numero = input("Ingrese un número entero: ")

suma = 0
longitud = len(numero)

# Calculamos la suma de los dígitos
for digito in numero:
    # Convertimos cada carácter a entero antes de sumarlo
    suma += int(digito)

# Calculamos el promedio (usamos // para división entera, igual que en Java)
promedio = suma // longitud
print(f"Promedio de sus dígitos: {promedio}")

# 2. Rotar hacia la izquierda
resultado = numero
for i in range(promedio):
    primer_digito = resultado[0]      # Obtenemos el primer carácter
    resto_del_numero = resultado[1:]  # Obtenemos todo desde la posición 1 en adelante
    # Reconstruimos: el resto al principio y el primero al final
    resultado = resto_del_numero + primer_digito

print(f"Número rotado {promedio} veces: {resultado}")