from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
db = SQLAlchemy()


# Initializing flask extensions
    # bootstrap.init_app(app)