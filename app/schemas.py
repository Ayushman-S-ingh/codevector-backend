from datetime import datetime
from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    items: list[ProductResponse]
    next_cursor_updated_at: datetime | None = None
    next_cursor_id: int | None = None