pila_de_mis_mangas = ['Tomo1', 'Tomo3', 'Tomo5' ]

print('Mi pila de mangas antes de que me regalen el nuevo:')
print(pila_de_mis_mangas)

print('Mi pila de mangas después de que me regalen el tomo 2:')
pila_de_mis_mangas.append('Tomo2')
print(pila_de_mis_mangas)

print('Me piden prestado un momento el tomo 2, mi pila de mangas queda:')
pila_de_mis_mangas.pop()
print(pila_de_mis_mangas)
