from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.auth import hash_senha, verificar_senha, criar_token

# O prefixo /auth faz todas as rotas começarem com /auth/...
router = APIRouter(prefix="/auth", tags=["Autenticação"])

templates = Jinja2Templates(directory="app/templates")

# Removemos as rotas GET /cadastro e GET /login daqui, 
# pois elas já estão sendo gerenciadas diretamente pelo seu main.py!


# Rota POST de login (Onde o formulário vai disparar os dados)
@router.post("/login")
def fazer_login(
    request: Request,
    username: str = Form(...), # O FastAPI exige 'username' vindo do formulário HTML
    senha: str = Form(...),    # O campo password do HTML vira 'senha' aqui
    db: Session = Depends(get_db),
):
    # Buscar o usuário no banco pelo e-mail informado no campo de username
    usuario = db.query(Usuario).filter_by(email=username).first()

    # Verificar a senha com bcrypt
    senha_correta = (usuario is not None and verificar_senha(senha, usuario.senha_hash))

   # Dentro do método fazer_login no seu auth_controller.py
    if not senha_correta:
        return templates.TemplateResponse(
        request,
        "auth/index.html",  # Adicionado o "auth/" aqui também!
        {"request": request, "erro": "E-mail ou senha incorretos."}
    )
    
    if not usuario.ativo:
        return templates.TemplateResponse(
            request,
            "index.html",
            {"request": request, "erro": "Usuário inativo."}
        )

    # Gera os dados do token JWT
    token_data = {
        "sub": usuario.email,
        "nome": usuario.nome,
        "role": usuario.role,
        "id": usuario.id
    }

    token = criar_token(token_data)

    # Redirecionar com sucesso direto para o Painel Administrativo (/dashboard)
    response = RedirectResponse(url="/dashboard", status_code=302)

    # Salvar o token em cookie seguro Httponly no navegador
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=3600, # Expira em 1 hora
        samesite="lax"
    )

    return response


# Rota de Sair (Logout)
@router.get("/logout")
def sair():
    # Quando deslogar, chuta o admin de volta para a rota /login do main.py
    response = RedirectResponse(url="/login", status_code=302)
    response.delete_cookie("access_token")
    return response