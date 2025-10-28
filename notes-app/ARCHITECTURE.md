# Notes Application Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                      FRONTEND                                │ │
│  │                    (Next.js 14)                              │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │ │
│  │  │              │  │              │  │              │      │ │
│  │  │ Login/Signup │  │  Dashboard   │  │ Note Modal   │      │ │
│  │  │   Page       │→ │    Page      │→ │ (Create/Edit)│      │ │
│  │  │              │  │              │  │              │      │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘      │ │
│  │          ↓                ↓                   ↓             │ │
│  │  ┌────────────────────────────────────────────────────────┐ │ │
│  │  │             API Client (lib/api.ts)                     │ │ │
│  │  │  - JWT Token Storage (localStorage)                    │ │ │
│  │  │  - Axios HTTP Client                                   │ │ │
│  │  │  - Automatic token injection                           │ │ │
│  │  └────────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                │ HTTP/HTTPS
                                │ REST API
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND SERVER                           │
│                        (FastAPI + Python)                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    API ROUTES (main.py)                     │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │ │
│  │  │     Auth     │  │    Notes     │  │  Middleware  │     │ │
│  │  │   Endpoints  │  │  Endpoints   │  │    (CORS)    │     │ │
│  │  │              │  │              │  │              │     │ │
│  │  │ POST /signup │  │ GET /notes   │  │ JWT Verify   │     │ │
│  │  │ POST /login  │  │ POST /notes  │  │ Auth Check   │     │ │
│  │  │ GET /me      │  │ PUT /notes/  │  │ RBAC Logic   │     │ │
│  │  │              │  │ DELETE /notes│  │              │     │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘     │ │
│  └────────────────────────────────────────────────────────────┘ │
│           ↓                      ↓                               │
│  ┌────────────────┐    ┌────────────────────────────────────┐  │
│  │  Auth Utils    │    │     Database Layer                  │  │
│  │  (auth.py)     │    │    (database.py + models.py)        │  │
│  │                │    │                                      │  │
│  │ • Hash Password│    │  ┌──────────────────────────────┐   │  │
│  │ • Verify Pass  │    │  │    SQLAlchemy ORM            │   │  │
│  │ • Create JWT   │    │  │                              │   │  │
│  │ • Verify JWT   │    │  │  • User Model                │   │  │
│  │                │    │  │  • Note Model                │   │  │
│  └────────────────┘    │  │  • Relationships             │   │  │
│                        │  └──────────────────────────────┘   │  │
│                        └────────────────────────────────────┘  │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                │ SQL Queries
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE (PostgreSQL)                         │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                      Tables                                 │ │
│  │                                                             │ │
│  │  ┌────────────────────┐        ┌────────────────────┐     │ │
│  │  │      USERS         │        │       NOTES        │     │ │
│  │  ├────────────────────┤        ├────────────────────┤     │ │
│  │  │ id (PK)            │◄───┐   │ id (PK)            │     │ │
│  │  │ name               │    │   │ title              │     │ │
│  │  │ email (unique)     │    │   │ description        │     │ │
│  │  │ password (hashed)  │    └───│ user_id (FK)       │     │ │
│  │  │ role (admin/user)  │        │ created_at         │     │ │
│  │  │ created_at         │        │ updated_at         │     │ │
│  │  └────────────────────┘        └────────────────────┘     │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagrams

### 1. User Authentication Flow

```
User Sign Up:
┌─────────┐   1. POST /auth/signup    ┌─────────┐   2. Hash Password   ┌──────────┐
│         │  ────────────────────────> │         │ ───────────────────> │          │
│ Browser │   {name, email, password}  │ Backend │   {bcrypt}           │ Database │
│         │ <──────────────────────── │         │ <─────────────────── │          │
└─────────┘   3. User Created          └─────────┘   4. Store User      └──────────┘
              {id, name, email, role}

User Login:
┌─────────┐   1. POST /auth/login     ┌─────────┐   2. Verify Password ┌──────────┐
│         │  ────────────────────────> │         │ ───────────────────> │          │
│ Browser │   {email, password}        │ Backend │   Check DB           │ Database │
│         │ <──────────────────────── │         │ <─────────────────── │          │
└─────────┘   4. JWT Token            └─────────┘   3. User Found       └──────────┘
              {token, user}                          {password matches}
              
              5. Store token in localStorage
```

### 2. Create Note Flow (User)

```
┌─────────┐   1. POST /notes          ┌─────────┐   2. Verify JWT      ┌──────────┐
│         │  ────────────────────────> │         │ ───────────────────> │          │
│ Browser │   Header: Bearer TOKEN     │ Backend │   Decode token       │ Database │
│         │   {title, description}     │         │                      │          │
│         │                            │         │   3. Get user_id     │          │
│         │                            │         │   4. Create note     │          │
│         │                            │         │ ───────────────────> │          │
│         │ <──────────────────────── │         │ <─────────────────── │          │
└─────────┘   6. Note Created         └─────────┘   5. Save to DB      └──────────┘
              {id, title, description,              {insert with user_id}
               user_id, created_at}
```

### 3. Get Notes Flow (Role-Based)

