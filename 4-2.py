#1. XML 기상청 날씨 데이터 조회
#2. XML 기상청 날씨 데이터 지역별 파싱 및 출력
# http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp

import sys
import io
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#다운로드 url
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108" #전국 중기예보 RSS
savename = "D:/Atom_Workspace/section4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
print('다운로드 확인')

#BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

#지역확인
info = {} #{"서울":[-1,-5,-3,-4], ""}
for location in soup.find_all("location"): # xml을 파싱할때는 find가 더 효율적
    loc  = location.find("city").string
    #print(loc)
    weather = location.find_all("tmn")
    #print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
print(sorted(info))
#print(list(info.keys()))
#print(info.values())

#각 지역별 날씨 텍스트 쓰기
with open('d:/Atom_Workspace/section4/forecast.txt', 'wt') as f:
    for loc in sorted(info.keys()): #dict형을 for문에 쓰면 list형태로 자동 형변환 되어 사용됨
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]: #key 값의 value
            print('-',n)
            f.write('\t'+str(n)+'\n')
