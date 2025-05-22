# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables desde .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
