from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db

# Bu satır, models.py içinde yazdığımız tüm sınıfları okur 
# ve PostgreSQL'de eğer o tablolar yoksa OTOMATİK OLARAK yaratır!
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FAM (Friends and Movies) API")

@app.get("/")
def read_root():
    return {"status": "success", "message": "FAM backend and database connection is online!"}

# Test amaçlı: Veritabanındaki kullanıcı sayısını dönen geçici bir endpoint
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    user_count = db.query(models.User).count()
    return {"message": "Database connection works perfectly!", "total_users": user_count}