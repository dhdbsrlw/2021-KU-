< 강의실 readme.txt >

1. 강의실 건물별 TOP3.ipynb : 건물당 가장 사용이 적고 넓은 강의실을 최대 3개 추출
2. 강의실_사용자_데이터.ipynb : 강의실 가상 사용자 생성
3. 사용자_강의실_점수.ipynb : 강의실 가상 사용자 True label 생성
4. 강의실 mlp 모델 최종.ipynb : 강의실 mlp 추천 모델
5. CollaborativeFiltering 강의실.ipynb : 강의실 SVD 이용 CollaborativeFiltering 추천 모델
6. ContentsFiltering_강의실.ipynb : 강의실 코사인 유사도 이용 ContentFiltering 추천 모델
7. classroom_model : 강의실 mlp 추천 모델 코드의 학습된 모델 결과 저장
8. events.out.tfevents.1628444437.4ae6496d5d5f : 강의실 mlp 모델 loss 
9. 이동시간_계산.ipynb : 교내 랜드마크(건물 혹은 명소) 간의 거리 측정 코드

< 라운지 + 혼잡도 readme.txt > 

1. 라운지_가상데이터 최종.ipynb : 가상 라운지 생성
2. 라운지_모델_최종.ipynb : 라운지 mlp 추천 모델
3. 라운지_사용자_데이터 최종.ipynb : 라운지 가상 사용자 생성
4. 라운지_트루라벨_모델 최종.ipynb : 라운지 가상 사용자 True label 생성
5. 혼잡도_데이터.ipynb : 혼잡도 생성 
6. CollaborativeFiltering 라운지.ipynb : 라운지 SVD 이용 CollaborativeFiltering 추천 모델
7. ContentsFiltering_라운지.ipynb : 라운지 코사인 유사도 이용 ContentFiltering 추천 모델
8. model_0/1/2/3 : 라운지 mlp 추천 모델 코드의 학습된 모델 결과 저장



< 전처리 readme.txt>

1. 학부 건물-강의실 추출.py : 2019 1R 학부 강의 목록에서 건물과 강의실만 추출하는 코드
2. 대학원 건물-강의실 추출.py : 2019 1R 학부 강의 목록에서 건물과 강의실만 추출하는 코드
3. 교시 to 시간.py : 강의목록 데이터의 모든 교시에 대해 시간으로 값을 바꾸는 코드 (ex. 1교시 -> 9:00 - 10:30)
4. 시간 수정 코드.py : 교시 to 시간.py 코드에서 잘못된 시간을 바로잡는 코드
5. 각 요일 별 강의실 사용 시간 정리.ipynb : 추출한 모든 강의실에 대해 어떤 요일 무슨 시간 대에 쓰이는지 전처리 



< 챗봇 실제 적용 모델 readme.txt >

1. classroom_mlp_model.ipynb : 챗봇에 실제 연결시킨 강의실 mlp 추천 코드 
2. lounge_mlp_model.ipynb : 챗봇에 실제 연결시킨 라운지 mlp 추천 코드



< 챗봇 readme.txt >

1. ngrok.ipynb : 외부에서 로컬 서버 접속 환경 설정 
2. Set Database.ipynb : 데이터베이스 설정 파일
3. webhook.ipynb : 웹훅을 받아서 데이터 처리 및 응답하는 메인 코드

< 챗봇 실행 방법 >
1. Flask 서버 실행 (GCP 프로젝트 구성원으로 등록 이후 실행 가능)
- GCP (Google Cloud Platform) 콘솔에서 get-me-classrooms 프로젝트 접속
- 콘솔에서 ‘datalab connect get-me-classrooms --no-user-checking’ 입력
- datalab 에서 ngrok.ipynb 실행
- webhook.ipynb 첫 블록 (pip install ~) 실행 (패키지 설치 및 버전 업데이트)
- webhook.ipynb 에서 reset session
- webhook.ipynb 두 번째 블록부터 마지막 블록까지 실행
- ngrok.ipynb 출력에서 외부에서 접속 가능한 url 복사

2. Dialogflow Agent 연결
- Dialogflow 에서 ‘구해줘룸즈’ 에이전트 선택
- Fulfillment 탭에서 URL에 1에서 복사한 url/webhook/ 입력 후 save

3. Dialogflow Messenger 과 통합
- Integration 탭에서 Dialogflow Messenger 선택
- ENABLE 클릭
- TRY IT NOW 클릭
- 챗봇 연결 완료




