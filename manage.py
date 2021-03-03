import os

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from app.api.models import Episode
from app.factory import create_app, db

app = create_app()


def main():
    directory = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "migrations")
    )

    Migrate(app, db, directory=directory)
    manager = Manager(app=app)
    manager.add_command("db", MigrateCommand)

    @manager.command
    def load_data():
        from app.omdb import OMDBClient

        if Episode.query.count() == 73:
            return

        client = OMDBClient(app.config["OMDB_API_KEY"])
        client.load_data()

    manager.run()


if __name__ == "__main__":
    main()
