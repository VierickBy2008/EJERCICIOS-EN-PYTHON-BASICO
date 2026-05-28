import math

n_postulantes = 1000  # Puedes bajarlo a 5 para probar
vacantes = 150
notas = []
ingresantes_notas = []

for i in range(1, n_postulantes + 1):
    print(f"\n--- Postulante {i} ---")
    # RM y RV
    c_rm = int(input("Correctas RM/RV (de 40): "))
    i_rm = int(input("Incorrectas RM/RV: "))
    # Ciencias
    c_ci = int(input("Correctas Ciencias (de 30): "))
    i_ci = int(input("Incorrectas Ciencias: "))
    # Letras
    c_le = int(input("Correctas Letras (de 30): "))
    i_le = int(input("Incorrectas Letras: "))
    
    # Cálculo de nota
    nota = (c_rm * 2 - i_rm * 1) + (c_ci * 3 - i_ci * 1.5) + (c_le * 1 - i_le * 0.5)
    notas.append(nota)
    
    if nota >= 120:
        ingresantes_notas.append(nota)
        print("ESTATUS: INGRESO")
    else:
        print("ESTATUS: NO INGRESO")

# b) Media aritmética
media = sum(notas) / len(notas)

# c) Varianza
suma_varianza = sum((x - media) ** 2 for x in notas)
varianza = suma_varianza / len(notas)

print("\n" + "="*40)
print(f"Media aritmética de notas: {media:.2f}")
print(f"Varianza de las notas: {varianza:.2f}")

# d) Nota mínima y máxima de ingresantes
if ingresantes_notas:
    # Ordenamos de mayor a menor y tomamos los primeros 150
    ingresantes_notas.sort(reverse=True)
    seleccionados = ingresantes_notas[:vacantes]
    
    print(f"Nota Máxima de ingresante: {max(seleccionados)}")
    print(f"Nota Mínima de ingresante: {min(seleccionados)}")
else:
    print("No hubo ingresantes.")