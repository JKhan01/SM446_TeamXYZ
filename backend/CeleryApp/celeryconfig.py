from dotenv import load_dotenv
from os import environ
load_dotenv()
broker_url = environ.get('REDIS_URL')