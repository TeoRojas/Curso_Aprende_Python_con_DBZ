#Encuentra la posición de Goku en la lista
saiyajins = ['Trunks', 'Son Gohan', 'Vegeta', 'Kakarotto', 'Goku', 'Nappa']
posicion = 0

for saiyajin in saiyajins:
    if saiyajin == 'Goku':
        print('Goku está en la posición: ', posicion)
        break
    else:
        posicion = posicion + 1

