import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

#조회 시작 & 마감 날짜
start = datetime.datetime(2018, 2, 1)
end = datetime.datetime(2018, 2, 15)

#Google API 금융 정보 호출
gs = web.DataReader('NKRX: 035720', 'google', start, end) #카카오
#gs = web.DataReader('NKRX: 035720', 'google')
print(gs)
print(gs.index)
print(gs['Open']) #시가
print(gs.ix['2018-02-13']) #row
print(gs.describe())
