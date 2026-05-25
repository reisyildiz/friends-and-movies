from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import models
import schemas
import security
from database import get_db

router = APIRouter()


@router.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=security.hash_password(user_data.password),
    )
    db.add(new_user)
    try:
        db.flush()
    except IntegrityError as exc:
        db.rollback()
        constraint = str(exc.orig)
        if "users_email_key" in constraint:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )
        if "users_username_key" in constraint:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already taken",
            )
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with these credentials already exists",
        )

    db.refresh(new_user)
    return new_user
