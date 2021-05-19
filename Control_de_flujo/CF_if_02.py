#Sabiendo que Goku está en alguna fase del súper saijayin devuelve cómo tiene 
#el pelo.

fase_ss = int(input('¿En qué fase súper saiyajin se encuentra [1/2/3]? '))

if fase_ss <= 1:
    tipo_de_pelo = 'DE PUNTA SUAVE'
elif fase_ss == 2:
    tipo_de_pelo = 'DE PUNTA RADICAL'
else:
    tipo_de_pelo = 'DE PUNTA Y LARGO'
    
print('Goku tiene el pelo ' + tipo_de_pelo)