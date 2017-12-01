from deleteuser import delete_user
from registry import registry
from login import login
from update_user import update_user

user_name = 'test66'
pass_word = 'cd123321'
userInfo = {'userName': user_name,
            'nickName': 'Anthony',
            'passWord': pass_word,
            'userType': '1',
            'telPhone': 'xxx',
            'eMail': 'xxx@163.com',
            'idCard': 'xxxxxxxxx'}
#registry(userInfo)

#res = login(user_name, pass_word)
#print(res)
#user_info=res['data']
user_info=userInfo
user_info['nickName']='Anthony'

print(update_user(user_info,'HJOqWjNQIIGH3t-3WV7DAw'))

#print(res['token'])
#delete_user(user_name, res['token'])

