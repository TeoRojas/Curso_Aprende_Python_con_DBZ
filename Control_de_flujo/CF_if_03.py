color_de_pelo = 'NEGRO'
tipo_de_pelo = 'NORMAL'

super_saiyajin = input('¿Está Son Goku en modo súper saiyajin? [s/n] → ')

if super_saiyajin == 's':
    color_de_pelo = 'AMARILLO'
    fase_ss = int(input('¿En qué fase súper saiyajin se encuentra [1/2/3]? '))

    if fase_ss <= 1:
        tipo_de_pelo = 'DE PUNTA SUAVE'
    elif fase_ss == 2:
        tipo_de_pelo = 'DE PUNTA RADICAL'
    else:
        tipo_de_pelo = 'DE PUNTA Y LARGO'
    

print('El color del pelo de Goku en el estado actual es ' + color_de_pelo)
print('El pelo lo tiene ' + tipo_de_pelo)