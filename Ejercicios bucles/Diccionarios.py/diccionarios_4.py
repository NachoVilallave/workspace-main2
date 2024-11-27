diccionario = {'a': 100, 'b': 200, 'c': 300}
numero=int(input("digame un numero: "))
if numero in diccionario.values():
    print(f'{numero} esta en el diccionario')
else:
    print(f'{numero} no esta en el diccionario')
