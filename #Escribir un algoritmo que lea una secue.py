#Escribir un algoritmo que lea una secuencia de numeros positivos acabada en 0 y encuentre el menor, el mayor y el promedio de los numeros leidos
mayor = None
menor = None
suma = 0
contador = 0

print("Introduce números positivos (escribe 0 para terminar):")

while True:
    numero = float( input("ingrese un numero: ") )

    if numero == 0:
        break
    if numero < 0:
        print("solo se permiten numeros positivos")
        continue

    suma += numero
    contador += 1

    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero

if contador > 0:
    promedio = suma / contador
    print("\n--- Resultados ---")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números válidos.")
  
















































































