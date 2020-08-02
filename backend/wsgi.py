import redis, boto3
from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MongoClient(app.config['MONGO_URL'])
task_queue = redis.Redis.from_url(url=app.config['REDIS_URL'], db = 0)
token_storage = redis.Redis.from_url(url=app.config['REDIS_URL'], db = 1)
s3 = boto3.client('s3')

import routes