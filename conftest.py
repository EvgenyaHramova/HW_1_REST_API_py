import json
import pytest
import yaml
import requests

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

url = conf['url_'] 
url_posts = conf['url_posts']   

@pytest.fixture()
def get_token():
    response = requests.post(url=conf['url_'], 
                             data={'username': conf['username'], 
                                   'password': conf['password']})
    token = response.json()['token']
    return token
#
@pytest.fixture()
def post_new_post():
    body = json.dumps({
        'title': 'TITLE_TITLE',
        'description': 'gggggggggggggggggggggggggggggggg',
        'content': 'To be or not to be, that is the question'     
        })
    
    response = requests.post(url=conf['url_posts'],
                             headers={"X-Auth-Token": conf['token']},
                             data= {'item': body},
                             params={"owner": "notMe"}
                            )
    return response.json()['description']