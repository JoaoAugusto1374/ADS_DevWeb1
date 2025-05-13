from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

PORTA = 8000

class ServidorSimples(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("index.html", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(conteudo.encode("utf-8"))

    def do_POST(self):
        tamanho = int(self.headers["Content-Length"])
        dados = self.rfile.read(tamanho).decode("utf-8")
        campos = parse_qs(dados)

        idade = int(campos.get("idade", ["0"])[0])
        nota = float(campos.get("nota", ["0"])[0])

        if idade >= 18:
            resultado_idade = "Acesso permitido"
        else:
            resultado_idade = "Acesso negado"

        if nota >= 9:
            resultado_nota = "Excelente"
        elif nota >= 6:
            resultado_nota = "Aprovado"
        else:
            resultado_nota = "Reprovado"

        resposta = f"""
        <html>
        <body>
            <h2>Resultado:</h2>
            <p>Idade: {idade} → <strong>{resultado_idade}</strong></p>
            <p>Nota: {nota} → <strong>{resultado_nota}</strong></p>
            <br>
            <a href="/">Voltar</a>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(resposta.encode("utf-8"))

with HTTPServer(("", PORTA), ServidorSimples) as servidor:
    print(f"Servidor rodando em http://localhost:{PORTA}")
    servidor.serve_forever()
