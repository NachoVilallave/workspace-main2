import math

#Calcular el área y el perímetro de una circunferencia.
  
def area_y_perimetro_circulo(radio):
  
  area = math.pi * radio**2
  perimetro = 2 * math.pi * radio
  return area, perimetro


radio = float(input("Ingrese el radio de la circunferencia: "))
area, perimetro = area_y_perimetro_circulo(radio)
print(f"El área de la circunferencia es: {area:.2f}")
print(f"El perímetro de la circunferencia es: {perimetro:.2f}")