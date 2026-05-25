from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL bağlantı URL'imiz
# Format: postgresql://kullanici_adi:sifre@localhost:port/veritabanı_adi
# Bizim şifremiz boş olduğu için iki nokta üst üste arasını boş bırakıyoruz.
DATABASE_URL = "postgresql://LENOVO:@localhost:5432/fam_db"

# Veritabanı motorunu çalıştırıyoruz
engine = create_engine(DATABASE_URL)

# Veritabanında işlem yapmamızı sağlayacak oturum fabrikası
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# İleride oluşturacağımız tabloların türeyeceği ana sınıf (Base)
Base = declarative_base()

# Backend isteklerinde veritabanı oturumunu güvenli açıp kapatacak fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()