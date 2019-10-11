from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# initialize app
app = Flask(__name__,instance_relative_config=True)
bootstrap = Bootstrap(app)

# set up configurations
app.config.from_pyfile('config.py')
app.config.from_object(DevConfig)
from app import views