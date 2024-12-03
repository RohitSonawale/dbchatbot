import os
import pathlib
from pathlib import Path
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()


@lru_cache()
class Settings:
#    BASE_DIR = Path(_file_).resolve().parent
    mongourl: str = os.getenv("MONGODB_URI")
    DATABASE_CONNECT_DICT: dict = {}


setting = Settings()