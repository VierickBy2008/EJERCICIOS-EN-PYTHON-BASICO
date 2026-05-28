# 1. Entrada de datos
binario = input("Ingrese un número binario: ")

# 2. Rellenar con ceros a la izquierda para tener grupos de 4 completos
# Mientras el largo no sea múltiplo de 4, añadimos un "0" al principio
while len(binario) % 4 != 0:
    binario = "0" + binario

# 3. Diccionario de equivalencias (Mapeo directo)
tabla_hex = {
    "0000": "0", "0001": "1", "0010": "2", "0011": "3",
    "0100": "4", "0101": "5", "0110": "6", "0111": "7",
    "1000": "8", "1001": "9", "1010": "A", "1011": "B",
    "1100": "C", "1101": "D", "1110": "E", "1111": "F"
}

resultado_hex = ""

# 4. Procesar el número en bloques de 4
# range(inicio, fin, salto)
for i in range(0, len(binario), 4):
    bloque = binario[i:i+4]  # Tomamos 4 caracteres
    resultado_hex += tabla_hex[bloque] # Traducimos y acumulamos

# 5. Salida
print(f"El número binario {binario} en hexadecimal es: {resultado_hex}")