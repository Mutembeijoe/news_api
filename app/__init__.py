from flask import Flask

from .config import DevConfig

# initialize app

app = Flask(__name__)

# set up configurations

app.config.from_pyfile('config.py')
app.config.from_object(DevConfig)
from app import views