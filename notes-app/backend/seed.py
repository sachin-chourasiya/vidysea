"""
Seed script to create test users in the database
Run this after setting up the database to create test accounts
"""

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from auth import get_password_hash

def seed_database():
    # Create tables
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if users already exist
        existing_admin = db.query(models.User).filter(models.User.email == "admin@example.com").first()
        existing_user = db.query(models.User).filter(models.User.email == "user@example.com").first()
        
        if existing_admin:
            print("Admin user already exists!")
        else:
            # Create admin user
            admin = models.User(
                name="Admin User",
                email="admin@example.com",
                password=get_password_hash("admin123"),
                role="admin"
            )
            db.add(admin)
            print("✅ Admin user created: admin@example.com / admin123")
        
        if existing_user:
            print("Regular user already exists!")
        else:
            # Create regular user
            user = models.User(
                name="Regular User",
                email="user@example.com",
                password=get_password_hash("user123"),
                role="user"
            )
            db.add(user)
            print("✅ Regular user created: user@example.com / user123")
        
        db.commit()
        print("\n✅ Database seeded successfully!")
        print("\nTest Credentials:")
        print("-" * 50)
        print("Admin:")
        print("  Email: admin@example.com")
        print("  Password: admin123")
        print("\nUser:")
        print("  Email: user@example.com")
        print("  Password: user123")
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database...")
    seed_database()
