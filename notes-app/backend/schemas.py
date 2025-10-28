from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User Schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# Note Schemas
class NoteCreate(BaseModel):
    title: str
    description: str

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class NoteResponse(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    created_at: datetime
    updated_at: datetime
    owner: UserResponse
    
    class Config:
        from_attributes = True

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
