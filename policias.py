n_presos = int(input("Número de presos: "))
conteo_pistas = {'A': 0, 'B': 0, 'C': 0}

for i in range(1, n_presos + 1):
    m_pistas = int(input(f"¿Cuántas pistas tiene el preso {i}?: "))
    puntos_total = 0
    for j in range(m_pistas):
        tipo = input("Tipo de pista (A, B, C): ").upper()
        if tipo == 'A': puntos_total += 20
        elif tipo == 'B': puntos_total += 15
        elif tipo == 'C': puntos_total += 30
        conteo_pistas[tipo] += 1
    
    # Determinar estatus
    if puntos_total > 85: estatus = "Culpable"
    elif puntos_total > 65: estatus = "Sospechoso de alto riesgo"
    else: estatus = "Sospechoso de bajo riesgo"
    
    print(f"Preso {i} - Estatus: {estatus}")

# Estadísticas de pistas
total_pistas = sum(conteo_pistas.values())
mas_frecuente = max(conteo_pistas, key=conteo_pistas.get)

print(f"\nTipo de pista más frecuente: {mas_frecuente}")
for tipo, cant in conteo_pistas.items():
    porcentaje = (cant / total_pistas) * 100 if total_pistas > 0 else 0
    print(f"Porcentaje de pistas tipo {tipo}: {porcentaje:.2f}%")