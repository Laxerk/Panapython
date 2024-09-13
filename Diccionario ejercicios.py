def sacarContraseña (contraseña):
    caracteres = len(contraseña) >= 10
    mayuscula = any(d.isupper() for d in contraseña)
    minuscula = any(d.islower() for d in contraseña)
    numero = any(d.isdigit() for d in contraseña)
    caracterEspecial = any(d in ".,_-{[]}^*+~¨´¿¡'?=/&%$#!" for d in contraseña)

    errores = []
    if not caracteres:
        errores.append("Tu contraseña tiene que tener mas de 10 caracteres")
    if not mayuscula:
        errores.append("Tu contraseña tiene que tener al menos una mayuscula")
    if not minuscula:
        errores.append("Tu contraseña tiene que tener al menos una minuscula")
    if not numero:
        errores.append("Tu contraseña tiene que tener al menos un numero")
    if not caracterEspecial:
        errores.append("Tu contraseña tiene que tener un caracter especial")
    if not errores:
        return"Tu contraseña es segura"
    else:
        return f'Tu contraseña es insegura, tiene los siguientes errores\n: {errores}'

contraseñaEZ = input("Coloca una contraseña: ")
validacion = sacarContraseña(contraseñaEZ)
print(validacion)

