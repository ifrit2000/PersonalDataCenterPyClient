import json

import urllib3
from encrypt import encode

userInfo = {'userName': 'xxx',
            'nickName': 'Anthony',
            'passWord': 'xxx',
            'userType': '1',
            'telPhone': 'xxx',
            'eMail': 'xxx@163.com',
            'idCard': 'xxxxxxxxx'}


def registry(user_info):
    http_pool = urllib3.PoolManager()
    key_id, user_info['passWord'] = encode(user_info['passWord'])
    header = {'Content-Type': 'application/json', 'keyId': key_id}
    user_info = json.dumps(user_info).encode('utf-8')
    response = http_pool.request("POST", "http://localhost:18888/users/registry", body=user_info, headers=header)
    return json.loads(response.data)['token']


print(registry(userInfo))
