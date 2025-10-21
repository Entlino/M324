import pytest
import httpx
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_items_end_to_end_flow():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        # Startliste
        r = await ac.get("/items")
        assert r.status_code == status.HTTP_200_OK
        start_len = len(r.json())

        # Neues Item
        r = await ac.post("/items", json={"text": "Testtodo"})
        assert r.status_code == status.HTTP_201_CREATED
        created = r.json()
        assert "id" in created and created["text"] == "Testtodo"

        # Liste +1
        r = await ac.get("/items")
        assert r.status_code == status.HTTP_200_OK
        assert len(r.json()) == start_len + 1
