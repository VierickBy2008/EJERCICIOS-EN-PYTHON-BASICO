# Inicializamos el acumulador
suma_multiplos_3 = 0

# El bucle recorre del 1 al 20 (usamos 21 porque el límite superior no se incluye)
for i in range(1, 21):
    # Calculamos el múltiplo de 3 y lo sumamos al acumulador
    suma_multiplos_3 += 3 * i

# Imprimimos el resultado final
print(f"La suma de los 20 primeros múltiplos de 3 es: {suma_multiplos_3}")