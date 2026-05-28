# 1. Creamos el diccionario de traducción
romanos = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
    11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV",
    16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX"
}

# 2. Entrada de datos
numero = int(input("Ingrese un número del 1 al 20: "))

# 3. Lógica de validación y visualización
if 1 <= numero <= 20:
    print(f"El número {numero} en romanos es: {romanos[numero]}")
else:
    print("Error: El número debe estar entre 1 y 20.")