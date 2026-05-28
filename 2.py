a = int(input("ingrese un numero:"))

if a > 10:
    print("si es mayor a 10")
else:
    print("no es mayor a 10")




b = int(input("ingrese un numero:"))

if b > 0:
   if (a % 2) == 0:
    print(f"el numero {b} es par")
   else:
    print(f"el numero {b} es impar")
else:
   if(b < 0):
      if (a % 2) == 0:
         print(f"el numero {b} es par negativo")
      else:
         print(f"el numero {b} es impar negativo")

   else:
    print(f"el numero {b} es neutro")