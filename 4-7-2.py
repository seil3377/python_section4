from pandas import Series, DataFrame
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Dict 선언
r_data = {'City': ['서울','대구','부산','대전'], 'Total1':[55000, 47000, 49000, 42000], 'Total2': [65000, 57000, 53000, 48000]} #key는 영문으로
i_data = ['one','two','three','four']
print(r_data)
print(i_data)

#DataFrame 정의
d_frame = DataFrame(r_data, index=i_data)
print(type(d_frame))
print(d_frame)
print(d_frame.index)
print(d_frame.values)
print(d_frame['City']) #Columns
print(d_frame.ix['one']) #rows

#요약
print(d_frame.describe())

#값 순회
for e in d_frame.values:
    #print(e) #리스트 형태
    for i, z in enumerate(e):
        print(i,z)
