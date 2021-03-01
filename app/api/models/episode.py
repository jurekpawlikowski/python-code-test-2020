from sqlalchemy import PrimaryKeyConstraint

from app.api.utlis.models import BaseModel
from app.factory import db


class Episode(BaseModel):
    """
    Class representing an episode of game of thrones
    """

    __tablename__ = "episodes"
    fields_to_serialize = [
        "season",
        "episode",
        "title",
        "year",
        "release_date",
        "runtime_in_minutes",
        "director",
        "writers",
        "actors",
        "plot",
        "imdb_rating",
        "imdb_votes",
        "imdb_id",
    ]

    season = db.Column(db.Integer, nullable=False)
    episode = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(128), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    runtime_in_minutes = db.Column(db.Integer, nullable=False)
    director = db.Column(db.String(128), nullable=False)
    writers = db.Column(db.String(512), nullable=False)
    actors = db.Column(db.ARRAY(db.String), nullable=False)
    plot = db.Column(db.Text, nullable=False)
    imdb_rating = db.Column(db.Numeric, nullable=False)
    imdb_votes = db.Column(db.BigInteger, nullable=False)
    imdb_id = db.Column(db.String(9), nullable=False, unique=True)

    __table_args__ = (
        PrimaryKeyConstraint("season", "episode"),
        {},
    )
