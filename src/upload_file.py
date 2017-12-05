# -*- coding: UTF-8 -*-

import json

import urllib3

file_id = "63UBnNc1Q8J18BDcsrbOQg=="

http_pool = urllib3.PoolManager()
response = http_pool.request("DELETE", "http://localhost:18888/file/test66/" + file_id)
print(json.loads(response.data))
