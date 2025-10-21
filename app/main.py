from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


class ItemIn(BaseModel):
    text: str


# In-Memory-Liste zum Speichern der Todos
items = [
    {"id": 1, "text": "Milch kaufen"},
    {"id": 2, "text": "E-Mail an Chef"},
    {"id": 3, "text": "Workout im Gym"}
]


@app.get("/items")
def list_items():
    return items


@app.post("/items", status_code=201)
def create_item(payload: ItemIn):
    if not payload.text:
        raise HTTPException(status_code=400, detail="text required")
    item = {"id": len(items) + 1, "text": payload.text}
    items.append(item)
    return item
