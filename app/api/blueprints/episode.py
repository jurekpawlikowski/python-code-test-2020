from flask import Blueprint

from app.api.models import Episode
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


@episode_blueprint.route("<int:season>/<int:episode>", methods=["GET"])
def get_episode(season: int, episode: int):
    """
    Get details of an episode
    """
    episode = Episode.query.get((season, episode))
    return json_response(
        status=200,
        response_data={"data": {"episode": episode.serialize()}},
    )
