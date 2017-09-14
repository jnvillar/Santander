from flask import Flask
from santander.controllers.index import main

app = Flask('santander')
app.config['SECRET_KEY'] = 'random'
app.debug = True

app.register_blueprint(main)
