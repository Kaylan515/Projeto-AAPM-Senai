from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.controllers import auth_controller
from app.controllers import admin_controller
from app.controllers import movimentacao_controller
from app.controllers import produto_controller
from app.controllers import categoria__controller
from app.controllers import cliente_controller
from app.controllers import pdv_controller
import os

app = FastAPI()

# 🟢 Inclui apenas os routers dos controllers que você possui na pasta
app.include_router(auth_controller.router)
app.include_router(admin_controller.router)
app.include_router(movimentacao_controller.router)
app.include_router(produto_controller.router)
app.include_router(categoria__controller.router)
app.include_router(cliente_controller.router)
app.include_router(pdv_controller.router)

# Descobre o caminho real da pasta onde este arquivo main.py está (pasta /app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🛠️ CORREÇÃO DEFINITIVA DO STATIC: Aponta para a pasta static real (onde tem CSS e assets)
static_dir = os.path.join(BASE_DIR, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Configura o Jinja2 para ler os arquivos HTML corretamente da pasta templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


# --- ROTAS DA APLICAÇÃO ---


# --- ROTAS DA APLICAÇÃO (USANDO JINJA2 CORRETAMENTE) ---

# --- ROTAS DA APLICAÇÃO (USANDO JINJA2 CORRETAMENTE) ---

# 1. Página Inicial Pública (Agora usa o arquivo 'page--1.html')
# Quando o cliente acessar "http://localhost:8000/", ele vai cair aqui
# --- ROTAS DA APLICAÇÃO (USANDO JINJA2 COM A PASTA AUTH CORRETA) ---

# 1. Página Inicial Pública (Sua vitrine/apresentação)
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    context = {"request": request}
    # Como o arquivo está dentro de templates/auth/, passamos o caminho relativo
    return templates.TemplateResponse(request=request, name="auth/page--1.html", context=context)


# 2. Página de Login Administrativo (Onde o admin digita e-mail/senha)
@app.get("/login", response_class=HTMLResponse)
def read_login(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="auth/index.html", context=context)


# 3. Painel Administrativo (Controle interno de estoque)
@app.get("/dashboard", response_class=HTMLResponse)
def read_dashboard(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="auth/dashboard.html", context=context)


# 4. Página de Visualização dos Clientes (Catálogo/Stock de consulta)
@app.get("/visualizacao", response_class=HTMLResponse)
def read_client_view(request: Request):
    context = {"request": request}
    return templates.TemplateResponse(request=request, name="auth/page2--.html", context=context)