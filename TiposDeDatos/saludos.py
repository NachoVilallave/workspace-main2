quieres_saludar="S"
NUM_MAX_SALUDO=4
num_saludo=0
while quieres_saludar=="S":
    print("hola que tal!")
    quieres_saludar =input("Quiere otro saludo? [S/N]")
    while quieres_saludar not in ("S","N"):
        quieres_saludar =input("solo se aceptan los caracteres \"S\" o \"N\". ¿Quieres otro saludo?")
print("Que tenga un buen dia")
