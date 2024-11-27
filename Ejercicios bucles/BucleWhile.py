import random
valor_minimo = int(input("Introduce el valor mínimo: "))
valor_maximo = int(input("Introduce el valor máximo: "))
secreto = random.randint(valor_minimo,valor_maximo)
intentos = 1
print(f"A ver si adivinas un numero entre {valor_minimo} y {valor_maximo}")
n = int(input("Escribe un numero: "))
while n != secreto:
    intentos += 1
    if n < secreto:
        n = int(input("El número es demasiado grande.Intentalo de nuevo: "))
    else:
        n = int(input("El número es demasiado pequeño. Intentalo de nuevo: "))
print(f"¡Enhorabuena! Has adivinado el número en {intentos} intentos.")
