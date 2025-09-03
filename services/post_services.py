from fastapi import status, HTTPException
from settings import models
from services.server import engine
from sqlalchemy.orm import Session
from sqlalchemy import func
from settings.schemas import PostResponse

# #Finds a post based on id
def get_posts(db: Session, limit, skip, search_parameter):
    # posts = db.query(models.Post).filter(models.Post.title.contains(search_parameter)).limit(limit).offset(skip).all()
    results = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search_parameter))
        .offset(skip).limit(limit)
        .all()
    )
    return results


def find_post(db: Session, post_id):
    post = (db.query(
        models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id==models.Post.id, isouter=True)
        .filter(models.Post.id == post_id)
        .group_by(models.Post.id)
        .first())
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {post_id} not found.")
    return post

def create_post(db: Session, post, id):
    try:
        new_post = models.Post(user_id = id, **post.model_dump())
        db.add(new_post)
        db.commit()
        # No returning possible with alchemy, so use refresh to put the value back to new_post
        db.refresh(new_post)
        return new_post
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

def delete_post(db:Session, id, user_id):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")
    is_owner(post, user_id)
    post_query.delete(synchronize_session = False)
    db.commit()

def update_post(id, post, db: Session, user_id):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_to_update = post_query.first()
    if post_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")
    is_owner(post_to_update, user_id)

    post_query.update(post.model_dump(), synchronize_session = False)
    db.commit()

def is_owner(query, user_id):
    if query.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authrorized to perform requested action")
