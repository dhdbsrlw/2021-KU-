import pandas as pd

##### txt 파일 불러오기 #####
df = pd.read_table('C:/Users/이연정/Desktop/데이터톤/2019_1R.txt', sep='\t')

# count = 0
#print(df)

##### 주 1회 이상 수업하는 강의 전처리 (<br> 처리) #####
for i in range(0, 4247):
    if type(df.loc[i, '강의시간/강의실']) == type('string') and df.loc[i, '강의시간/강의실'].endswith('<br>'):
        #print(i)
        copy = df.loc[i, :]
        number_of_class = 0
        while True:    # 수업이 주 3, 4 회 있는 경우도 모두 고려 + 관련된 행에서 강의시간/강의실 정보만 바꿔 끝항에 추가
            number_of_class = number_of_class + 1
            copy.at['강의시간/강의실'] = df.loc[i + number_of_class, '년도']
            '''
            print(" **** change ******")
            print(copy)
            print(" **********")
            '''
            df = df.append(copy, ignore_index=True)
            # count = count + 1
            if df.loc[i+number_of_class, '년도'].endswith('<br>'):
                continue
            break

#print(count)

##### 2019년도로 시작하지 않는 모든 정보 삭제 #####
drop_index_year = df[df['년도'] != '2019'].index
df = df.drop(drop_index_year)

##### 강의실 정보가 있는 것만 남김 ######
df = df[df['강의시간/강의실'].str.contains('호|실', na=False)]
#pd.set_option('display.max_rows', None)
#print(df)


##### 요일(시간) 있는 것만 남김 #####
df = df[df['강의시간/강의실'].str.contains('월\(|화\(|수\(|목\(|금\(|토\(|일\(', na=False)]
#pd.set_option('display.max_rows', None)
#print(df)


##### 강의시간/강의실 정보만 추출 #####
extract_df = df[['강의시간/강의실']].reset_index(drop=True)
#pd.set_option('display.max_rows', None)
#print(extract_df)


##### (요일, 시간, 건물, 강의실) 로 열 쪼개기 #####
extract_df = pd.DataFrame(extract_df['강의시간/강의실'].str.split('(', 1).tolist(), columns = ['day','temp'])
day_time = pd.DataFrame(extract_df['temp'].str.split('\) ', 1).tolist(), columns = ['time','building_room'])
extract_df = pd.concat([extract_df, day_time], axis=1)
extract_df = extract_df.drop(['temp'], axis=1)
#pd.set_option('display.max_rows', None)
#print(extract_df)
building_room = pd.DataFrame(extract_df['building_room'].str.split(' ', 1).tolist(), columns = ['building','room'])
#extra = building_room[building_room['room'].isnull()]      # 띄어쓰기로 호가 쪼개지지 않은 모든 경우 찾아서 바꿈
#pd.set_option('display.max_rows', None)
#print(building_room)
#print(extra)
extract_df = pd.concat([extract_df, building_room], axis=1)
extract_df = extract_df.drop(['building_room'], axis=1)
#pd.set_option('display.max_rows', None)
#print(extract_df)



extract_df.to_csv('test.txt',index=False,sep='\t')


