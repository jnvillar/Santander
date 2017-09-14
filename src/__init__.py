from flask import Flask
from src.jobs import celery

app = Flask('santander')
app.config['SECRET_KEY'] = 'random'
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

app.debug = True
celery = celery.make_celery(app)

from src.controllers import index


