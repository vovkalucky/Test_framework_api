import os

class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: 'https://api.restful-api.dev/',
        PROD: 'https://api.restful-api.dev/prod'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV


ENV_OBJECT = Environment()