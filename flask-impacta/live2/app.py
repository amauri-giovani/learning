from flask import Flask
from deputados.routes import bp_deputados


app = Flask(__name__)
app.register_blueprint(bp_deputados)
