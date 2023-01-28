from flask import Flask
from .models import Base, engine, session, User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mysecret"

    # create_database(app, engine)

    from .views import views
    app.register_blueprint(views)

    return app


def create_database(app, engine):
    with app.app_context():
        Base.metadata.create_all(engine)
        print("Created Database!")
