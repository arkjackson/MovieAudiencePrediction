from konlpy.tag import Okt
import time

# 긍정, 부정 명사 리스트
res_pos_lst = ['최고', '다시', '명작', '꼭', '마음', '또', '가슴', '인생', '기억', '눈물', '매력', '한번', '여운', '현실', '굿', '음악', '우리', '추천', '가장', '대박', '아이', '번', '만', '저', '인간', '모습', '짱', '알', '속', '모두', '삶', '대한', '함', '가족', '기대', '계속']
res_neg_lst = ['쓰레기', '최악', '이건', '돈', '별로', '개', '수준', '무슨', '못', '전개', '소재', '실망', '원작', '점도', '노잼', '게', '별', '전혀', '차라리', '알바', '급', '작가', '자체', '보지', '코미디', '욕', '뿐', '일본', '막장', '뭔가', '중간', '도대체']
# train 영화 리스트
movie_title_lst = [['pmc 더 벙커', '샹치와 텐 링즈의 전설', '대호', '담보', '인질', '크루엘라'],
                    ['나우유씨미 마술사기단', '마녀 Part2', '보스베이비', '트랜스포머 최후의 기사', '형'],
                    ['돈', '인크레더블2', '토이스토리4'],
                    ['강철비', '신비한 동물사전', '주토피아'],
                    ['아쿠아맨','청년경찰'],
                    ['럭키', '미션임파서블 로그네이션'],
                   ['1987', '공조'],
                   ['백두산', ],
                   ['보헤미안 랩소디'],
                   ['겨울왕국2', '기생충']]
# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.
okt = Okt()
res = []
for i in range(len(movie_title_lst)):
    pos_noun_number = 0
    neg_noun_number = 0
    for j in range(len(movie_title_lst[i])):
        filename = 'C:/Users/82104/Desktop/영화댓글수집/영화/' + movie_title_lst[i][j] + '.txt'
        f = open(filename, 'r', encoding='utf8')
        sentences = f.readlines()
        for k in range(len(sentences)):
            words = okt.pos(sentences[k])
            print(sentences[k])
            for l in range(len(words)): # 긍정, 부정 명사 별로 카운트
                if words[l][1] == 'Noun':
                    if words[l][0] in res_pos_lst:
                        pos_noun_number += 1
                    elif words[l][0] in res_neg_lst:
                        neg_noun_number += 1
    res.append([pos_noun_number / len(movie_title_lst[i]), neg_noun_number / len(movie_title_lst[i])])
    print("positive number of noun:", pos_noun_number / len(movie_title_lst[i]))
    print("negative number of noun:", neg_noun_number / len(movie_title_lst[i]))
    time.sleep(2)

for i in range(10):
    print(str(100 * (i + 1)) + '만 대 :',res[i])