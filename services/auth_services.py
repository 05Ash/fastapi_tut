from services.server import engine
from sqlalchemy.orm import Session
from settings import models
from utilities import utils
from fastapi import status, HTTPException
from tokens import oauth2

def user_login(user_credentials, db: Session):
    print(user_credentials)
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail = "Invalid Credentials")
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail = "Invalid Credentials")

    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access_token" : access_token, "token_type": "bearer"}
