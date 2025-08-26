from flask import Flask, request, jsonify, Response

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "senhor dos canais", "autor": "jose", "ano": 2000},
    {"id": 2, "titulo": "harry porta", "autor": "paulo", "ano": 3000}
]

@app.route("/livros", methods=["GET"])
def listarLivros():
    if request.headers.get("Accept") == "application/xml":
        xml = "<livros>"
        for l in livros:
            xml += f"<livros><id>{l['id']}</id><titulo>{l['titulo']}</titulo><autor>{l['autor']}</autor><ano>{l['ano']}</ano></livros>"
        xml += "</livros>"
        return Response(xml, mimetype="application/xml")
    return jsonify(livros)

@app.route("/livros", methods=["POST"])
def adicionarLivros():
    dados = request.json
    livros.append(dados)
    return jsonify({"mensagem": "livro adicionado com sucesso", "livro": dados}), 201

if __name__=="__main__":
    app.run(debug=True)