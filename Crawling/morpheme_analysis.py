# 형태소 분석 프로그램
# 영화 별 명사, 동사, 형용사 수 저장
from konlpy.tag import Okt
import pandas as pd

# 결과값 .csv파일로 저장
def save_results_to_csv(lst):
    final=[]
    final.append(lst)
    # 데이터프레임 생성
    df = pd.DataFrame(final, columns=['Noun', 'Verb', 'Adjective'])
    df.to_csv("C:/Users/82104/Desktop/morphe.csv", index=False)
# 형태소 분석 이후 명사, 동사, 형용사 개수 카운트
def count_morpheme(s):
    word_class = okt.pos(s)  # 품사 부착
    for j in range(len(word_class)):
        if word_class[j][1] == 'Noun':  # 명사
            mor_list[0] += 1
        elif word_class[j][1] == 'Verb':  # 동사
            mor_list[1] += 1
        elif word_class[j][1] == 'Adjective':  # 형용사
            mor_list[2] += 1

# .csv 파일 대신 .txt 파일 읽기
filename = 'C:/Users/82104/Desktop/영화댓글수집/영화/대호.txt'
f = open(filename, 'r', encoding='utf8')
sentences = f.readlines()
# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
okt = Okt()
# 형태소 저장 변수
mor_list = [0, 0, 0]
for i in range(len(sentences)):
    # 공백 리뷰가 아닌 경우만 형태소 분석 실행
    if sentences[i] != "\n":
        print(sentences[i])
        # 형태소 개수 저장
        count_morpheme(sentences[i])
# 결과 .csv 파일로 저장
save_results_to_csv(mor_list)
# 결과 출력
print(mor_list)