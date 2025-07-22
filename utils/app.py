from flask import Flask, request, jsonify
from flask_cors import CORS
import os, json
import functions
import estoque

caminhoEstoque = "./estoque.json"
app = Flask(__name__)
CORS(app)

@app.route('/realizarPedidos', methods=['POST']) # recebe o pedido do Front-End
def receberPedido():
    try:
        dadosPedido = request.json
        functions.salvarPedido(dadosPedido)
        estoque.contabilizarEstoque(dadosPedido)
        print(f"Informações salvas: {dadosPedido}")
        return jsonify({"mensagem": "Conectado ao servidor com sucesso\nInformações salvas com sucesso"})
    except Exception as e:
        print("Erro ao processar pedido:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/carregarEstoque', methods=['GET']) # envia o estoque ao Front-End
def carregarEstoque():
    try:
        if os.path.exists(caminhoEstoque):
            with open(caminhoEstoque, 'r') as estoque:
                estoque = json.load(estoque)
            return jsonify(estoque)
        else:
            return jsonify({"error":"Estoque não encontrado"})
    except Exception as e:
        print("Erro ao carregar estoque:", e)
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)