cantidad = int(input("Cantidad de dinero en euros: "))

for billete in [20, 10, 5, 1]:
    cantidad_billetes = cantidad // billete
    cantidad = cantidad % billete  # Lo que sobra para el siguiente billete
    if cantidad_billetes > 0:
        print(f"Billetes de {billete}€: {cantidad_billetes}")