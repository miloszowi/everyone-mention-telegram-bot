import os
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ['BOT_TOKEN']
WEBHOOK_URL = os.environ['WEBHOOK_URL']
PORT = os.environ['PORT']

MONGO_DATABASE = os.environ['MONGODB_DATABASE']
MONGO_CONNECTION_STRING = "mongodb://%s:%s@%s:%s/%s?authSource=admin" % (
    os.environ['MONGODB_USERNAME'], quote_plus(os.environ['MONGODB_PASSWORD']),
    os.environ['MONGODB_HOSTNAME'], os.environ['MONGODB_PORT'], MONGO_DATABASE
)

BANNED_USERS = os.environ['BANNED_USERS'].split(',') or []
