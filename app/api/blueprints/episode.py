from flask import Blueprint

from app.api.models import Episode, Comment
from app.api.utlis.http import json_response

episode_blueprint = Blueprint("episode", __name__)


@episode_blueprint.route("", methods=["GET"])
def list_episodes():
    """
    List all episodes of the system
    """
    return json_response(
        status=200,
        response_data={
            "data": {
                "episodes": [
                    episode.serialize(
                        [
                            "season",
                            "episode",
                            "title",
                            "imdb_rating",
                        ]
                    )
                    for episode in Episode.all()
                ]
            },
        },
    )


@episode_blueprint.route("<int:season_id>/<int:episode_id>", methods=["GET"])
def get_episode(season_id: int, episode_id: int):
    """
    Get details of an episode
    """
    episode = Episode.query.get((season_id, episode_id))
    return json_response(
        status=200,
        response_data={"data": {"episode": episode.serialize()}},
    )


@episode_blueprint.route("<int:season_id>/<int:episode_id>/comments", methods=["GET"])
def get_comments(season_id: int, episode_id: int):
    """
    Get comments for an episode
    """
    return json_response(
        status=200,
        response_data={
            "data": {
                "comments": [
                    comment.serialize()
                    for comment in Comment.query.filter_by(
                        season=season_id, episode=episode_id
                    )
                ]
            }
        },
    )
