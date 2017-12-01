import json

import urllib3


def update_user(user_info, token):
    http_pool = urllib3.PoolManager()

    response = http_pool.request("PUT", "http://localhost:18888/users/info/" + user_info['userName'],
                                 body=json.dumps(user_info),
                                 headers={'Content-Type': 'application/json', 'token': token})
    return json.loads(response.data)
