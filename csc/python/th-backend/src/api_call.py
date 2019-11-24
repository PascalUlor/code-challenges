import json
import requests


api_token = '83efa02aa0e40572bd9b3be4978c781d02a1c55e'
api_url_base = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Token {0}'.format(api_token)}

def get_data():

    api_url = '{0}account/keys'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


print(get_data())