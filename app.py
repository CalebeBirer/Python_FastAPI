import requests  # Importa o módulo requests para fazer requisições HTTP
import json      # Importa o módulo json para trabalhar com dados no formato JSON

# Define a URL de onde os dados JSON serão obtidos
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Faz uma requisição GET para obter os dados do URL
response = requests.get(url)

# Imprime o objeto da resposta HTTP para verificar o resultado inicial
print(response)

# Verifica se a requisição foi bem-sucedida (status code 200 indica sucesso)
if response.status_code == 200:
    
    # Converte o conteúdo da resposta para um objeto JSON (dicionário ou lista no Python)
    dados_json = response.json()
    
    # Inicializa um dicionário vazio para armazenar os dados organizados por restaurante
    dados_restaurante = {}
    
    # Itera sobre cada item dentro dos dados JSON
    for item in dados_json:
        
        # Obtém o nome do restaurante a partir do campo 'Company' no JSON
        nome_do_restaurante = item['Company']
        
        # Se o restaurante ainda não estiver no dicionário, cria uma nova entrada para ele
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        # Adiciona os detalhes do item de menu ao restaurante correspondente
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],            # Nome do item
            "price": item['price'],          # Preço do item
            "description": item['description']  # Descrição do item
        })

# Caso o status da resposta não seja 200, imprime o código de erro
else: 
    print(f'O erro foi {response.status_code}')

# Itera sobre cada restaurante e seus dados
for nome_do_restaurante, dados in dados_restaurante.items():
    
    # Cria um nome de arquivo baseado no nome do restaurante
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    
    # Abre (ou cria) o arquivo correspondente no modo escrita
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        
        # Grava os dados do restaurante no arquivo em formato JSON com indentação de 4 espaços
        json.dump(dados, arquivo_restaurante, indent=4)


#PARA RODAR O SERVIDOR USAR == uvicorn main:app --reload