n = int(input("¿Cuántos números vas a introducir? "))

maximo = n
minimo = n
suma = 0

for i in range(n):
  numero = float(input(f"Introduce el número {i+1}: "))

  if numero > maximo:
    maximo = numero
  elif numero < minimo:
    minimo = numero

  suma += numero

media = suma / n

print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")
print(f"La media de los números es: {media}")
