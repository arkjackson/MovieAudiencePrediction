# 형태소 분석 프로그램
# 영화 별 명사, 동사, 형용사 수 저장

from konlpy.tag import Okt

# .csv 파일 대신 .txt 파일 읽기
filename = 'C:/Users/82104/Desktop/movie_name.txt'
f = open(filename, 'r', encoding='utf8')
sentences = f.readlines()
# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
okt = Okt()
# 형태소 저장 변수
dic = {'Noun': 0, 'Verb': 0, 'Adjective': 0}
for i in range(len(sentences)):
    # 공백 리뷰가 아닌 경우
    if sentences[i] != "\n":
        print(sentences[i])
        word_class = okt.pos(sentences[i])  # 품사 부착
        for j in range(len(word_class)):
            if word_class[j][1] == 'Noun':  # 명사
                dic['Noun'] += 1
            elif word_class[j][1] == 'Verb':    # 동사
                dic['Verb'] += 1
            elif word_class[j][1] == 'Adjective':   # 형용사
                dic['Adjective'] += 1
# 결과 출력
print(dic)