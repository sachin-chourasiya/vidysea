# Notes Application

A full-stack notes application with user authentication and role-based access control.

## Features

- **User Authentication**
  - Sign up with name, email, password, and role (admin/user)
  - Secure login with JWT tokens
  - Protected dashboard access

- **Notes Management**
  - Create, read, update, and delete notes
  - View notes in a clean table format
  - Modal-based note creation and editing

- **Role-Based Access Control**
  - **Admin**: Can manage ALL notes from all users
  - **User**: Can only manage their own notes

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **JWT** - Token-based authentication
- **Bcrypt** - Password hashing

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client

## Project Structure

```
notes-app/
├── backend/
│   ├── main.py              # FastAPI app and routes
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database configuration
│   ├── auth.py              # Authentication utilities
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
│
└── frontend/
    ├── app/
    │   ├── page.tsx         # Login/Signup page
    │   ├── dashboard/
    │   │   └── page.tsx     # Dashboard page
    │   ├── layout.tsx       # Root layout
    │   └── globals.css      # Global styles
    ├── lib/
    │   └── api.ts           # API utility functions
    ├── package.json         # Node dependencies
    ├── next.config.js       # Next.js config
    ├── tsconfig.json        # TypeScript config
    ├── tailwind.config.js   # Tailwind config
    └── .env.local           # Environment variables
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 18+
- PostgreSQL 12+

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create PostgreSQL database:
```bash
createdb notesdb
```

5. Update `.env` file with your database credentials:
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/notesdb
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

6. Run the application:
```bash
python main.py
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Update `.env.local` if needed:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run the development server:
```bash
npm run dev
```

Frontend will run on `http://localhost:3000`

## Test Credentials

### Admin User
- **Email**: admin@example.com
- **Password**: admin123
- **Role**: admin

### Regular User
- **Email**: user@example.com
- **Password**: user123
- **Role**: user

**Note**: These users need to be created through the signup page first.

## API Endpoints

### Authentication
- `POST /auth/signup` - Create new user account
- `POST /auth/login` - Login and get JWT token
- `GET /auth/me` - Get current user info

### Notes
- `GET /notes` - Get all notes (filtered by role)
- `POST /notes` - Create new note
- `GET /notes/{id}` - Get specific note
- `PUT /notes/{id}` - Update note
- `DELETE /notes/{id}` - Delete note

## Deployment

### Backend Deployment Options
- Render
- Railway
- Heroku
- AWS EC2

### Frontend Deployment Options
- Vercel (Recommended)
- Netlify
- AWS Amplify

### Environment Variables for Production

**Backend:**
- Update `SECRET_KEY` with a strong random key
- Set `DATABASE_URL` to production PostgreSQL URL
- Configure CORS for production frontend URL

**Frontend:**
- Set `NEXT_PUBLIC_API_URL` to production backend URL

## Development Notes

- The application uses JWT tokens stored in localStorage
- Role-based access is enforced on both frontend and backend
- Admin users see an additional "Owner" column in the notes table
- All passwords are hashed using bcrypt
- CORS is configured to allow all origins in development

## Future Enhancements

- Email verification
- Password reset functionality
- Note categories/tags
- Search and filter notes
- Rich text editor
- File attachments
- Sharing notes with other users

## License

MIT

## Contact

For any questions or issues, please create an issue in the GitHub repository.
