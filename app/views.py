from app import app
from flask import render_template
from .requests import get_sources

@app.route('/')
def index():
    sources_list = get_sources()
    title = 'Sources'
    print(sources_list[0].__dict__)
    return render_template('index.html', sources = sources_list, title= title)

@app.route('/source/<name>')
def source(name):
    return f"<h1>Hello {name}</h1>"