```
Regular User:
┌─────────┐   1. GET /notes           ┌─────────┐   2. Verify JWT      ┌──────────┐
│         │  ────────────────────────> │         │ ───────────────────> │          │
│ Browser │   Header: Bearer TOKEN     │ Backend │   Get user_id        │ Database │
│         │                            │         │   role = "user"      │          │
│         │                            │         │                      │          │
│         │                            │         │   3. Query:          │          │
│         │                            │         │   WHERE user_id=X    │          │
│         │                            │         │ ───────────────────> │          │
│         │ <──────────────────────── │         │ <─────────────────── │          │
└─────────┘   5. User's Notes Only    └─────────┘   4. Filter by user  └──────────┘
              [{note1}, {note2}...]

Admin User:
┌─────────┐   1. GET /notes           ┌─────────┐   2. Verify JWT      ┌──────────┐
│         │  ────────────────────────> │         │ ───────────────────> │          │
│ Browser │   Header: Bearer TOKEN     │ Backend │   Get user_id        │ Database │
│         │                            │         │   role = "admin"     │          │
│         │                            │         │                      │          │
│         │                            │         │   3. Query:          │          │
│         │                            │         │   SELECT ALL notes   │          │
│         │                            │         │ ───────────────────> │          │
│         │ <──────────────────────── │         │ <─────────────────── │          │
└─────────┘   5. ALL Users' Notes     └─────────┘   4. Return all      └──────────┘
              [{note1}, {note2}...     with owner info
               {note3(other user)}]
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       Security Layers                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 1: Password Security                                      │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ • Bcrypt hashing (cost factor 12)                          │ │
│  │ • Salted passwords                                         │ │
│  │ • Never store plain text                                   │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  Layer 2: JWT Authentication                                     │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ • HS256 algorithm                                          │ │
│  │ • 30-minute expiration                                     │ │
│  │ • Includes user email in payload                           │ │
│  │ • Verified on every request                                │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  Layer 3: Authorization (RBAC)                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ Admin Role:                    User Role:                  │ │
│  │ • Access ALL notes             • Access own notes only     │ │
│  │ • Edit ANY note                • Edit own notes only       │ │
│  │ • Delete ANY note              • Delete own notes only     │ │
│  │ • See all users' data          • See own data only         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  Layer 4: CORS Protection                                        │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ • Allowed origins configuration                            │ │
│  │ • Credentials handling                                     │ │
│  │ • HTTP methods restriction                                 │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  Layer 5: Input Validation                                       │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ • Pydantic schemas                                         │ │
│  │ • Email validation                                         │ │
│  │ • Required field checks                                    │ │
│  │ • Type checking                                            │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Tech Stack Details

```
Frontend Layer:
┌──────────────────────────────────────────────────┐
│ Next.js 14 (App Router)                          │
│ ├── React 18                                     │
│ ├── TypeScript (type safety)                     │
│ ├── Tailwind CSS (styling)                       │
│ └── Axios (HTTP client)                          │
└──────────────────────────────────────────────────┘

Backend Layer:
┌──────────────────────────────────────────────────┐
│ FastAPI (Python 3.8+)                            │
│ ├── Pydantic (validation)                        │
│ ├── SQLAlchemy (ORM)                             │
│ ├── python-jose (JWT)                            │
│ ├── passlib (password hashing)                   │
│ └── Uvicorn (ASGI server)                        │
└──────────────────────────────────────────────────┘

Database Layer:
┌──────────────────────────────────────────────────┐
│ PostgreSQL 12+                                    │
│ ├── Relational database                          │
│ ├── ACID compliance                              │
│ ├── Foreign key relationships                    │
│ └── Automatic timestamps                         │
└──────────────────────────────────────────────────┘
```

## Deployment Architecture (Production)

```
┌─────────────────────────────────────────────────────────────────┐
│                            Internet                              │
└────────────────────────┬────────────────────────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ↓                             ↓
┌──────────────────────┐      ┌──────────────────────┐
│   Vercel (Frontend)  │      │   Render (Backend)   │
│   ┌────────────────┐ │      │   ┌────────────────┐ │
│   │   Next.js App  │ │      │   │  FastAPI App   │ │
│   │   - Static Gen │ │      │   │  - Uvicorn     │ │
│   │   - SSR        │ │      │   │  - Workers     │ │
│   └────────────────┘ │      │   └────────────────┘ │
│                      │      │           │          │
│   Environment Vars:  │      │           ↓          │
│   NEXT_PUBLIC_API_   │      │   ┌────────────────┐ │
│   URL=render-url     │      │   │  PostgreSQL DB │ │
└──────────────────────┘      │   │  - Managed     │ │
                              │   │  - Backups     │ │
                              │   │  - SSL         │ │
                              │   └────────────────┘ │
                              │                      │
                              │   Environment Vars:  │
                              │   DATABASE_URL       │
                              │   SECRET_KEY         │
                              └──────────────────────┘

CDN Edge Network              Load Balancing
(Vercel Global)               (Render Auto-scaling)
```

## File Organization

```
Backend Structure:
backend/
├── main.py         ← All API routes (200 lines)
├── models.py       ← Database models (30 lines)
├── schemas.py      ← Pydantic schemas (50 lines)
├── database.py     ← DB connection (20 lines)
├── auth.py         ← JWT utilities (60 lines)
└── seed.py         ← Test data (60 lines)

Frontend Structure:
frontend/
├── app/
│   ├── page.tsx              ← Auth page (150 lines)
│   ├── dashboard/page.tsx    ← Dashboard (300 lines)
│   ├── layout.tsx            ← Root layout
│   └── globals.css           ← Styles
└── lib/
    └── api.ts                ← API client (60 lines)

Total Code: ~920 lines
Simple, clean, maintainable!
```

This architecture ensures:
✓ Security at multiple layers
✓ Scalability through stateless design
✓ Maintainability with clean separation
✓ Performance with efficient queries
✓ Reliability with proper error handling
