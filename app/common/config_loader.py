import os, sys
from pathlib import Path
from dotenv import load_dotenv


if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

SUPA_DB_HOST=os.getenv("SUPA_DB_HOST")
SUPA_DB_PORT=int(os.getenv("SUPA_DB_PORT"))
SUPA_DB_USER=os.getenv("SUPA_DB_USER")
SUPA_DB_PASSWD=os.getenv("SUPA_DB_PASSWD")
SUPA_DB_DBNAME=os.getenv("SUPA_DB_DBNAME")

AUTH_DB_HOST=os.getenv("AUTH_DB_HOST")
AUTH_DB_PORT=int(os.getenv("AUTH_DB_PORT"))
AUTH_DB_USER=os.getenv("AUTH_DB_USER")
AUTH_DB_PASSWD=os.getenv("AUTH_DB_PASSWD")
AUTH_DB_DBNAME=os.getenv("AUTH_DB_DBNAME")