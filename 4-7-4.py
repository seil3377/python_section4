import matplotlib.pyplot as plt

#리스트 범위(x축)
x = range(0, 256)
print(x)

#리스트 범위(y축)
y = []
for v in x:
    y.append(v*v)
#y = [v*v for v in x]
print(y)

#차트 설정1
#plt.plot(x, y)

#차트 설정2
#plt.plot(x, y, 'ro')
plt.plot(x, y, 'b--')

#차트 실행
plt.show()
