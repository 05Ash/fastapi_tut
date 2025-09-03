from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from settings import models

def up_vote(vote, db: Session, user):
    # if post.user_id == user.id:
    #     raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                     models.Vote.user_id == user.id)
    found_vote = vote_query.first()
    post = db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist")
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail = f"User {user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = user.id)
        db.add(new_vote)
        db.commit()

    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message":"successfully deleted vote"}
