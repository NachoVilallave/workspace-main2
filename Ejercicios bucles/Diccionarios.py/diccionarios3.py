trabajadores = {
    "nombre": "Susana",
    "edad": 26,
    "salario": 1500,
    "ciudad": "Vinaroz"
}

claves= ["nombre", "salario"]
for clave in claves:
    trabajadores.pop(clave)

    print(f"Ahora el contenido del diccionario es: {trabajadores}")
