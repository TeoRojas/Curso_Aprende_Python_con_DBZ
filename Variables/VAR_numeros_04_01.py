#La Tarta de Bulma
gramos_de_la_tarta_de_bulma = 900
porciones_para_goku = 3
porciones_para_vegeta = porciones_para_goku
porciones_para_beerus = 4

porciones_a_dividir_la_tarta = (porciones_para_goku 
                                + porciones_para_vegeta 
                                + porciones_para_beerus)

print("Habrá que dividir la tarta en las siguientes porciones:")
print(porciones_a_dividir_la_tarta)
print("Y para que el sr. Beerus no se enfade, cada porción deberá pesar:")
print(gramos_de_la_tarta_de_bulma / porciones_a_dividir_la_tarta)