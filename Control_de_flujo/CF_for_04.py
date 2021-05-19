#Elimina los espacios en blanco de un nombre
nombre = 'Son Gohan'
nombre_copia = ''

for caracter in nombre:
    if caracter != ' ':
        nombre_copia += caracter

print("El nombre original era:")
print(nombre)
print("El nombre sin espacios es:")
print(nombre_copia)