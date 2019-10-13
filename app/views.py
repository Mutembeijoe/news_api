from app import app
from flask import render_template
from .requests import get_sources,get_specific_source

@app.route('/')
def index():
    sources_list = get_sources()
    title = 'Sources'
    return render_template('index.html', sources = sources_list, title= title)

@app.route('/source/<name>')
def source(name):
    articles_list = get_specific_source(name)
    if len(articles_list) > 0:
        source = articles_list[0].source['name']
    else:
        source = None
    title = f"{name} articles"
    return render_template('source_articles.html', articles = articles_list, title=title, source = source)