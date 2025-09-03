from settings.schemas import PostCreate, PostResponse, PostOut
from fastapi import APIRouter, status, HTTPException, Response, Depends
from services import post_services as services
from services.server import get_db
from sqlalchemy.orm import Session
from typing import List, Optional
from tokens import oauth2
from settings import models

router = APIRouter(
                    prefix="/post",
                    tags=['Posts']
                    )

@router.get("/home", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome"}

@router.get("s/", status_code=status.HTTP_200_OK, response_model=List[PostOut])
def get_posts(limit: int = 10, skip:int = 0,
              search: Optional[str] = "",
              db: Session = Depends(get_db)):
            #   ,current_user: models.User = Depends(oauth2.get_current_user)):
    # print(current_user.email)
    data = services.get_posts(db, limit, skip, search)
    return data

@router.post("/", status_code= status.HTTP_201_CREATED, response_model = PostResponse)
def create_post(post:PostCreate, db:Session = Depends(get_db), current_user:models.User = Depends(oauth2.get_current_user)):
    try:
        return services.create_post(db, post, current_user.id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Something went wrong")

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= PostOut)
def get_post(id: int, db:Session = Depends(get_db)):
    post = services.find_post(db, id)
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    services.delete_post(db, id, current_user.id)
    print(current_user.email)
    return {Response(status_code = status.HTTP_204_NO_CONTENT)}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
def update_post(id: int, post:PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    services.update_post(id, post, db, current_user.id)
    print(current_user.email)
    return  services.find_post(db, id)
