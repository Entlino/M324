from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

class ItemIn(BaseModel):
    text: str

items = []

@app.get("/items")
def list_items():
    return items

@app.post("/items", status_code=201)
def create_item(payload: ItemIn):
    if not payload.text:
        raise HTTPException(status_code=400, detail="text required")
    item = {"id": len(items)+1, "text": payload.text}
    items.append(item)
    return item

# End of file: app/main.py

# SMS-7: Healthcheck-Endpoint implementiert
