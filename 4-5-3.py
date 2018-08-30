import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')) #0~100사이의 무작위 100*4 df
#df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
print(df)

#CSV 쓰기
df.to_csv('d:/Atom_Workspace/section4/result.csv',index=False)
#df.to_csv('d:/Atom_Workspace/section4/result.csv',index=False,header=False)
