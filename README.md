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

# Exemplo de como seria uma conexao com PostgreSQL usando SQLAlchemy:
#
# 1. Instale as dependencias:
#    pip install sqlalchemy psycopg2-binary
#
# 2. Configure a URL de conexao:
#    from sqlalchemy import create_engine
#    from sqlalchemy.orm import sessionmaker, Session
#    from fastapi import Depends
#
#    DATABASE_URL = "postgresql://usuario:senha@localhost:5432/nome_do_banco"
#
#    engine = create_engine(DATABASE_URL)
#    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# 3. Crie uma funcao para abrir e fechar a sessao do banco:
#    def get_db():
#        db_postgres = SessionLocal()
#        try:
#            yield db_postgres
#        finally:
#            db_postgres.close()
#
# 4. Use a sessao do banco nas rotas com Depends:
#    @app.get("/items-postgres")
#    def listar_items_postgres(db_postgres: Session = Depends(get_db)):
#        # Exemplo:
#        # return db_postgres.query(ItemModel).all()
#        # ItemModel seria uma classe/tabela criada com SQLAlchemy.
#        return {"mensagem": "Aqui voce consultaria os items no PostgreSQL"}
#
#    @app.post("/items-postgres")
#    def criar_item_postgres(item: Item, db_postgres: Session = Depends(get_db)):
#        # Exemplo:
#        # novo_item = ItemModel(id=item.id, nome=item.nome, preco=item.preco)
#        # db_postgres.add(novo_item)
#        # db_postgres.commit()
#        # db_postgres.refresh(novo_item)
#        # return novo_item
#        return {"mensagem": "Aqui voce salvaria o item no PostgreSQL"}
#
# Observacao: este projeto ainda usa uma lista em memoria apenas para estudo.