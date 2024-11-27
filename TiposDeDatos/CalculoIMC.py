#Vamos a realizar un programa para calcular tu indice de masa corporal
peso=float(input("introduzca su peso en kilogramos: "))
altura=float(input("introduzca su altura en metros: "))
imc=round(peso/(altura*altura),2)
print (f"tu imc es {imc}")

if imc <= 18.5 : 
    print("tienes insuficiencia ponderal")
elif imc > 18.5 :
    if imc < 24.9:
        print("tienes un peso normal")
    elif imc <= 29.9:
        print("tiens sobrepeso")
    else:
        print("tienes hola mundo")
