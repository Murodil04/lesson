import json
# from turtle import back
# json.dumps,json.load
# son=77.67
# json_son=json.dumps(son)
# print(son,type(son))
# print(json_son,type(json_son))

# True-true
# isGrand=True
# json_true=json.dumps(isGrand)
# print(json_true)
# back_py=json.loads(json_true)
# print(back_py)

import requests
# url='https://jsonplaceholder.typicode.com/posts'
# data=requests.get(url)
# for i in data.json():
#     print(i)
#     print('====')

id=int(input('id:'))
try:
    url=f'https://jsonplaceholder.typicode.com/users/{id}'
    data=requests.get(url).json
    print(f"{['name']}-{['email']}")
except:
    print('error')

print('d')
print('d')
