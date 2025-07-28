from pathlib import Path 

def resposta_index():
    #return "<h1>Bem vindo ao servidor modularizado!</h1>"
    caminho = Path("index.html")
    if caminho.exists():
        return caminho.read_text(encoding="utf-8")
    else:
        return "<h1>index.html não encontrado</h1>"
def resposta_404():
    return "<h1>404 - Página não encontrada</h1>"
