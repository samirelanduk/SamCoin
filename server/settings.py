import os
from .secrets import SECRET_KEY

VERSION = "0.1"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

DEBUG = True

ROOT_URLCONF = "server.urls"



INSTALLED_APPS = [
]

MIDDLEWARE = [
]
