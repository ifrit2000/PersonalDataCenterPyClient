import json

import urllib3

from encrypt import encode


def login(user_name, pass_word):
    key_id, pass_word = encode(pass_word)
    http_pool = urllib3.PoolManager()
    response = http_pool.request("POST", "http://localhost:18888/users/info/" + user_name,
                                 headers={'Content-Type': 'application/json'},
                                 body=json.dumps({'passWord': pass_word, 'keyId': key_id}))
    print(json.loads(response.data))


login('xxx', 'xxx')
