import redis
from celery import Celery
from . import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)
token_store = redis.Redis.from_url(url=celeryconfig.broker_url, db = 1)