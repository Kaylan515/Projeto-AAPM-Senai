from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Descobre o caminho real da pasta onde este arquivo main.py está (pasta /app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Configura a pasta dos arquivos estáticos (CSS e JS) que ficam dentro de app/templates/static
# Como "templates" está no mesmo nível que "main.py", usamos o BASE_DIR
static_dir = os.path.join(BASE_DIR, "templates", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 2. Configura a pasta de assets (Imagens, Logos e Fundo) que fica fora da pasta app
# Usamos o os.path.dirname(BASE_DIR) para subir um nível (para a raiz do projeto) e achar a pasta "assets"
assets_dir = os.path.join(os.path.dirname(BASE_DIR), "assets")
app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")


# --- ROTAS DA APLICAÇÃO ---

# Rota para a Página Inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index():
    # Caminho do seu arquivo index.html
    index_path = os.path.join(BASE_DIR, "templates", "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()


# Rota para a Página de Login (login.html)
@app.get("/login", response_class=HTMLResponse)
def read_login():
    # Caminho do seu arquivo login.html dentro da pasta auth
    login_path = os.path.join(BASE_DIR, "templates", "auth", "login.html")
    with open(login_path, "r", encoding="utf-8") as f:
        return f.read()


# Rota para a Página de Cadastro (cadastro.html)
@app.get("/cadastro", response_class=HTMLResponse)
def read_cadastro():
    # Caminho do seu arquivo cadastro.html dentro da pasta auth
    cadastro_path = os.path.join(BASE_DIR, "templates", "auth", "cadastro.html")
    with open(cadastro_path, "r", encoding="utf-8") as f:
        return f.read()


# Permite rodar o projeto diretamente com o comando "python main.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)