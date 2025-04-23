from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print('Recebido no webhook:', data)
    return jsonify({'status': 'sucesso', 'mensagem': 'Webhook recebido!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
