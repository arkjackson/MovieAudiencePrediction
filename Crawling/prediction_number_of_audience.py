# ver 0.1
# 명사, 동사, 형용사 수 별로 기준 데이터에 가장 가까운 값이 영화의 관객 수로 예측하는 프로그램

import pandas as pd
import time

# 결과 출력 함수
def print_prediction_message(number_audience, idx_lst):
    morpheme = ['명사', '동사', '형용사']
    for i in range(len(morpheme)):
        print("\n" + morpheme[i] + " 기준:", str(100 * idx_lst[i]) + '~' + str(100 * (idx_lst[i] + 1)) + "만 명", end=' ')
        if 100 * idx_lst[i] <= number_audience and number_audience < 100 * (idx_lst[i] + 1):
            print("---> 예측 성공")
        elif 100 * (idx_lst[i] - 1) <= number_audience and number_audience < 100 * (idx_lst[i] + 2):
            print("---> 예측 근사")
        else:
            print("---> 예측 실패")

# 관객 수에 따라 품사수 저장
df = pd.read_csv('C:/Users/82104/Desktop/morpheme_result.csv')
noun_list = df['Noun'].values
verb_list = df['Verb'].values
adj_list = df['Adjective'].values
diff_noun = 100000
n_i = 0
diff_verb = 100000
v_i = 0
diff_adj = 100000
a_i = 0
# 예측 대상에 대한 형태소 분석 결과
movie_mor_list = [[64679, 25597, 15681], [111933, 36637, 25878], [129314, 37999, 22231],
                  [50165, 13969, 10777], [23362, 7283, 6422]]
# 예측 대상의 실제 관객수
movie_real_number_audience = [204, 361, 475, 296, 160]
# 예측 대상
movie_name_list = ["소울", "모가디슈", "남산의 부장들", "블랙위도우", "닥터두리틀"]
while True:
    # 입력 화면
    print("아래에 보이는 영화 중 예측을 원하는 영화의 번호를 입력하세요!")
    print("1. " + movie_name_list[0] + "   2. " + movie_name_list[1] + "   3. " + movie_name_list[2] + "   4. " + movie_name_list[3] + "   5. " + movie_name_list[4])
    movie_num = input()
    if movie_num == "1" or movie_num == "2" or movie_num == "3" or movie_num == "4" or movie_num == "5":
        movie_num = int(movie_num)
        # 가장 오차가 적을 떄의 관객 수 찾기
        for i in range(len(noun_list)):
            if diff_noun > abs(movie_mor_list[movie_num - 1][0] - noun_list[i]):
                diff_noun = abs(movie_mor_list[movie_num - 1][0] - noun_list[i])
                n_i = i
            if diff_verb > abs(movie_mor_list[movie_num - 1][1] - verb_list[i]):
                diff_verb = abs(movie_mor_list[movie_num - 1][1] - verb_list[i])
                v_i = i
            if diff_adj > abs(movie_mor_list[movie_num - 1][2] - adj_list[i]):
                diff_adj = abs(movie_mor_list[movie_num - 1][2] - adj_list[i])
                a_i = i
        # 리스트화
        index_list = [n_i, v_i, a_i]
        # 딜레이
        print("'" + movie_name_list[movie_num - 1] + "'" + " 관객 수를 예측하고 있습니다! 잠시만 기다려주세요!")
        time.sleep(2)
        # 결과 화면
        print("---------------" + movie_name_list[movie_num - 1] + " 관객수 예측-------------------")
        print("실제 관객수: " + str(movie_real_number_audience[movie_num - 1]) + "만 명")
        print_prediction_message(movie_real_number_audience[movie_num - 1], index_list)
    else:
        print("잘못된 입력입니다! 다시 입력해 주세요!\n")
        time.sleep(1)
        continue
    while True:
        print("\n다른 영화 예측: ""y""키",end='  ')
        print("프로그램 종료: ""n""키")
        key = input()
        if key == 'n' or key == 'N':
            print("프로그램이 종료됩니다.")
            time.sleep(2)
            exit()
        elif key == 'y' or key == 'Y':
            break
        else:
            print("잘못된 입력입니다! 다시 입력해 주세요!")
            time.sleep(1)