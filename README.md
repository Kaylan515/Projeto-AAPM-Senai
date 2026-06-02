# Principais contribuidores:
Felipe, Jackelyne, Yasmin, Vinicios e Kaylan

# Instale o requirements.txt

```bash
pip install -r requirements.txt
```

# Iniciar o alembic
```bash
python -m alembic init migrations
```

# Gerar a migrations
```bash
python -m alembic revision --autogenerate -m "Criar tabela usuarios"
```

# Aplicar a migration
```bash
python -m alembic upgrade head
```

# Como rodar o código:
```bash
python -m uvicorn app.main:app --reload

Para as alterações aparecerem nessa máquina nova, elas precisam ter subido para o GitHub antes. Vamos ver se o Git está encontrando essas alterações na nuvem.

Rode este comando:

PowerShell
git status

Rode este comando para ver todas as branches que existem no seu GitHub:

PowerShell
git branch -r

Digite esse comando para ver os últimos commits que essa máquina nova consegue enxergar:

PowerShell
git log --oneline -n 5

git pull origin main

pip install jinja2
pip install python-jose[cryptography]

