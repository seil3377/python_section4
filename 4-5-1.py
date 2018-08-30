#1. Python Pandas 개요
#2. CSV 데이터 간단 개요
#3. 파이썬 Pandas로 CSV 데이터 읽고쓰기
#4. 파이썬 Pandas로 CSV 데이터 편집하기

import pandas as pd
import csv

#기본 읽기
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv')
print(df)

#행 스킵
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0])
print(df)

#행 스킵, 헤더 생략
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0],header=None)
print(df)

#헤더 정의
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960])
print(df)

#인덱스 컬럼 정의
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960], index_col=[0])
print(df)

#특정 값 치환
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960], na_values=["JAN"])
print(pd.isnull(df))
print(df)

#실습 정리 및 인덱스 재 정의
df = pd.read_csv('d:/Atom_Workspace/section4/csv_s1.csv', skiprows=[0],header=None, names=["Month",1958,1959,1960])
print(df)
print(df.index) #RangeIndex(start=0, stop=12, step=1)
print(list(df.index)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#print(df.index.values.tolist()) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df.index.values) #[ 0  1  2  3  4  5  6  7  8  9 10 11]
print(df.rename(index=lambda x : x+1)) #람다식을 이용하여 index 변경
print(df.rename(index=lambda x : x+1).index) #Int64Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype='int64')



#읽기
df2 = pd.read_csv('d:/Atom_Workspace/section4/csv_s2.csv',sep=';', skiprows=[0], header=None, names=["First name", "Test1", "Test2", "Test3", "Final", "Grade"])
print(df2)

#Columns 값 수정
df2['Grade'] = df2['Grade'].str.replace('"', ' ')

#평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1) # 0:열 1:행

#합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)

print(df2)
