# {{ values.name }}/app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200

# Adicione suas rotas e lógica de API aqui
@app.route('/', methods=['GET'])
def home():
    return "<h1>Olá, mundo! Esta é a sua API Flask.</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)