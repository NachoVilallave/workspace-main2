

#Imprime un histograma a partir de una lista de números enteros.

def histograma(numeros):
  
  for numero in numeros:
    print("*" * numero)

# Solicitar al usuario la cantidad de números
cantidad_numeros = int(input("Ingrese la cantidad de números: "))

# Crear una lista vacía para almacenar los números
numeros = []

# Solicitar al usuario los números
print("Ingrese los números:")
for i in range(cantidad_numeros):
  numero = int(input(f"Número {i+1}: "))
  numeros.append(numero)

# Imprimir el histograma
histograma(numeros)