
#Comprueba si un carácter introducido es una vocal.

  
letra= input("introduce una letra: ")

  
#True si el carácter es una vocal, False en caso contrario.
  
def es_vocal(caracter):
  
  vocales = 'aeiouAEIOU'
  return caracter in vocales

resultado = es_vocal(letra)

print(f"El caracter es vocal? ---> {resultado}")