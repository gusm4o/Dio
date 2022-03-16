import requests
def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    dado_cep = response.json()
    print(dado_cep['logradouro'])
    return dado_cep

def return_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def return_text(url):
    response = requests.get('https://www.google.com')
    print(response.text)
    return response.text
if __name__ == '__main__':
    retorna_cep('78300015')
    dados_pokemon = return_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_female'])
    return_text('https://www.google.com')