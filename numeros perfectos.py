num = int(input("Ingresa un número para saber si es perfecto: "))
suma_divisores = 0

for i in range(1, num):
    if num % i == 0:
        suma_divisores += i

if suma_divisores == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")