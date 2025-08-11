from flask import Flask, request, make_response, send_from_directory, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(".", "index.html")

@app.route('/sessao', methods=['GET', 'POST'])
def autenticacao_sessao():
    username = 'joao'
    password = '123'
    
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        if nome == username and senha == password:
            mensagem = "Cookie de sessão 'usuario_logado' definido com sucesso."
            html = f"""
                <html>
                    <head><title>Login</title></head>
                    <body>
                        <h1>{mensagem}</h1>
                        <p>Você está logado como: <b>admin</b></p>
                    </body>
                </html>
            """
            resposta = make_response(render_template_string(html))
            resposta.set_cookie('usuario_logado', 'admin')
            return resposta
        else:
            return "usuário ou senha inválidos" 
    return send_from_directory("." , "login.html")

if __name__ == '__main__':
    app.run(debug=True)