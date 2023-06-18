import pandas as pd
from konlpy.tag import Okt

# nsmc 데이터 불러오기
raw_data = pd.read_csv('//ratings.txt', header=0, delimiter='\t', quoting=3)
raw_data.head()
# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
okt = Okt()
# label에 따른 명사 저장 변수
pos_noun = {}
neg_noun = {}
# label에 따라 명사 분류
for i in range(len(raw_data['document'])):
    if not isinstance(raw_data['document'][i], str):
        continue
    print(raw_data['document'][i])
    words = okt.pos(raw_data['document'][i])
    for j in range(len(words)):
        if words[j][1] == 'Noun':
            if raw_data['label'][i] == 1 and words[j][0] not in pos_noun:
                pos_noun[words[j][0]] = 1
            elif raw_data['label'][i] == 1 and words[j][0] in pos_noun:
                pos_noun[words[j][0]] += 1
            elif raw_data['label'][i] == 0 and words[j][0] not in neg_noun:
                neg_noun[words[j][0]] = 1
            elif raw_data['label'][i] == 0 and words[j][0] in neg_noun:
                neg_noun[words[j][0]] += 1
# 키 값 기준 내림차순 정렬
res_pos_noun_list = sorted(pos_noun.items(), key=lambda item:item[1], reverse=True)
res_neg_noun_list = sorted(neg_noun.items(), key=lambda item:item[1], reverse=True)
top_pos_noun_list = []
top_neg_noun_list = []
# 상위 100개 명사 저장
for i in range(100):
    top_pos_noun_list.append(res_pos_noun_list[i][0])
    top_neg_noun_list.append(res_neg_noun_list[i][0])
print(top_pos_noun_list)
print(top_neg_noun_list)
res_pos = []
res_neg = []
# 겹치는 명사 제거
for i in range(len(top_pos_noun_list)):
    if top_pos_noun_list[i] not in top_neg_noun_list:
        res_pos.append(top_pos_noun_list[i])
    if top_neg_noun_list[i] not in top_pos_noun_list:
        res_neg.append(top_neg_noun_list[i])
print(res_pos)
print(res_neg)