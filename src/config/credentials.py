import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ['bot_token']

firebaseConfig = {
    "apiKey": os.environ['firebase_apiKey'],
    "authDomain": os.environ['firebase_authDomain'],
    "databaseURL": os.environ['firebase_databaseURL'],
    "projectId": os.environ['firebase_projectId'],
    "storageBucket": os.environ['firebase_storageBucket'],
}
