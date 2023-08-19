import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True


SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATION = True


SECRET_KEY = os.getenv('SECRET_KEY')
