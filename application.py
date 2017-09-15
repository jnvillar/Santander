from flask import Flask
from santander.controllers.index import main

app = Flask('santander')
app.debug = True

# register blueprints
app.register_blueprint(main)
