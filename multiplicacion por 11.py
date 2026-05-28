n_str = input("Ingresa el número para multiplicar por 11: ")
m = len(n_str)

# El último dígito (unidades) queda igual
resultado = n_str[-1]

# Sumamos dígitos adyacentes de derecha a izquierda
llevo = 0
for i in range(m - 1, 0, -1):
    suma = int(n_str[i]) + int(n_str[i-1]) + llevo
    resultado = str(suma % 10) + resultado
    llevo = suma // 10

# El primer dígito más lo que se lleve
resultado = str(int(n_str[0]) + llevo) + resultado

print(f"Resultado: {resultado}")