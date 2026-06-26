from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Index,
)

from sqlalchemy.sql import func

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    category = Column(String, index=True)

    price = Column(Float)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    __table_args__ = (
        Index(
            "idx_updated_id",
            "updated_at",
            "id",
        ),
    )