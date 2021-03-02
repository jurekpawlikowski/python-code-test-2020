from sqlalchemy import ForeignKeyConstraint

from .episode import Episode
from app.api.utlis.models import BaseModel
from app.factory import db


class Comment(BaseModel):
    """
    Class representing a comment for an episode
    """

    __tablename__ = "comments"
    fields_to_serialize = [
        "id",
        "season",
        "episode",
        "content",
        "author_name",
        "created_at",
        "updated_at",
    ]

    id = db.Column(db.BigInteger, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    episode = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.String(128), nullable=False, unique=True)

    __table_args__ = (
        ForeignKeyConstraint((season, episode), (Episode.season, Episode.episode)),
        {},
    )
