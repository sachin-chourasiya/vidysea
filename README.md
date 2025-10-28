# Notes Application

A simple full-stack notes app with user authentication and role-based access control.

## Features

- User signup and login
- Create, read, update, and delete notes
- Admin can manage all notes
- Regular users can only manage their own notes

## Tech Stack

**Frontend:** Next.js, TypeScript, Tailwind CSS  
**Backend:** FastAPI, Python  
**Database:** PostgreSQL

## Setup

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
createdb notesdb
python seed.py
python main.py
```

Backend runs on: http://localhost:8000

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: http://localhost:3000

## Test Credentials

**Admin:**
- Email: admin@example.com
- Password: admin123

**User:**
- Email: user@example.com
- Password: user123

## Project Structure

```
notes-app/
├── backend/          # FastAPI backend
└── frontend/         # Next.js frontend
```

## Environment Variables

**Backend (.env):**
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/notesdb
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Frontend (.env.local):**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## License

MIT
