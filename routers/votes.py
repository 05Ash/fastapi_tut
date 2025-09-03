from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from tokens import oauth2
from settings.schemas import PostCreate, Vote
from services.server import get_db
from settings.models import User
from services import vote_services as services


router = APIRouter(
    prefix = "/vote",
    tags = ["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: Vote, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return services.up_vote(vote, db, current_user)
