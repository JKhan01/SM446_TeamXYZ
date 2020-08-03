import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = "secret"
#MONGO_URL = os.environ["MONGO_URL"]
REDIS_URL = os.environ["REDIS_URL"]
PRODUCT_KEY_BITBUCKET = os.environ["PRODUCT_KEY_BITBUCKET"]
PRODUCT_SECRET_BITBUCKET = os.environ["PRODUCT_SECRET_BITBUCKET"]
#RASA_SERVER_URL = 'http://localhost:5005'
#S3_BUCKET = 'sih2020-meetings'
#FRONTEND_URL = 'http://localhost:8000/jarvis.html' ## front-end url here
SESSION_TIMEOUT = 2592000