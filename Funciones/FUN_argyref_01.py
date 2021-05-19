def cambia_nombre(lista):
    for i, nombre in enumerate(lista):
        lista[i] = 'Vegeta'

lista = ['Goku', 'Vegeta', 'Broly']

print(*lista)
cambia_nombre(lista)
print(*lista)

