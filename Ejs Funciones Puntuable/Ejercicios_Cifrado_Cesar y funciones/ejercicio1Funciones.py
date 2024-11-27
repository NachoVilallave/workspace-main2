
#Devuelve el mayor de tres números.

#pido los números
n1 = int(input("El primer número: "))
n2 = int(input("El segundo número: "))
n3 = int(input("El tercer número: "))
  

def max_de_tres(a, b, c):
 
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c

mayor = max_de_tres(n1 , n2 , n3)
#devuelve el resultado
print(f"el número mayor es {mayor}")