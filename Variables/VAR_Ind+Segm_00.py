dbz = 'Dragon Ball Z'

#Imprime el valor cada '1' índice - 0,1,2,3,4,...,12
print('0º--> ' + dbz[:]) 
print('1º--> ' + dbz[::1]) 
#Imprime el valor cada '2' índices - 0,2,4,6,8,10,12
print('2º--> ' + dbz[::2]) 
#Imprime el valor cada '3' índices - 0,3,6,9,12
print('3º--> ' + dbz[::3]) 
#Imprime de los primeros 6 carácteres el valor cada '3' índices: 0,3
print('4º--> ' + dbz[:6:3]) 
#Imprime de los 6 últimos carácteres el valor cada '2' índices: 
#-6,-4,-2, o 7,9,11; El tercer carácter es un espacio en blanco.
print('5º--> ' + dbz[-6::2])