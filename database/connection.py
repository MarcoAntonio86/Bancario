import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent.parent
DATABASE_PATH = ROOT_PATH / "bank.db"


def create_connection():
    return sqlite3.connect(DATABASE_PATH)