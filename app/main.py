from datetime import datetime
from typing import Optional

import app.models
from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeVector Backend Assignment",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}


@app.get("/products", response_model=schemas.ProductListResponse)
def get_products(
    limit: int = Query(
        default=20,
        ge=1,
        le=100,
        description="Number of products per page (1-100)",
    ),
    category: Optional[str] = Query(
        default=None,
        description="Filter by category",
    ),
    cursor_updated_at: Optional[datetime] = Query(
        default=None,
        description="Cursor updated_at value",
    ),
    cursor_id: Optional[int] = Query(
        default=None,
        description="Cursor id value",
    ),
    db: Session = Depends(get_db),
):

    products = crud.get_products(
        db=db,
        limit=limit,
        category=category,
        cursor_updated_at=cursor_updated_at,
        cursor_id=cursor_id,
    )

    next_updated = None
    next_id = None

    if products:
        last = products[-1]
        next_updated = last.updated_at
        next_id = last.id

    return {
        "items": products,
        "next_cursor_updated_at": next_updated,
        "next_cursor_id": next_id,
    }