#데이터 추출 프로그램

import pandas as pd
import pymysql

# DB 접속 정보 작성
conn = pymysql.connect(host='localhost', user='root', password='personal pw', db='personal database name', charset='utf8')
# 모든 column 선택
query = 'SELECT * FROM reviewInformation'
df = pd.read_sql_query(query, conn)
# csv 파일로 저장
df.to_csv(r'C:\Users\82104\Desktop\movie_review_2021.csv', index=False)