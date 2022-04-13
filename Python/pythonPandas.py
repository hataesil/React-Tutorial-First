# 2022-03-16
# Pandas 
import pandas as pd
print(pd.__version__)

# Pandas Series
a = [1,3,7,9,11,13,15]
var = pd.Series(a)
print(var)

# Labels
print(var[0])

# Create Lavels
a = [1,7,2]
var = pd.Series(a, index = ["x","y","z"])
print(var)
print(var["y"])

# Key / Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3":390}
var = pd.Series(calories)
print(var)

myvar = pd.Series(calories, index = ["day1","day2"])
print(myvar)

# DataFrames
data = {
    "calories": [420,380,390],
    "duration":[50,40,45]
}
df = pd.DataFrame(data)
print(df)
# Named Indexes  Add a list of names to give each row a name:
df = pd.DataFrame(data,index = ["day1","day2","day3"])
print(df)

# Locate Row  - loc 속성은 한개나 더 많은 행을 리턴해준다
print(df.loc["day1"])
# print(df.loc[0,1])  When using [], the result is a Pandas DataFrame.
print(df.loc[["day1","day3"]])


# 2022-03-17
# Load Files into a DataFrame
# CSV files 컨트롤
# df = pd.read_csv('web\Python\data.csv')
# print(df.to_string()) # to_string() 전체 DataFrame을 인쇄하는데 사용한다
# print(df) # print(df) 는 커다란 DataFrame에서 first 5rows, last 5rows 만인쇄
# print(pd.options.display.max_rows) # 현재 system에서 최대행 확인
# pd.options.display.max_rows = 9999 최대행수 늘리기

# JSON read
#df = pd.read_json('data.json')
#print(df.to_string())

# DataFrame Analysis
df = pd.read_csv('web\Python\data.csv') 
print(df.head(10))  #DataFrame의 빠른 개요를 얻기 위해 가장 많이 사용되는 방법 중 하나는 head()메서드입니다.
# 행수를 지정하지 않으면 처음 5개 행을 인쇄합니다
print(df.tail()) # 마지막 5개의 행을 인쇄

# Data Information
print(df.info())

# Null Values
# 빈 값 또는 Null 값은 데이터를 분석할 때 좋지 않을 수 있으며 빈 값이 있는 행을 제거하는 것을 고려해야 합니다. 이것은 데이터 정리 라고 하는 것을 향한 단계이며 다음 장에서 이에 대해 더 배우게 될 것입니다.

# Cleaning Empty Cells
# 1: 빈셀이 포함된 행을 제거하는 법 dropna()
df = pd.read_csv('web\Python\data.csv')
new_df = df.dropna()   # 빈셀이 없는 새로운 프레임을 return
print(new_df.to_string)
# 기본적으로 dropna()메서드는 새 DataFrame을 반환하고 원본을 변경하지 않습니다.
# 원본을 변경하려면 inplace = True 인수를 사용
df = pd.read_csv('web\Python\data.csv')
df.dropna(inplace= True)

# 2.빈값을 바꾸기  fillna()
df=pd.read_csv('web\Python\data.csv')
df.fillna(130, inplace=True) # Null 값을 숫자 130 으로 바꾼다(전체)
df["Calories"].fillna(130, inplace = True) #Calories row Null 값을 130 으로 바꾼다
# mean(), median(), mode() 메소드를 사용하여 지정된 열에 각 값을 계산
df = pd.read_csv('web\Python\data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
# median 중앙값 , mode 최빈값

# 잘못된 데이터 수정
# Wrong Data Fixing
# Replacing Valus
# Set "Duration" = 45 in row :
#df.loc[7, 'Duration'] = 45
#df.loc

#for x in df.index:
#    if df.loc[x, "Duration"] > 120:
#        df.loc[x, "Duration"] = 120
    
# 행저거 방식(120보다 큰 행 삭제)
#for x in df.index:
#  if df.loc[x, "Duration"] > 120:
#    df.drop(x, inplace = True)

# Removing Duplicates 중복제거
# print(df.duplicated())
# df.drop_duplicates(inplace = True)

# Data Correlations 
df.corr()  #이 corr()방법은 "숫자가 아닌" 열을 무시합니다.
# 완전한 상관관계 1  

# Plotting 그래프 그리기
# df.plot()
# plt.show()

# Scatter Plot 산점도 그리기
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('data.csv')
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

# Histogram
# df["Duration"].plot(kind = 'hist') 히스토그램



