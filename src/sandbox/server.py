from flask import Flask, request, jsonify
import sys
import traceback

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_stripe_webhook():
    try:
        event = request.json
        # ERRO INTENCIONAL PARA O AGENTE CORRIGIR: Aceder a uma chave inexistente
        customer_id = event['data']['object']['customer_id_missing']
        return jsonify({"status": "success", "customer": customer_id}), 200
    except Exception as e:
        # Retorna o rastreio detalhado para o motor de auditoria e AST analisar
        tb = traceback.format_exc()
        return jsonify({"error": str(e), "traceback": tb}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
