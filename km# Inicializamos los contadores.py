# Inicializamos los contadores
total_encuestados = 0
acepta_A = 0
acepta_B = 0
acepta_Ambos = 0
acepta_A_no_B = 0
acepta_B_no_A = 0
acepta_Ninguno = 0

print("--- Encuesta de Mercado (Ingresa -1 para finalizar) ---")

while True:
    val_A = int(input("\n¿Acepta el producto A? (1=Sí, 0=No): "))
    if val_A == -1: break  # Condición para salir del bucle
    
    val_B = int(input("¿Acepta el producto B? (1=Sí, 0=No): "))
    
    total_encuestados += 1
    
    # Lógica de clasificación
    if val_A == 1 and val_B == 1:
        acepta_Ambos += 1
        acepta_A += 1
        acepta_B += 1
    elif val_A == 1 and val_B == 0:
        acepta_A_no_B += 1
        acepta_A += 1
    elif val_A == 0 and val_B == 1:
        acepta_B_no_A += 1
        acepta_B += 1
    elif val_A == 0 and val_B == 0:
        acepta_Ninguno += 1

# Cálculos de porcentajes (solo si hubo encuestados para evitar error de división por cero)
if total_encuestados > 0:
    def porcentaje(cantidad):
        return (cantidad / total_encuestados) * 100

    print("\n" + "="*30)
    print(f"Total de encuestados: {total_encuestados}")
    print(f"Aceptan A: {porcentaje(acepta_A)}%")
    print(f"Aceptan B: {porcentaje(acepta_B)}%")
    print(f"Aceptan los dos: {porcentaje(acepta_Ambos)}%")
    print(f"Aceptan A pero no B: {porcentaje(acepta_A_no_B)}%")
    print(f"Aceptan B pero no A: {porcentaje(acepta_B_no_A)}%")
    print(f"No aceptan ninguno: {porcentaje(acepta_Ninguno)}%")
else:
    print("No se ingresaron datos.")