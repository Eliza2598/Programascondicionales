#Encuentre el valor maximo dados dos números
try:
    x=int(input("Digite un numero "))
    y=int(input("Digite otro numero "))
    if x < y:
        print(x," Es menor que ",y)
    if x > y:
        print(x,"Mayor que",y)
    if x==y:
        print("Los numeros ingresados son iguales")
    numeros=x,y
    print("El numero maximo de los dos valores es:",max(numeros))
    print("El numero minimo de los dos valores es:",min(numeros))
except:
    print("Error en la entrada del usuario .")