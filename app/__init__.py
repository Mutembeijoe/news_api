from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_moment import Moment



# initialize app
app = Flask(__name__,instance_relative_config=True)
bootstrap = Bootstrap(app)
moment = Moment(app)

# set up configurations
app.config.from_pyfile('config.py')
app.config.from_object(DevConfig)
from app import views