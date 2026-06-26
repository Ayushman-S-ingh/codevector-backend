# 🚀 CodeVector Backend Assignment

A scalable backend service built using **FastAPI** and **PostgreSQL** that allows users to browse over **200,000 products** using efficient **cursor-based pagination** while maintaining consistent results even when new products are inserted or updated.

---

## 🌐 Live Demo

**API Base URL**

https://codevector-backend-v6e4.onrender.com

**Swagger Documentation**

https://codevector-backend-v6e4.onrender.com/docs

---

# GitHub Repository

https://github.com/Ayushman-S-ingh/codevector-backend

---

# Assignment Requirements

This project satisfies the following requirements:

- ✅ Browse approximately 200,000 products
- ✅ Return newest products first
- ✅ Filter by category
- ✅ Fast pagination
- ✅ Cursor-based pagination
- ✅ Consistent browsing while data changes
- ✅ Seed script included
- ✅ Hosted backend
- ✅ Hosted PostgreSQL database

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend REST API |
| PostgreSQL (Neon) | Cloud Database |
| SQLAlchemy | ORM |
| Faker | Generate realistic product data |
| Uvicorn | ASGI Server |
| Render | Backend Hosting |
| GitHub | Source Code |

---

# Project Structure

```
codevector-backend/

│
├── app/
│   ├── main.py          # API routes
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database queries
│   ├── seed.py          # Generates 200,000 products
│   └── __init__.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Database Schema

## Product

| Field | Type |
|--------|------|
| id | Integer (Primary Key) |
| name | String |
| category | String |
| price | Float |
| created_at | Timestamp |
| updated_at | Timestamp |

---

# API Endpoint

## Get Products

```
GET /products
```

### Query Parameters

| Parameter | Description |
|------------|-------------|
| limit | Number of products (1-100) |
| category | Optional category filter |
| cursor_updated_at | Cursor timestamp |
| cursor_id | Cursor product id |

Example

```
GET /products?limit=20
```

Next Page

```
GET /products?limit=20&cursor_updated_at=2026-07-25T17:57:08.351928Z&cursor_id=25460
```

---

# Cursor Pagination

Instead of OFFSET/LIMIT pagination, this project uses **cursor-based pagination**.

Products are sorted using:

```
ORDER BY updated_at DESC, id DESC
```

The last product returned becomes the cursor for the next request.

Example response:

```json
{
  "next_cursor_updated_at": "...",
  "next_cursor_id": 25460
}
```

These values are passed into the next request.

---

# Why Cursor Pagination?

Offset pagination becomes slower as the table grows because the database has to skip rows before returning results.

Cursor pagination directly continues from the last record, making it:

- Faster
- More scalable
- Stable while new rows are inserted
- Prevents duplicate records
- Prevents missing records

This makes it suitable for large datasets.

---

# Database Indexes

To improve query performance, a composite index is created on:

```
(updated_at DESC, id DESC)
```

This matches the ordering used during pagination and allows PostgreSQL to efficiently retrieve the next page.

---

# Seed Script

The project includes a seed script that generates **200,000 products**.

Run:

```bash
python -m app.seed
```

The script generates:

- Random product names
- Random categories
- Random prices
- created_at timestamps
- updated_at timestamps

Products are inserted in batches for better performance.

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/Ayushman-S-ingh/codevector-backend.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```
DATABASE_URL=YOUR_DATABASE_URL
```

Start server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Deployment

Backend

- Render

Database

- Neon PostgreSQL

---

# Design Decisions

### Why FastAPI?

- Fast
- Lightweight
- Automatic Swagger documentation
- Type validation using Pydantic
- Excellent async support

---

### Why PostgreSQL?

- Reliable relational database
- Excellent indexing
- Handles large datasets efficiently
- Strong SQL support

---

### Why SQLAlchemy?

- Clean ORM
- Easy model management
- Database abstraction
- Readable query construction

---

# Performance Considerations

Implemented:

- Cursor Pagination
- Composite Index
- Batch Inserts
- Query Filtering
- Limited Response Size

These choices allow the API to remain responsive even with large datasets.

---

# Future Improvements

If given more time, I would add:

- API authentication
- Unit and integration tests
- Docker support
- Alembic migrations
- Redis caching
- Rate limiting
- Logging and monitoring
- CI/CD pipeline using GitHub Actions

---

# AI Usage

AI tools (ChatGPT) were used as a development assistant to:

- Discuss architecture choices
- Review implementation ideas
- Explain concepts
- Help debug errors
- Improve documentation

All code was reviewed, tested, understood, and modified manually before submission.

---

# Author

**Ayushman Singh**

B.Tech Computer Science (Data Science)

Backend Developer | Python | FastAPI | SQL