n = int(input("Dime cuantas palabras tiene la lista: "))
lista1=[]
for i in range(0,n):
    palabra = input(f"Di la palabra {i+1}: ")
    lista1.append(palabra)
print(f"La lista creada es: {lista1}")
lista_ordenada=list(sorted(lista1))
print(f"La lista ordenada alfabeticamente es: {lista_ordenada}")
