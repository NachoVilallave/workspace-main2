n = int(input("Dime un numero: "))
lista=[]

for i in range(1,n+1):
    if i%2==0:
        lista.append(i)
print(f"Pares hasta el {n}: {lista}")
