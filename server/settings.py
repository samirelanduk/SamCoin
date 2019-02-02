import os
from .secrets import SECRET_KEY

VERSION = "0.1"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

DEBUG = True

ROOT_URLCONF = "server.urls"

DATABASES = {"default": {
 "ENGINE": "django.db.backends.sqlite3",
 "NAME": f"{BASE_DIR}/db.sqlite3"
}}

COIN_STORE = "store"

INSTALLED_APPS = [
]

MIDDLEWARE = [
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.abspath(f"{BASE_DIR}/../static")
