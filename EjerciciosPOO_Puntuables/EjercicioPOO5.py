class Usuario:
   def __init__(self, nombre, apellido, correo_electronico, nombre_usuario, intentos_inicio = 0):
       self.nombre = nombre
       self.apellido = apellido
       self.correo_electronico = correo_electronico
       self.nombre_usuario = nombre_usuario
       self.intentos_inicio = intentos_inicio

   def describir_usuario(self):
       print(f'Nombre: {self.nombre}')
       print(f'Apellido: {self.apellido}')
       print(f'Correo electrónico: {self.correo_electronico}')
       print(f'Nombre de usuario: {self.nombre_usuario}')

   def saludar_usuario(self):
       print(f'Hola, {self.nombre}')

   def incrementar_intentos_inicio(self):
       self.intentos_inicio += 1

   def restablecer_intentos_inicio(self):
       self.intentos_inicio = 0

usuario1 = Usuario('Nacho', 'Vilallave', 'nacvilvil@alu.edu.gva.es', 'Nachito')

usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()

usuario1.saludar_usuario()
usuario1.describir_usuario()

print(f'Intentos de inicio: {usuario1.intentos_inicio}')

usuario1.restablecer_intentos_inicio()

print(f'Reseteo de intentos --> Intentos de inicio:: {usuario1.intentos_inicio}')