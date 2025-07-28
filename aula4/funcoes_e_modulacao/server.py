from http.server import BaseHTTPRequestHandler, HTTPServer
from utils.funcoes import resposta_index, resposta_404
from urllib.parse import urlparse

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            mensagem = resposta_index()
        else:
            mensagem = resposta_404()
        
        #mensagem = "<h1>Servidor rodando com sucesso!</h1>"
        print(mensagem) #Mostra no terminal a mensagem
        self.send_response(200)
        self.send_header("Content-type", "text/html; charsert-utf-8")
        self.end_headers()
        self.wfile.write(mensagem.encode("utf-8"))
    
if __name__ == "__main__":
    host = "localhost"
    porta = 8080
    servidor_http = HTTPServer((host,porta), Servidor)
    print(f"Servidor iniciado em http://{host}:{porta}")
    servidor_http.serve_forever()

