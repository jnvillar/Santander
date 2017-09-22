web: gunicorn application:app
init: python db_create.py
upgrade: python db_upgrade.py
clock: python santander/jobs/clock.py --loglevel=INFO