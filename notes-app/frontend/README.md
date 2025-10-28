# Frontend - Notes Application

Next.js frontend for the Notes Application.

## Structure

```
app/
├── page.tsx              # Login/Signup page
├── dashboard/
│   └── page.tsx          # Dashboard with notes table
├── layout.tsx            # Root layout
└── globals.css           # Global styles

lib/
└── api.ts                # API utility functions
```

## Quick Start

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

App runs on: http://localhost:3000

## Features

### Authentication Page
- Toggle between Login and Signup
- Form validation
- Error handling
- Redirect to dashboard on success

### Dashboard
- Display all notes in a table
- Create new notes with modal
- Edit existing notes
- Delete notes with confirmation
- Logout functionality
- Role-based UI (admin sees owner info)

## API Integration

All API calls are in `lib/api.ts`:
- `signup()` - Create account
- `login()` - Login
- `getMe()` - Get current user
- `getNotes()` - Fetch all notes
- `createNote()` - Create note
- `updateNote()` - Update note
- `deleteNote()` - Delete note

## Styling

Uses Tailwind CSS for styling:
- Responsive design
- Modern UI components
- Gradient backgrounds
- Clean table layout
- Modal overlays

## Environment Variables

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Build for Production

```bash
npm run build
npm start
```

## Deployment

Recommended: Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

Set environment variable in Vercel dashboard:
- `NEXT_PUBLIC_API_URL` = your production backend URL
