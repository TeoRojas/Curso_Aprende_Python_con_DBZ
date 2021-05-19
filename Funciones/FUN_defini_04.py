def obten_nombre_fusion_metamorana(guerrero_1, guerrero_2):
    return guerrero_1[:2] + guerrero_2[2:]

saiyajin_1 = 'Goku'
saiyajin_2 = 'Vegeta'

fusion = obten_nombre_fusion_metamorana(saiyajin_1, saiyajin_2)

print('El Nombre de la fusión de', saiyajin_1, 'y', saiyajin_2, 'es:')
print(fusion)