from app import app
import urllib.request,json
from .models import source

Source = source.Source



all_sources_url = app.config['ALL_SOURCES_URL']
api_key = app.config['API_KEY']


def get_sources():
    get_sources_url = all_sources_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        sources_raw_data = url.read()
        sources_response = json.loads(sources_raw_data)

    sources_list = None

    if sources_response['sources']:
        new_list = []
        for source in sources_response['sources']:
            id = source['id']
            name = source['name']
            description = source['description']
            new_source = Source(id,name,description)
            new_list.append(new_source)

        sources_list = new_list


    return sources_list

