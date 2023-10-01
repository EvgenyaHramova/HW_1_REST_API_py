import json
import requests as requests
import yaml

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

def get_token():
    response = requests.post(url=conf['url_'], 
                             data={'username': conf['username'],
                                   'password': conf['password']})
    return response.json()['token']
#print(response.json()['token'])

# def get(token: str):
#     response = requests.get(conf["url_posts"],
#                             headers={"X-Auth-Token": token},
#                             params={"owner": "notMe"}).json()
#     return response
def get_posts(token):
    response = requests.get(conf["url_posts"],
                            headers={"X-Auth-Token": token},
                            params= {"owner": "Me"}
                            ).json()
    return  response

# создание поста

def post_new_post(token):
    body = {
        'title': 'TITLE_TITLE',
        'description': 'gggggggggggggggggggggggggggggggg',
        'content': 'To be or not to be, that is the question'     
        }
    response = requests.post(url=conf['url_posts'],
                             headers={"X-Auth-Token": token},
                             json=body
                            
                            )
    return response.json()

if __name__ == '__main__':
    #print(get_token())
    temp_token = get_token()
    #print(get(temp_token))
    #print(get_posts(temp_token))
    #get_posts(temp_token)
    print(post_new_post(temp_token))