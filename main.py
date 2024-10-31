from fastapi import FastAPI, Query  # Importa o FastAPI para criar a API e Query para lidar com parâmetros de consulta
import requests  # Importa o módulo requests para fazer requisições HTTP

# Instancia a aplicação FastAPI
app = FastAPI()

# Define uma rota GET para a URL /api/hello
@app.get('/api/hello')
def hello_world():
    # Retorna uma mensagem simples "Hello World"
    return {'Hello': 'World'}

# Define uma rota GET para a URL /api/restaurantes/ que aceita um parâmetro opcional 'restaurante'
@app.get('/api/restaurantes/')
def get_restaturantes(restaurante: str = Query(None)):
    # URL de onde os dados de restaurantes serão obtidos
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    
    # Faz uma requisição HTTP GET para obter os dados JSON de restaurantes
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (status code 200)
    if response.status_code == 200:
        # Converte o conteúdo da resposta para JSON
        dados_json = response.json()

        # Se nenhum restaurante foi especificado como parâmetro, retorna todos os dados
        if restaurante is None:
            return {'Dados': dados_json}
        
        # Se um restaurante foi especificado, inicializa uma lista para armazenar os itens do restaurante
        dados_restaurante = []
        
        # Itera sobre os dados JSON para filtrar os itens do restaurante especificado
        for item in dados_json:
            # Verifica se o nome do restaurante no item corresponde ao restaurante fornecido como parâmetro
            if item['company'] == restaurante:
                # Adiciona os itens correspondentes a esse restaurante na lista 'dados_restaurante'
                dados_restaurante.append({
                    "item": item['Item'],           # Nome do item do menu
                    "price": item['price'],         # Preço do item
                    "description": item['description']  # Descrição do item
                })

        # Retorna o nome do restaurante e seu cardápio filtrado
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

    # Caso a requisição HTTP não tenha sucesso, retorna o código de erro e o texto da resposta
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
