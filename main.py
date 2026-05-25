import os
import models
from fastapi import FastAPI
from database import engine
from routers import auth

if os.getenv("ENVIRONMENT", "development") == "development":
    models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FAM (Friends and Movies) API",
    description="Backend API for the Friends and Movies social platform",
    version="0.1.0",
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])


@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "ok"}
