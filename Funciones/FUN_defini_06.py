def saiyajin_top():
    saiyajin_mas_poderoso = 'Broly' #variable LOCAL
    print('El saiyajin más poderoso es:', saiyajin_mas_poderoso)

saiyajin_mas_poderoso = 'Son Goku' #variable GLOBAL

print('El saiyajin más poderoso es:', saiyajin_mas_poderoso)
saiyajin_top()
print('El saiyajin más poderoso es:', saiyajin_mas_poderoso)
