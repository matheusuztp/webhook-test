import requests

url = 'http://localhost:5000/webhook'
data = {
    'evento': 'teste',
    'mensagem': 'Olá, webhook!'
}

response = requests.post(url, json=data)

print('Status code:', response.status_code)
print('Resposta:', response.json())
