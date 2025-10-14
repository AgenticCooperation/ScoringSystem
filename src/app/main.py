from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from starlette.middleware.cors import CORSMiddleware

from src.app.models import Base, User, UserCreate, UserUpdate, UserResponse
import os

# Veritabanı bağlantısı
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/fastapi_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 

# Veritabanı tablosunu oluştur
Base.metadata.create_all(bind=engine)

# FastAPI uygulaması
app = FastAPI(title="FastAPI Users API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Veritabanı bağımlılığı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpointler
@app.get("/")
async def root():
    return {"message": "FastAPI Users API'ye hoş geldiniz!"}

@app.get("/users", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    """Tüm kullanıcıları getir"""
    users = db.query(User).all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """ID'ye göre kullanıcı getir"""
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    return user

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Yeni kullanıcı oluştur"""
    # Email kontrolü
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu email adresi zaten kullanılıyor")
    
    db_user = User(name=user.name, email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """Kullanıcı bilgilerini güncelle"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    
    # Sadece verilen alanları güncelle
    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        # Email kontrolü
        existing_user = db.query(User).filter(User.email == user.email, User.id != user_id).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Bu email adresi zaten kullanılıyor")
        db_user.email = user.email
    if user.age is not None:
        db_user.age = user.age
    
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Kullanıcıyı sil"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    
    db.delete(db_user)
    db.commit()
    return {"message": "Kullanıcı başarıyla silindi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

