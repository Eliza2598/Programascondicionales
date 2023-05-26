#Encuentre el valor maximo dados dos números
x=int(input("Digite un numero "))
y=int(input("Digite otro numero "))
l=int(input("Digite otro numero "))
if x==y==l:
    print("Los numeros ingresados son iguales")
numeros=x,y,l
print("El numero máximo de los tres valores es:",max(numeros))
print("El numero minimo de los tres valores es:",min(numeros))