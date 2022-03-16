from bs4 import BeautifulSoup
import requests
site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())
temperatura = soup.find("span", class_="teste")
print(temperatura)
print(soup.title.string)
