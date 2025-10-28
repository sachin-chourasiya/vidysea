# Deployment Guide

## Quick Deployment Options

### Option 1: Render + Vercel (Recommended - Free)

#### Backend on Render

1. Push your code to GitHub
2. Go to [Render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: notes-api
   - **Root Directory**: backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add Environment Variables:
   - `DATABASE_URL`: (Use Render's PostgreSQL)
   - `SECRET_KEY`: (Generate a strong random key)
   - `ALGORITHM`: HS256
   - `ACCESS_TOKEN_EXPIRE_MINUTES`: 30
7. Create PostgreSQL database (New → PostgreSQL)
8. Copy Internal Database URL to `DATABASE_URL`
9. Deploy!

#### Frontend on Vercel

1. Go to [Vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: frontend
4. Add Environment Variable:
   - `NEXT_PUBLIC_API_URL`: Your Render backend URL
5. Deploy!

### Option 2: Railway (Easiest - Free tier)

1. Go to [Railway.app](https://railway.app)
2. Create New Project
3. Add PostgreSQL database
4. Add Python service for backend:
   - Set root directory: `backend`
   - Add environment variables from PostgreSQL
5. Add Node.js service for frontend:
   - Set root directory: `frontend`
   - Add `NEXT_PUBLIC_API_URL` environment variable
6. Deploy!

### Option 3: Heroku

#### Backend

```bash
cd backend
heroku create notes-api
heroku addons:create heroku-postgresql:mini
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALGORITHM=HS256
heroku config:set ACCESS_TOKEN_EXPIRE_MINUTES=30
git push heroku main
```

#### Frontend

```bash
cd frontend
heroku create notes-frontend
heroku config:set NEXT_PUBLIC_API_URL=https://notes-api.herokuapp.com
git push heroku main
```

## Environment Setup

### Backend Environment Variables

```bash
DATABASE_URL=postgresql://user:pass@host:5432/db
SECRET_KEY=generate-a-strong-random-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate SECRET_KEY:
```python
import secrets
print(secrets.token_urlsafe(32))
```

### Frontend Environment Variables

```bash
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

## CORS Configuration

Update `main.py` in backend for production:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Database Migration

For production, ensure database tables are created:

```python
# This runs automatically in main.py
models.Base.metadata.create_all(bind=engine)
```

## Testing Production

1. Visit your frontend URL
2. Create an admin account
3. Create a regular user account
4. Test all CRUD operations
5. Verify role-based access

## Monitoring

- Backend logs: Check your hosting platform's logs
- Frontend errors: Use Vercel Analytics
- Database: Monitor connection pool usage

## Backup Strategy

- Enable automated backups on your database hosting
- Export database regularly:
```bash
pg_dump $DATABASE_URL > backup.sql
```

## Security Checklist

- ✅ Strong SECRET_KEY in production
- ✅ HTTPS enabled
- ✅ CORS configured for specific origins
- ✅ Environment variables not in code
- ✅ Database password is strong
- ✅ JWT tokens expire appropriately

## Common Issues

### CORS Errors
- Add your frontend URL to allowed origins in backend

### Database Connection Failed
- Verify DATABASE_URL is correct
- Check if database is running
- Verify firewall rules

### 401 Unauthorized
- Check if JWT token is being sent
- Verify SECRET_KEY matches between deployments
- Check token expiration time

## Cost Estimate

**Free Tier Options:**
- Render: Free (with limitations)
- Vercel: Free (hobby projects)
- Railway: Free $5 credit/month
- Heroku: Free (limited)

**Paid Options (Recommended for production):**
- Render: $7/month (web service) + $7/month (PostgreSQL)
- Vercel: $20/month (Pro)
- Railway: Pay as you go ($0.000463/GB-hour)

## Support

For deployment issues:
1. Check hosting platform documentation
2. Review application logs
3. Test locally first
4. Create issue on GitHub repository
