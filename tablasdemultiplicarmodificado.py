#Tablas de multiplicar
multiplos=""
while not isinstance(multiplos,int):
    try:
        multiplos=int(input("Digite un numero "))
    except:
        print("Error en la entrada del usuario.")
if isinstance(multiplos,int):
    numero = 1
    while numero <= 12:
        print (multiplos, "*" ,numero, " = " ,numero *multiplos)
        numero = numero + 1