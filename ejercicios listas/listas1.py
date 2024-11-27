n = int(input("Dime cuantas palabras tiene la lista: "))
lista=[]
for i in range(1,n+1):
    palabra = input(f"Di la palabra {i}: ")
    lista.append(palabra)
print(f"La lista creada es: {lista}")

palabra_eliminar = input("palabra a eliminar: ")
lista.remove(palabra_eliminar)

while palabra_eliminar in lista:
    lista.remove(palabra_eliminar)
print(f"Nueva lista: {lista}")
