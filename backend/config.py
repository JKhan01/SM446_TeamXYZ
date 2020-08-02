import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ["SECRET_KEY"]
MONGO_URL = os.environ["MONGO_URL"]
REDIS_URL = os.environ["REDIS_URL"]
PRODUCT_KEY_BITBUCKET = os.environ["PRODUCT_KEY_BITBUCKET"]
PRODUCT_SECRET_BITBUCKET = os.environ["PRODUCT_SECRET_BITBUCKET"]
RASA_ACTION_SERVER_URL = 'http://'
S3_BUCKET = 'sih2020-meetings'
FRONTEND_URL = '' ## front-end url here
SESSION_TIMEOUT = 2592000