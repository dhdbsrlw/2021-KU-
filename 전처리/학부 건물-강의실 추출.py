import pandas as pd

df = pd.read_table('C:/Users/lyj/Desktop/데이터톤/학부 강의목록 전처리.txt', sep='\t')

#df1 = df.sort_values(by=['building', 'room'], axis=0).reset_index(drop=True)
#df1.to_csv('대학원 강의목록 전처리 정렬.txt',index=False,sep=',')

df = df[['building','room']]

#df = df[['building']]

df = df.drop_duplicates().reset_index(drop=True)
df = df.sort_values(by=['building', 'room'], axis=0).reset_index(drop=True)

pd.set_option('display.max_rows', None)
print(df)


df.to_csv('학부 강의 건물-강의실.txt',index=False,sep=',')


##### 학부-대학원 강의실 concat #####
import pandas as pd

df1 = pd.read_table('C:/Users/lyj/Desktop/데이터톤/대학원 강의 건물-강의실.txt', sep=',')
#print(df1)

df2 = pd.read_table('C:/Users/lyj/Desktop/데이터톤/학부 강의 건물-강의실.txt', sep=',')
#print(df2)

df = pd.concat([df1, df2], axis=0).reset_index(drop=True)
df = df.drop_duplicates().reset_index(drop=True)
pd.set_option('display.max_rows', None)
df = df.sort_values(by=['building', 'room'], axis=0).reset_index(drop=True)

df.to_csv('건물-강의실.txt',index=False,sep=',')
print(df)
