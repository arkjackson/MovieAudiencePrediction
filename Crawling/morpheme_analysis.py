# 형태소 분석 프로그램

import pandas as pd
from konlpy.tag import Okt

# csv파일 읽어오기
csv = pd.read_csv(r'C:\Users\82104\Desktop\movie_review_2021.csv',\
                  names=['movie_title', 'released_date', 'comment', 'writing_date', 'star_score', 'upvote', 'downvote', 'save_date'],\
                  encoding='CP949')
# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
okt = Okt()
# 명사, 동사, 형용사 별로 개수 분류
for i in range(1, len(csv['comment'])):
    if str(csv['comment'][i]) == 'nan':
        continue
    dic = {'Noun': 0, 'Verb': 0, 'Adjective': 0}
    word_class = okt.pos(csv['comment'][i])
    for j in range(len(word_class)):
        if word_class[j][1] == 'Noun':
            dic['Noun'] += 1
        elif word_class[j][1] == 'Verb':
            dic['Verb'] += 1
        elif word_class[j][1] == 'Adjective':
            dic['Adjective'] += 1
    print(i)
    print(csv['movie_title'][i], dic)