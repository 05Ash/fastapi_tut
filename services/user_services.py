from fastapi import status, HTTPException
from settings import models
from utilities import utils
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_user(user, db:Session):
    #hash the password
    user.password = utils.hash(user.password)
    try:
        user = models.User(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists."
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )

def find_user(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    return user
