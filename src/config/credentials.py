import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ['bot_token']

MONGODB_DATABASE=os.environ['MONGODB_DATABASE']
MONGODB_USERNAME=os.environ['MONGODB_USERNAME']
MONGODB_PASSWORD=os.environ['MONGODB_PASSWORD']
MONGODB_HOSTNAME=os.environ['MONGODB_HOSTNAME']
MONGODB_PORT=os.environ['MONGODB_PORT']
