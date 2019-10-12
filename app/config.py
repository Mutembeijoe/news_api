class Config:
    '''
    General app configurations
    '''
    ALL_SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'

    SOURCE_URL = ' https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True