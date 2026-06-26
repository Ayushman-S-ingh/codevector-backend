from sqlalchemy.orm import Session
from sqlalchemy import desc, or_, and_

from app.models import Product


def get_products(
    db: Session,
    limit: int = 20,
    category: str | None = None,
    cursor_updated_at=None,
    cursor_id=None,
):

    query = db.query(Product)

    if category:
        query = query.filter(Product.category == category)

    if cursor_updated_at and cursor_id:
        query = query.filter(
            or_(
                Product.updated_at < cursor_updated_at,
                and_(
                    Product.updated_at == cursor_updated_at,
                    Product.id < cursor_id,
                ),
            )
        )

    products = (
        query.order_by(
            desc(Product.updated_at),
            desc(Product.id),
        )
        .limit(limit)
        .all()
    )

    return products