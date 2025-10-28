# Quick Start Guide 🚀

Get the Notes Application running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- Node.js 18+ installed
- PostgreSQL installed and running

## Step 1: Setup Database (2 minutes)

```bash
# Create database
createdb notesdb

# Or using psql
psql -U postgres
CREATE DATABASE notesdb;
\q
```

## Step 2: Setup Backend (2 minutes)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Update .env file with your database credentials
# DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/notesdb

# Seed database with test users
python seed.py

# Run backend
python main.py
```

Backend should now be running on http://localhost:8000

## Step 3: Setup Frontend (1 minute)

Open a new terminal:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

Frontend should now be running on http://localhost:3000

## Step 4: Test the Application

1. Open http://localhost:3000 in your browser
2. Login with test credentials:
   - **Admin**: admin@example.com / admin123
   - **User**: user@example.com / user123
3. Try creating, editing, and deleting notes!

## Test Credentials

### Admin User (Can manage all notes)
- Email: `admin@example.com`
- Password: `admin123`

### Regular User (Can only manage own notes)
- Email: `user@example.com`
- Password: `user123`

## Verify Installation

### Check Backend
```bash
curl http://localhost:8000
# Should return: {"message":"Notes API is running"}
```

### Check API Docs
Visit: http://localhost:8000/docs

## Troubleshooting

### Backend won't start
- Check if PostgreSQL is running: `pg_isready`
- Verify database exists: `psql -l | grep notesdb`
- Check DATABASE_URL in .env file

### Frontend won't start
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Check if port 3000 is available

### Can't login
- Run seed script: `python seed.py`
- Check backend logs for errors
- Verify backend is running on port 8000

## Next Steps

1. Create your own user account
2. Start creating notes
3. Test admin vs user permissions
4. Explore the API at http://localhost:8000/docs
5. Customize the application
6. Deploy to production (see DEPLOYMENT.md)

## Project Structure

```
notes-app/
├── backend/           # FastAPI backend
│   ├── main.py       # Main application
│   ├── models.py     # Database models
│   └── ...
└── frontend/         # Next.js frontend
    ├── app/          # App router pages
    └── lib/          # Utilities
```

## Common Commands

### Backend
```bash
# Start server
python main.py

# Seed database
python seed.py

# Install new package
pip install package-name
pip freeze > requirements.txt
```

### Frontend
```bash
# Development
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## API Endpoints

- `POST /auth/signup` - Register new user
- `POST /auth/login` - Login
- `GET /notes` - Get all notes
- `POST /notes` - Create note
- `PUT /notes/{id}` - Update note
- `DELETE /notes/{id}` - Delete note

## Need Help?

- Check README.md for detailed documentation
- See DEPLOYMENT.md for deployment instructions
- Review code comments for implementation details

Happy coding! 🎉
