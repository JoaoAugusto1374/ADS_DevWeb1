# app.py
from flask import Flask, request, make_response

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota principal para uma mensagem de boas-vindas e links de navegação
@app.route('/')
def index():
    return """
    <h1>Bem-vindo à aplicação de demonstração de Cookies!</h1>
    <p>Este sistema simula operações básicas de gerenciamento de estado no lado do cliente.</p>
    <ul>
        <li><a href="/definir-cookie-sessao">Definir cookie de sessão</a></li>
        <li><a href="/definir-cookie-persistente">Definir cookie persistente (expira após 7 dias)</a></li>
        <li><a href="/ler-cookie">Ler o cookie armazenado</a></li>
        <li><a href="/remover-cookie">Remover cookie</a></li>
    </ul>
    """

# Define um cookie de sessão (válido até o navegador ser fechado)
@app.route('/definir-cookie-sessao')
def definir_cookie_sessao():
    # make_response é usado para criar um objeto de resposta que podemos modificar
    resposta = make_response("Cookie de sessão 'usuario_logado' definido com sucesso.")
    # set_cookie é o método que adiciona o cabeçalho 'Set-Cookie' na resposta HTTP.
    # Por padrão, se 'max_age' ou 'expires' não forem definidos, será um cookie de sessão.
    resposta.set_cookie('usuario_logado', 'admin')
    resposta.set_cookie('meu_secure', 'valor', httponly=True)
    resposta.set_cookie('meu_only', 'aqui', secure=True)
    return resposta

# Define um cookie persistente com validade de 7 dias
@app.route('/definir-cookie-persistente')
def definir_cookie_persistente():
    resposta = make_response("Cookie persistente 'token_autenticacao' definido. Ele expira em 7 dias.")
    # Usamos o parâmetro 'max_age' para definir a duração do cookie em segundos.
    # 60 segundos * 60 minutos * 24 horas * 7 dias = 604800 segundos.
    resposta.set_cookie('token_autenticacao', 'abc123DEF456', max_age=60*60*24*7)
    resposta.set_cookie('meu_secure', 'valor', httponly=True)
    resposta.set_cookie('meu_only', 'aqui', secure=True)
    return resposta

# Lê os cookies recebidos na requisição
@app.route('/ler-cookie')
def ler_cookie():
    # request.cookies é um objeto tipo dicionário que contém todos os cookies
    # que o navegador enviou com a requisição atual.
    # Usamos .get() para evitar erros se o cookie não existir.
    usuario = request.cookies.get('usuario_logado', 'Nenhum cookie de sessão encontrado.')
    token = request.cookies.get('token_autenticacao', 'Nenhum cookie persistente encontrado.')
    return f"""
    <h1>Cookies Atuais</h1>
    <p>Valor do cookie de sessão <strong>'usuario_logado'</strong>: <strong>{usuario}</strong></p>
    <p>Valor do cookie persistente <strong>'token_autenticacao'</strong>: <strong>{token}</strong></p>
    <p><a href="/">Voltar à Página Inicial</a></p>
    """

# Remove os cookies do navegador
@app.route('/remover-cookie')
def remover_cookie():
    resposta = make_response("Cookies 'usuario_logado' e 'token_autenticacao' removidos com sucesso.")
    # Para remover um cookie, definimos seu valor como vazio e sua data de expiração no passado (expires=0).
    # O navegador, ao receber este Set-Cookie, entende que deve apagar o cookie.
    resposta.set_cookie('usuario_logado', '', expires=0)
    resposta.set_cookie('token_autenticacao', '', expires=0)
    return resposta

@app.route('/contador-visitas')
def contador():
    

# Bloco para rodar a aplicação quando o script é executado diretamente
if __name__ == '__main__':
    app.run(debug=True) # debug=True ativa o modo de depuração (reinicia ao salvar e mostra erros)