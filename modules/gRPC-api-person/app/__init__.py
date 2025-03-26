from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os
from typing import List, Type

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

# Datenbank-Engine erstellen
engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
db = SQLAlchemy()
db.session = scoped_session(sessionmaker(bind=engine))