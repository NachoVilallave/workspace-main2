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

usuario1 = Usuario('Alvaro', 'Garcia', 'alvgarmar@alu.edu.gva.es', 'Alvapoor')

usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()
usuario1.incrementar_intentos_inicio()

usuario1.saludar_usuario()
usuario1.describir_usuario()

print(f'Intentos de inicio: {usuario1.intentos_inicio}')

usuario1.restablecer_intentos_inicio()

print(f'Reseteo de intentos --> Intentos de inicio:: {usuario1.intentos_inicio}')

class Admin:
    def __init__(self, nombre, apellido, correo_electronico, nombre_usuario, intentos_inicio = 0, privilegios="Puede borrar comentarios, Administrar usuarios."):
       self.nombre = nombre
       self.apellido = apellido
       self.correo_electronico = correo_electronico
       self.nombre_usuario = nombre_usuario
       self.intentos_inicio = intentos_inicio
       self.privilegios = privilegios
    

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
       
    def mostrar_privilegios(self):
        print(f"Los privilegios del usuario son: {self.privilegios}.")
        
        
        

    
Admin1 = Admin('Nacho', 'Vilallave', 'nacvilvil@alu.edu.gva.es', 'Nacho_Admin',)

Admin1.incrementar_intentos_inicio()
Admin1.incrementar_intentos_inicio()
Admin1.incrementar_intentos_inicio()

Admin1.saludar_usuario()
Admin1.describir_usuario()
Admin1.mostrar_privilegios()



