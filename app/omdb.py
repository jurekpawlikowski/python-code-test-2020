from datetime import datetime
from typing import Dict, List

import requests

from app.api.models import Episode

SEASON_URL = f""
EPISODE_URL = f""


class OMDBClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_episode_ids(self, season: int) -> List[str]:
        season_url = f"http://www.omdbapi.com/?t=Game%20of%20Thrones&Season={season}&apikey={self.api_key}"
        response = requests.get(season_url)
        response_data = response.json()
        return [episode["imdbID"] for episode in response_data["Episodes"]]

    def get_episode_data(self, episode_id: str) -> Dict:
        episode_url = (
            f"https://www.omdbapi.com/?i={episode_id}&apikey={self.api_key}&plot=full"
        )
        response = requests.get(episode_url)
        return response.json()

    def load_season_data(self, season):
        episode_ids = self.get_episode_ids(season)
        for episode_id in episode_ids:
            data = self.get_episode_data(episode_id)
            episode = Episode(
                season=season,
                episode=data["Episode"],
                title=data["Title"],
                year=data["Year"],
                release_date=datetime.strptime(data["Released"], "%d %b %Y"),
                runtime_in_minutes=int(data["Runtime"].strip(" min")),
                director=data["Director"],
                writers=data["Writer"].split(","),
                actors=data["Actors"].split(","),
                plot=data["Plot"],
                imdb_rating=data["imdbRating"],
                imdb_votes=data["imdbVotes"],
                imdb_id=data["imdbID"],
            )
            episode.save()

    def load_data(self):
        for season in range(1, 9):
            self.load_season_data(season)
