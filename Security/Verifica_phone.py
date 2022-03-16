import phonenumbers

from phonenumbers import geocoder

p_number = input('Entre com o numero de telefone: ')
phone_num = phonenumbers.parse(p_number)
print(geocoder.description_for_number(phone_num, 'pt'))