#Primer Problema
palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
numeroPalabra = 0
for palabra in palabras:
    if palabra == "Python":
        numeroPalabra += 1
    else:
        numeroPalabra == 0
print(f'El numero de veces que aparece la palabra es de {numeroPalabra}')

#Segundo problema
frases = ["hola", "mundo", "python", "es", "genial"]
cambio = [palabra.swapcase() for palabra in frases]
cambioMayus = " ".join(cambio)
print(cambioMayus)

#Tercer problema
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
mostrarPalabras = [palabra for palabra in palabras if len(palabra) >= 4]
pala = " ".join(mostrarPalabras)
print(f'Las palabras ahora son {pala}')
    
#Cuarto problema
numeros = [15, 22, 8, 34, 9, 6, 17]
maximo = [palabra for palabra in numeros if palabra > palabra]
print(maximo)