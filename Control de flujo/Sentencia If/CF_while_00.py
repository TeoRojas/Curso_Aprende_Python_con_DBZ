poder_base_goku = 5000
goku = 'Goku:\t¡Vas a pagar por esto!'
gohan = 'Gohan:\tPapá, ¡eres increíble!'
nappa = [
    'Nappa:\t',
    '¿Qué es esa mirada en tu cara?',
    'No me gusta',
    'Vegeta, ¿Cuál es el poder de combate de Kakarotto?',
    '¿¡Superior a 8000!?',
    'Tiene que ser un error',
    '¡¡¡Es una avería!!!'
    ]
vegeta = [
    'Vegeta:\t',
    'Poder de combate 7000...',
    'Poder de combate 8000...',
    '¡Imposible!',
    '¡Superior a 8000!'
    ]

print(nappa[0] + nappa[1])
print(nappa[0] + nappa[2])
print(goku)
print("\n--GOKU INCREMENTA SU PODER...--\n")

while poder_base_goku < 8500:
    if poder_base_goku == 6000:
        print(gohan)
    if poder_base_goku == 7000:
        print(vegeta[0] + vegeta[1])
    if poder_base_goku == 8000:
        print(vegeta[0] + vegeta[2])
    if poder_base_goku == 8200:
        print(vegeta[0] + vegeta[3])
    poder_base_goku = poder_base_goku + 1

print(nappa[0] + nappa[3])
print(vegeta[0] + vegeta[4])
print(nappa[0] + nappa[4])
print(nappa[0] + nappa[5]+ ', ' + nappa[6])