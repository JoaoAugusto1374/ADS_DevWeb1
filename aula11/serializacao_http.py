from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = [
        {"id": 1, "nome": "Pedro", "email": "pedro@gmail.com"},
        {"id": 2, "nome": "João", "email": "joao@gmail.com"}
    ]
    return jsonify(usuarios)

# Nova rota POST
@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    dados = request.json  # desserializa automaticamente
    dados["cursos"] = None
    return jsonify({"mensagem": "Usuario Cadastrado", "usuario": dados}), 201

if __name__ == "__main__":
    app.run(debug=True)