# Backend - Notes API

FastAPI backend for the Notes Application.

## Structure

- `main.py` - Main application file with all API routes
- `models.py` - SQLAlchemy database models (User, Note)
- `schemas.py` - Pydantic schemas for request/response validation
- `database.py` - Database connection and session management
- `auth.py` - Authentication utilities (JWT, password hashing)
- `.env` - Environment variables
- `requirements.txt` - Python dependencies

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Create database
createdb notesdb

# Run server
python main.py
```

Server runs on: http://localhost:8000

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Schema

### Users Table
- `id` - Primary key
- `name` - User's full name
- `email` - Unique email (used for login)
- `password` - Hashed password
- `role` - Either "admin" or "user"
- `created_at` - Timestamp

### Notes Table
- `id` - Primary key
- `title` - Note title
- `description` - Note content
- `user_id` - Foreign key to Users
- `created_at` - Timestamp
- `updated_at` - Timestamp

## Environment Variables

```
DATABASE_URL=postgresql://user:password@localhost:5432/notesdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Testing with cURL

### Sign Up
```bash
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "test123",
    "role": "user"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'
```

### Create Note (with token)
```bash
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "title": "My First Note",
    "description": "This is a test note"
  }'
```
