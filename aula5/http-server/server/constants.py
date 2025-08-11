allowed_methods = {
    "GET", #Recupera dados do servidor(Carregar uma página de exemplo)
    "HEAD", #Igual ao Get mas sem o corpo da respota, só cabeçalhos
    "POST", #Envia dados para o servidor(ex: formulários)
    "PUT", #Substitui um recurso do servidor
    "DELETE", #Remove um recurso do servidor
    "CONNECT", #estabelece um túnel para comunicação segura(HTTPS)
    "OPTIONS", #Retorna os métodos suportados pelo servidor criado
    "TRACE", #Coloca a requisição para diagnóstico
    "PATCH" #Atualiza parcialmente um recurso
}

status_codes = {
    100: "Continuar",
    101: "Trocando protocolos",
    200: "OK",
    201: "Criado",
    202: "Aceito",
    203: "Informação não-autorizada",
    204: "Sem conteúdo",
    205: "Redefinir conteúdo",
    206: "Conteúdo Parcial",
    300: "Múltiplas escolhas",
    301: "Movido Permanentemente",
    302: "Encontrado",
    303: "Ver outro",
    304: "Não Modificado",
    305: "User proxy",
    307: "Redirecionamento temporário",
    400: "Requisição inválida",
    401: "Não autorizado",
    402: "Pagamento necessário",
    403: "Proibido",
    404: "Não encontrado",
    405: "Método não permitido",
    406: "Não aceitável",
    407: "autenticação de proxy necessária",
    408: "tempo de requisição esgotado",
    409: "conflito",
    410: "removido",
    411: "comprimento necessário",
    412: "Pré-condição falhou",
    413: "carga muito grande",
    414: "URI muito longo",
    415: "tipo de mídia não suportado",
    416: "faixa não satisfatória",
    417: "expectativa falhou",
    418: "Sou um bule de chá",
    426: "Atualização necessária",
    500: "erro interno no servidor",
    501: "não implementado",
    502: "gateway inválido",
    503: "serviço indisponível",
    504: "tempo de gateway esgotado",
    505: "Versão http não suportada"   
}