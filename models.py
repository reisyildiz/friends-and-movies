from sqlalchemy import Column, BigInteger, String, Boolean, Float, DateTime, func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(30), unique=True, index=True, nullable=False)
    email = Column(String(254), unique=True, index=True, nullable=False)
    hashed_password = Column(String(72), nullable=False)
    is_active = Column(Boolean, server_default="true", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r}>"


class Movie(Base):
    __tablename__ = "movies"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String(500), index=True, nullable=False)
    director = Column(String(200), nullable=True)
    year = Column(BigInteger, nullable=True)
    imdb_rating = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"<Movie id={self.id} title={self.title!r}>"
