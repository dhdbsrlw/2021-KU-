import pandas as pd

df = pd.read_table('C:/Users/이연정/Desktop/데이터톤/대학원 강의목록 1차 전처리.txt', sep='\t')
pd.set_option('display.max_rows', None)
#print(df)

df1 = df[df['time'].str.len()<=2].reset_index(drop=True)
pd.set_option('display.max_rows', None)
#print(df1)
df1 = df1.replace({'time': '1'}, {'time': '09:00-10:30'})
df1 = df1.replace({'time': '2'}, {'time': '10:30-12:00'})
df1 = df1.replace({'time': '3'}, {'time': '12:00-13:00'})
df1 = df1.replace({'time': '4'}, {'time': '13:00-14:00'})
df1 = df1.replace({'time': '5'}, {'time': '14:00-15:30'})
df1 = df1.replace({'time': '6'}, {'time': '15:30-17:00'})
df1 = df1.replace({'time': '7'}, {'time': '17:00-18:30'})
df1 = df1.replace({'time': '8'}, {'time': '18:30-20:00'})
df1 = df1.replace({'time': '9'}, {'time': '20:00-21:30'})
df1 = df1.replace({'time': '10'}, {'time': '21:30-23:00'})
df1 = df1.replace({'time': '11'}, {'time': '23:00-00:30'})

#df1 = df1.loc[df1['time']==1] = '09:00-10:30'
#print(df1)

spilt_df1 = pd.DataFrame(df1['time'].str.split('-', 1).tolist(), columns = ['start','end'])
df1 = pd.concat([df1, spilt_df1], axis=1)
#print(df1)
df1 = df1.drop(['time'], axis=1)
print(df1)

#df1.to_csv('df1.txt',index=False,sep='\t')




df2 = df[df['time'].str.len() > 2].reset_index(drop=True)
pd.set_option('display.max_rows', None)

#print(df2)

spilt_df2 = pd.DataFrame(df2['time'].str.split('-', 1).tolist(), columns = ['start','end'])
#print(spilt_df2)

spilt_df2 = spilt_df2.replace({'start': '1'}, {'start': '09:00'})
spilt_df2 = spilt_df2.replace({'start': '2'}, {'start': '10:30'})
spilt_df2 = spilt_df2.replace({'start': '3'}, {'start': '12:00'})
spilt_df2 = spilt_df2.replace({'start': '4'}, {'start': '13:00'})
spilt_df2 = spilt_df2.replace({'start': '5'}, {'start': '14:00'})
spilt_df2 = spilt_df2.replace({'start': '6'}, {'start': '15:30'})
spilt_df2 = spilt_df2.replace({'start': '7'}, {'start': '17:00'})
spilt_df2 = spilt_df2.replace({'start': '8'}, {'start': '18:30'})
spilt_df2 = spilt_df2.replace({'start': '9'}, {'start': '20:00'})
spilt_df2 = spilt_df2.replace({'start': '10'}, {'start': '21:30'})
spilt_df2 = spilt_df2.replace({'start': '11'}, {'start': '23:00'})

spilt_df2 = spilt_df2.replace({'end': '1'}, {'end': '10:30'})
spilt_df2 = spilt_df2.replace({'end': '2'}, {'end': '12:00'})
spilt_df2 = spilt_df2.replace({'end': '3'}, {'end': '13:00'})
spilt_df2 = spilt_df2.replace({'end': '4'}, {'end': '14:00'})
spilt_df2 = spilt_df2.replace({'end': '5'}, {'end': '15:30'})
spilt_df2 = spilt_df2.replace({'end': '6'}, {'end': '17:00'})
spilt_df2 = spilt_df2.replace({'end': '7'}, {'end': '18:30'})
spilt_df2 = spilt_df2.replace({'end': '8'}, {'end': '20:00'})
spilt_df2 = spilt_df2.replace({'end': '9'}, {'end': '21:30'})
spilt_df2 = spilt_df2.replace({'end': '10'}, {'end': '13:00'})
spilt_df2 = spilt_df2.replace({'end': '11'}, {'end': '00:30'})


df2 = pd.concat([df2, spilt_df2], axis=1)
#print(df2)
df2 = df2.drop(['time'], axis=1)
#print(df2)


#print(spilt_df2)
#print(df2)


#df2.to_csv('df2.txt',index=False,sep='\t')


