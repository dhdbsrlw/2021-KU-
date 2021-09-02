import pandas as pd

df = pd.read_table('C:/Users/dldus/Desktop/학부 강의목록 전처리.txt', sep='\t')
pd.set_option('display.max_rows', None)
print(df)


df = df.replace({'start': '09:00'}, {'start': '09:00'})
df = df.replace({'start': '10:30'}, {'start': '10:30'})
df = df.replace({'start': '12:00'}, {'start': '12:00'})
df = df.replace({'start': '13:00'}, {'start': '13:00'})
df = df.replace({'start': '14:00'}, {'start': '14:00'})
df = df.replace({'start': '15:30'}, {'start': '15:30'})
df = df.replace({'start': '17:00'}, {'start': '17:00'})
df = df.replace({'start': '18:30'}, {'start': '18:00'})
df = df.replace({'start': '20:00'}, {'start': '19:00'})
df = df.replace({'start': '21:30'}, {'start': '20:00'})
df = df.replace({'start': '23:00'}, {'start': '21:00'})

df = df.replace({'end': '10:30'}, {'end': '10:30'})
df = df.replace({'end': '12:00'}, {'end': '12:00'})
df = df.replace({'end': '13:00'}, {'end': '13:00'})
df = df.replace({'end': '14:00'}, {'end': '14:00'})
df = df.replace({'end': '15:30'}, {'end': '15:30'})
df = df.replace({'end': '17:00'}, {'end': '17:00'})
df = df.replace({'end': '18:30'}, {'end': '18:00'})
df = df.replace({'end': '20:00'}, {'end': '19:00'})
df = df.replace({'end': '21:30'}, {'end': '20:00'})
df = df.replace({'end': '13:00'}, {'end': '21:00'})
df = df.replace({'end': '00:30'}, {'end': '22:00'})


pd.set_option('display.max_rows', None)

df = df.sort_values(by=['building', 'room'], axis=0).reset_index(drop=True)
print(df)
df.to_csv('학부 강의목록 전처리(시간수정).txt',index=False,sep='\t')


