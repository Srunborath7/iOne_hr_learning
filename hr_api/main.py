from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

class Item(BaseModel):
    name: str
    price: float
db: dict[int, Item] = {}

@app.post("/items/{item_id}", status_code = 201)
def create(item_id: int, item: Item):
    if item_id in db:
        raise HTTPException(400,"Item already exists")
    db[item_id] = item
    return item

@app.get("/items/{item_id}")
def read(item_id: int):
    if item_id not in db:
        raise HTTPException(400,"Item not found")
    return db[item_id]

@app.put("/items/{item_id}")
def update(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(400,"Item not found")
    db[item_id] = item
    return item

@app.delete("/items/{item_id}")
def delete(item_id: int):
    if item_id not in db:
        raise HTTPException(400,"Item not found")
    del db[item_id]
    return ("Deleted item successfully")