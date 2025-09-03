from jose import JWTError, jwt
from settings import models, schemas
from settings.config import settings as set
from datetime import UTC, datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from services import server
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(tz=UTC) + timedelta(minutes=set.access_token_time)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, set.authorization_key, algorithm=set.algorithm)

    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, set.authorization_key, algorithms=[set.algorithm])
        id = payload.get("user_id")

        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id = id)

    except JWTError:
        raise credential_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(server.get_db)):
    credential_exception = HTTPException(
                                        status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail = "Could not validate credentials",
                                        headers={"WWW-Authenticate": "Bearer"}
                                        )

    token_data = verify_access_token(token, credential_exception)

    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    return user
