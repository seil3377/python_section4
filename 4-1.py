#1. 머신러닝에서 다양한 형식 데이터 가공의 필요성
#2. 바이너리(Binary) 데이터 vs 텍스트(Text) 데이터
#3. 바이너리(Binary), 텍스트(Text) 데이터 생성 실습

import pickle #객체, 텍스트를 직렬화 & 역직렬화

# 파일 이름과 데이터
bfilename = "d:/Atom_Workspace/section4/test.bin"
tfilename = 'd:/Atom_Workspace/section4/test.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ["car", "animal", "house"]

# 바이너리 쓰기(객체 직렬화)
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f) #dump 객체를 바이너리로 쓸때, dumps 텍스트(문자열)를 직렬화 할 때
    pickle.dump(data2, f)
    pickle.dump(data3, f)

#텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

# 바이너리 읽기(역직렬화)
with open(bfilename, 'rb') as f:
    b = pickle.load(f) #loads(문자열로부터 역직렬화)
    print(type(b), ' Binary Read1 | ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2 | ', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3 | ', b)

'''
pickle(바이너리,자료형 유지)
<class 'int'>  Binary Read1 |  77
<class 'str'>  Binary Read2 |  Hello, world!
<class 'list'> Binary Read3 |  ['car', 'animal', 'house']
'''


# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + ' | ' + line, end='')

'''
텍스트(자료형 변환)
<class 'str'> Text Read1 | 77
<class 'str'> Text Read2 | Hello, world!
<class 'str'> Text Read3 | car
<class 'str'> Text Read4 | animal
<class 'str'> Text Read5 | house
'''
