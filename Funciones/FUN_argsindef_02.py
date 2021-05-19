def conquista_de_planetas(*args, **kwargs):
    print('Los planetas que deben ser conquistados son:')
    for planeta in args:
        print('- Planeta', planeta)

    print('El guerrero al que se le ha encargado la tarea es:')
    print(kwargs)
    print('-----------------')

conquista_de_planetas(1, 'Arlia', 35, nombre='Vegeta', numero_guerrero=250)
conquista_de_planetas('Tierra', nombre='Kakarotto', poder_de_combate=5)
