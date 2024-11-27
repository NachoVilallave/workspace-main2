def mcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mcd_resultado = mcd(num1, num2)

print(f"El MCD de {num1} y {num2} es: {mcd_resultado}")
