import os


SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://silvianjoki:password@localhost/pitches'