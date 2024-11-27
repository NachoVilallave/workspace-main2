def segundos_a_hms(segundos):
 
  horas = segundos // 3600
  segundos_restantes = segundos % 3600
  minutos = segundos_restantes // 60
  segundos = segundos_restantes % 60
  return horas, minutos, segundos

def hms_a_segundos(horas, minutos, segundos):
 
  return horas * 3600 + minutos * 60 + segundos


while True:
  print("\nMenú:")
  print("1. Convertir a segundos")
  print("2. Convertir a horas, minutos y segundos")
  print("3. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    total_segundos = hms_a_segundos(horas, minutos, segundos)
    print(f"El tiempo en segundos es: {total_segundos}")

  elif opcion == "2":
    segundos = int(input("Ingrese los segundos: "))
    horas, minutos, segundos = segundos_a_hms(segundos)
    print(f"El tiempo en horas, minutos y segundos es: {horas}:{minutos}:{segundos}")

  elif opcion == "3":
    break

  else:
    print("Opción inválida. Por favor, ingrese una opción válida.")