from faker import Faker
import random
from datetime import timedelta

from app.database import SessionLocal
from app.models import Product

fake = Faker()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home",
    "Beauty",
    "Toys",
    "Furniture"
]

TOTAL_PRODUCTS = 200_000
BATCH_SIZE = 5000

db = SessionLocal()

for start in range(0, TOTAL_PRODUCTS, BATCH_SIZE):

    products = []

    for _ in range(BATCH_SIZE):

        created = fake.date_time_between(
            start_date="-365d",
            end_date="now"
        )

        updated = created + timedelta(
            days=random.randint(0, 30)
        )

        products.append(
            Product(
                name=fake.word().title() + " " + fake.word().title(),
                category=random.choice(categories),
                price=round(random.uniform(100, 5000), 2),
                created_at=created,
                updated_at=updated
            )
        )

    db.bulk_save_objects(products)
    db.commit()

    print(f"Inserted {start + BATCH_SIZE:,} / {TOTAL_PRODUCTS:,}")

db.close()

print("Done!")