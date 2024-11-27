def Login(username, password, intentos):
  
  if username == "usuario1" and password == "asdasd":
    return True
  else:
    intentos += 1
    return False, intentos


intentos = 0
for i in range(3):
  username = input("Ingrese nombre de usuario: ")
  password = input("Ingrese contraseña: ")

  result, intentos = Login(username, password, intentos)

  if result:
    print("Inicio de sesión exitoso!")
    break
  else:
    print(f"Nombre de usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}")

if intentos == 3:
  print("Demasiados intentos. Acceso denegado.")