from server.server import Server
from urllib.parse import parse_qs

app = Server()

@app.route("/")
def index(request, response):
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    response.body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Saudação</title>
    </head>
    <body>
        <form action="/saudar" method="POST">
            <label for="name">
                Digite seu nome:
                <input type="text" name="name">
            </label>
            <input type="submit">
        </form>
    </body>
    </html>
    """

@app.route("/saudar", methods=["POST"])
def saudar(request, response):
    name = parse_qs(request.body)["name"][0]
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    response.body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Olá!</title>
    </head>
    <body>
        <p>Olá, {name}!</p>
        <a href="/">Tente novamente</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.start(port=3000)