#1. JSON 데이터 간단 개요
#2. 파이썬으로 JSON 데이터 읽고 쓰기
#3. 파이썬으로 JSON 데이터 파싱 하기
#4. Github Repository JSON 데이터 파싱 실습

import simplejson as json
#import json

#Dict(Json)선언
data = {}
data['people'] = []

data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
})

data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})

print(data)

#data = {'people': [{'from': 'Seoul', 'website': 'naver.com', 'name': 'Kim'}, {'from': 'Busan', 'website': 'google.com', 'name': 'Park'}, {'from': 'Incheon', 'website': 'daum.net', 'name': 'Lee'}]}

#Dict(Json) -> Str
e = json.dumps(data, indent=4) #들여쓰기 옵션
print(type(e))
print(e)

#Str -> Dict(Json)
d = json.loads(e)
print(type(d))
print(d)

#json 파일 쓰기(dumps) : 문자열을 다룸
with open('d:/Atom_Workspace/section4/member.json','w') as outfile:
    outfile.write(e)

#json 파일 읽기(loads)
with open('d:/Atom_Workspace/section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print('=====')
    #print(type(r))
    #print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
