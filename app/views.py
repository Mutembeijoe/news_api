from app import app
from flask import render_template
from .requests import get_sources



@app.route('/')
def index():
    sources_list = get_sources()
    title = 'Sources'
    return render_template('index.html', sources = sources_list, title= title)