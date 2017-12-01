import json

import urllib3

from encrypt import encode


def login(user_name, pass_word):
    key_id, pass_word = encode(pass_word)
    http_pool = urllib3.PoolManager()
    url = "http://localhost:18888/users/token/"+user_name
    response = http_pool.request("GET", url, headers={'passWord': pass_word, 'keyId': key_id})
    return json.loads(response.data)


