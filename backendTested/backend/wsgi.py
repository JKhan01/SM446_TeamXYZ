import redis
# from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, origins=['127.0.0.1:8000'])
CORS(app)
app.config.from_pyfile('config.py')
# db = MongoClient(app.config['MONGO_URL'])
# task_queue = redis.Redis.from_url(url=app.config['REDIS_URL'], db = 0)
token_storage = redis.Redis.from_url(url=app.config['REDIS_URL'], db = 0)
# s3 = boto3.client('s3')

import routes

# if __name__=='__main__':
#     app.run(debug=True)