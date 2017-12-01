# -*- coding: UTF-8 -*-
import urllib3


def delete_user(user_name, token):
    http_pool = urllib3.PoolManager()
    response = http_pool.request("DELETE", "http://localhost:18888/users/info/" + user_name,
                                 headers={'token': token})
    return response
