#Encuentra un nombre en la lista de saiyajins
saiyajins = ['Trunks', 'Son Gohan', 'Vegeta', 'Kakarotto', 'Goku', 'Nappa']
nombre = input('Introduzca el nombre de un Saiyajin: ')
posicion = 0
iteraciones = 0

for saiyajin in saiyajins:
    if saiyajin == nombre:
        print(nombre, 'está en la posición:', posicion)
        break
    else:
        posicion = posicion + 1
    iteraciones = iteraciones + 1
else:
    print(nombre, 'NO se ha encontrado en la lista de Saiyajins')

print('Se han hecho', iteraciones, 'iteraciones.')