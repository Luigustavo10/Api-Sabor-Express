import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

# se o o response der 200 mostrar todos os dados json se nao colocar o err e o nome do erro 
if response.status_code == 200:
    dados_json = response.json()
    #Criando Dicionario para filtrar os dados
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']# Filtrando Nome 
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })


else: 
    print(f'O erro foi {response.status_code}')

#Cria os diiconarios do json PARA FAZER OS FILTROS PELO NOME DO RESTAURANTES 
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)

