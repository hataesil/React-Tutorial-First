import pandas as pd
# df = pd.DataFrame(
#         {"a" : [4,5,6],
#         "b" : [7,8,9],
#         "c" : [10,11,12]},
#     index = [1,2,3])
# print(df)
# df = pd.DataFrame.read_csv('Qsheet1.csv')
# print(df.to_string())
df = pd.DataFrame.read_csv('data.csv')
# df = df.read_csv('data.csv')
print(df.to_string())
