num_empleados = 5  # Cambiado de 50 a 5 para pruebas rápidas
pago_hora = float(input("Cantidad que se paga por hora ordinaria: "))
factor_extra = 1.5

for i in range(1, num_empleados + 1):
    horas = float(input(f"Horas trabajadas por el empleado {i}: "))
    
    if horas <= 40:
        salario = horas * pago_hora
    else:
        # 40 horas normales + (extras por el precio extra)
        horas_extras = horas - 40
        salario = (40 * pago_hora) + (horas_extras * pago_hora * factor_extra)
    
    print(f"El salario del empleado {i} es: {salario}")