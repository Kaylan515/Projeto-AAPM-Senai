from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.controllers import auth_controller
from app.controllers import admin_controller
from app.controllers import movimentacao_controller
from app.controllers import produto_controller
from app.controllers import categoria__controller
import os

app = FastAPI()

# 🟢 Inclui apenas os routers dos controllers que você possui na pasta
app.include_router(auth_controller.router)
app.include_router(admin_controller.router)
app.include_router(movimentacao_controller.router)
app.include_router(produto_controller.router)
app.include_router(categoria__controller.router)

# Descobre o caminho real da pasta onde este arquivo main.py está (pasta /app)
# 1. Configura a pasta dos arquivos estáticos (CSS e JS)
# Descobre o caminho real da pasta onde este arquivo main.py está (pasta /app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🛠️ CORREÇÃO DA LINHA DO STATIC: Apontando direto para onde sua pasta CSS está!
static_dir = os.path.join(BASE_DIR, "templates")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# 2. Configura a pasta de assets (Imagens, Logos e Fundo) fora da pasta app
assets_dir = os.path.join(os.path.dirname(BASE_DIR), "assets")
app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

# 3. Configura o Jinja2 para ler os arquivos HTML corretamente
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# --- ROTAS DA APLICAÇÃO ---


# --- ROTAS DA APLICAÇÃO (USANDO JINJA2 CORRETAMENTE) ---

# Página Inicial (index.html)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="index.html", context=context)


# Página de Login (login.html)
@app.get("/login", response_class=HTMLResponse)
def read_login(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="auth/login.html", context=context)


# Página de Cadastro (cadastro.html)
@app.get("/cadastro", response_class=HTMLResponse)
def read_cadastro(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="auth/cadastro.html", context=context)


# Painel Administrativo (dashboard.html)
@app.get("/dashboard", response_class=HTMLResponse)
def read_dashboard(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="dashboard.html", context=context)