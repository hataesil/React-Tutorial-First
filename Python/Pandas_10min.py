import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan,6,8])
#print(s)
dates = pd.date_range('20210101', periods=6)
#print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print(df)
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
# print(df2)
# a1 = df.head()
# a2 = df.tail(3)
# a3 = df.index
# a4 = df.values
# a5 = df.describe()
# a6 = df.T
# a7 = df['A']
# a8 = df[df>0]
#print(a8)
#통계
a10 = df.mean()
print(a10)
