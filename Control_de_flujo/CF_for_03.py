#Se requiere cambiar Vegeta por Trunks en la siguiente lista de saiyajins
saiyajins = ['Kakarotto', 'Vegeta', 'Bardock', 'Nappa', 'Raditz']
saiyajins_copia = []
for saiyajin in saiyajins:
    if saiyajin != 'Vegeta':
        saiyajins_copia.append(saiyajin)
    else:
        saiyajins_copia.append('Trunks')

print("La lista original era:")
print(saiyajins)
print("La nueva lista modificada es:")
print(saiyajins_copia)