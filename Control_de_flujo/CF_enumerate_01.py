#Cambiar 'Vegeta' por 'Trunks' en la lista
saiyajins = ['Kakarotto', 'Vegeta', 'Bardock', 'Nappa', 'Raditz']
print('Lista de saiyajins original:')
print(saiyajins)

for n_posicion, saiyajin in enumerate(saiyajins):
    if saiyajin == 'Vegeta':
        saiyajins[n_posicion] = 'Trunks'

print('Lista de saiyajins modificada:')
print(saiyajins)