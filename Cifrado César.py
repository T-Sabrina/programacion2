#Cifrado César

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Ingresa tu mensaje: ")
mensaje = input("Mensaje: ")

print("Ingresa la clave que desees: ")
clave = int(input("Clave: "))

cifrado = ""

for letra in mensaje.upper(): 
    if letra in alfabeto:
        indice = alfabeto.find(letra)
        indice += clave
        if indice >= 26: 
            indice -= 26
        cifrado += alfabeto[indice]
    else:
        cifrado += letra
print(cifrado)
