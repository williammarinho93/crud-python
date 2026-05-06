# CRUD com FastAPI (Python)
1. Instalação

``pip install fastapi uvicorn``

2. Rodando o servidor

uvicorn main:app --reload

3. Acesse no navegador:

`` http://127.0.0.1:8000/items ``

# Mapeamento HTTP 

Método HTTP	Rota	Ação

POST	/items	Criar
GET	/items	Listar
GET	/items/{id}	Buscar
PUT	/items/{id}	Atualizar
DELETE	/items/{id}	Deletar