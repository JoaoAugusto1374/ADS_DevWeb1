import socket 
from threading import Thread 
from .router import Router 
from .plumbing import Request, Response 

class Server:
    def __init__(self):
        self.router = Router()

    
    def start(self, port=5000, host="", header_size=1024):
        """
        Inicia o servidor socket. Escuta conexões em uma porta definida.
        Cada conexão é tratada em uma thread separada.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            sock.listen(1)
            print(f"Servidor ouvindo em http://{socket.getfqdn()}:{port}/")

            while True:
                conn, addr = sock.accept()
                Thread(
                    target=self.handle_connection,
                    args=(conn, addr, header_size)
                ).start()

    def handle_connection(self, conn, addr, header_size):
        """
        Trata uma requisição recebida por socket.
        Interpreta os dados, encontra a rota e envia a resposta.
        """
        with conn:
            request_bytes = conn.recv(header_size)  # Lê a requisição (bruta)
            response = Response()                   # Prepara uma resposta vazia

            try:
                request = Request(request_bytes, addr)  # Constrói objeto da requisição
                self.router.handle_route(request, response)  # Executa rota
                print(f"{response.status_code} {request.method} {request.path}")
            except Exception as e:
                print("Erro ao processar a requisição:", e)
                response.status_code = 500
                response.body = "<h1>Erro interno no servidor</h1>"

            conn.sendall(response.serialize())  # Envia a resposta para o cliente

    def route(self, path, methods=None):
        """
        Decorador para registrar rotas como no Flask:
        @app.route("/caminho", methods=["GET"])
        """
        if methods is None:
            methods = ["GET"]
        return self.router.add_route(path, methods)






    '''
    def start(self, port=3000, host=""):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSADOR, 1)
            sock.bind((host, port))
            sock.listen(1)
            print(f"Servidor ouvindo em http://localhost:{port}")

            while True:
                conn, addr = socket.accept()
                Tread(target=self.handle_connection, args=(conn, addr, header_sizer)).start()
                
                def handle_connection(self,conn, addr, header_size):

                with conn:
                    request_bytes = conn.recv(header_size)
                    print(f"Conexão recebida de {addr}")
                    print(request_bytes.decode("utf-8"))

                    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Servidor Online</h1>"
                    conn.sendall(response.encode("utf-8"))



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((""), 3000)
sock.listen(1)
print("Aguardando conexões em http://localhost:3000")

conn, addr = sock.accept()
print("Conexão recebida de", addr)

data = conn.recv(1024)
print(data.decode())

response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Ola mundo</h1>"
conn.sendall(responsa.encode("utf-8"))
conn.close()'''