from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    id: int
    nome: str
    preco: float

# "Banco de dados" em memória
db: List[Item] = []

# CREATE
@app.post("/items", response_model=Item)
def criar_item(item: Item):
    db.append(item)
    return item

# READ (todos)
@app.get("/items", response_model=List[Item])
def listar_items():
    return db

# READ (por id)
@app.get("/items/{item_id}", response_model=Item)
def obter_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def atualizar_item(item_id: int, item_atualizado: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = item_atualizado
            return item_atualizado
    raise HTTPException(status_code=404, detail="Item não encontrado")

# DELETE
@app.delete("/items/{item_id}")
def deletar_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            del db[index]
            return {"mensagem": "Item deletado"}
    raise HTTPException(status_code=404, detail="Item não encontrado")