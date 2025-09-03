from pydoc import text
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from services.server import engine

Base = declarative_base()



class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    published = Column(Boolean, nullable = False, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone = True),
                        nullable = False,
                        server_default = text('Now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
    user = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, nullable = False, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),
                        nullable = False,
                        server_default = text('NOW()'))
    phone_number = Column(String)

class Vote(Base):
    __tablename__ = "votes"

    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),primary_key=True)
    post = relationship("Post")
    user = relationship("User")

#models.Base.metadata.create_all(bind = engine)
