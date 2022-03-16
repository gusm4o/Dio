import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
pais = dados['country']
reg = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegiao :{1}\nPais:{2}\nCiadade:{3}\nOrg.:{0}'.format(org, reg, pais, city, ip))