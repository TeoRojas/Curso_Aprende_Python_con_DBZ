#Las bolas de dragón NO pueden revivir a una persona que haya sido revivida
#por el mismo deseo anteriormente.

veces_que_resucito_krilin = int(input("¿Cuántas veces ha resucitado Krilin? "))

print("Bulma: ¡¡¡Dragón Mágico, sal y cumple nuestro deseo!!!!")
print("""
    Mi nombre es Shen Long,
    Soy el dragón de las bolas mágicas.
    Me has invocado, así que pide tu deseo...
    """)
print("¡Queremos que resucites a Krilin!")

if veces_que_resucito_krilin >= 1:
    print("""
    Lo siento mucho Krilin ya ha sido resucitado anteriormente, 
    NO PUEDO cumplir tu deseo.
    """)
    print("--- Krilin continúa su letargo... ---")
else:
    print("¡A SUS ÓRDENES!...")
    print("--- ¡¡Krilin despierta de su letargo, ALELUYA!! ---")