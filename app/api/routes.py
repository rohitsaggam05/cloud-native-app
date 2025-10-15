from fastapi import APIRouter, HTTPException, Path, Query
from typing import List, Dict, Any
from .models import Item

router = APIRouter(prefix="/items", tags=["items"])

# In-memory database
items_db: Dict[int, Item] = {}

@router.post("/", response_model=Item, status_code=201)
async def create_item(item: Item):
    item_id = len(items_db) + 1
    items_db[item_id] = item
    return item

@router.get("/", response_model=List[Dict[str, Any]])
async def read_items(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    return [{"id": k, **v.dict()} for k, v in list(items_db.items())[skip:skip+limit]]

@router.get("/{item_id}", response_model=Dict[str, Any])
async def read_item(item_id: int = Path(..., ge=1)):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id].dict()}

@router.put("/{item_id}", response_model=Dict[str, Any])
async def update_item(item: Item, item_id: int = Path(..., ge=1)):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}

@router.delete("/{item_id}", response_model=Dict[str, str])
async def delete_item(item_id: int = Path(..., ge=1)):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}
