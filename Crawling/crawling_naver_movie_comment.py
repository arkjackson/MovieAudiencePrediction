#영화 리뷰 크롤링 프로그램

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

#자신의 크롬버전에 맞는 chromedriver 설치하기
driver = webdriver.Chrome('./chromedriver')
#영화 평점 링크 넣어주기 ex) 비상선언
driver.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkEw&pkid=68&os=10105426&qvt=0&query=%EC%98%81%ED%99%94%20%EB%B9%84%EC%83%81%EC%84%A0%EC%96%B8%20%ED%8F%89%EC%A0%90')
#웹페이지 스크롤 내리기 (y축 방향으로 +600)
ActionChains(driver) \
        .scroll_by_amount(0, 600) \
        .perform()
#아래 코드 진행을 위해 잠시 딜레이시키기
time.sleep(2)
#스포일러 감상 보여주기 버튼 클릭
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/button").click()
#영화 리뷰에 대한 인덱스
comment_index = 1
while True:
    #관람객 코멘트 부분 찾기
    comment = driver.find_elements(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[6]/ul/li[' + str(comment_index) + ']/div[2]/div/span[2]')
    #관람객 별점 부분 찾기
    star_score = driver.find_elements(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div[6]/ul/li[' + str(comment_index) + ']/div[1]/div/div[2]')
    try:
        if len(comment) > 0:
            #print(len(comment))
            print("별점:", star_score[0].text[13:]) #별점 출력
            print("감상평:", comment[0].text)  #코멘트 출력
            comment_index += 1
    except:
        break   #크롤링 종료
    time.sleep(0.5)
    #스크롤 내리기 위해 영화 평점 창 부분으로 초점 이동
    scroll_origin = ScrollOrigin.from_viewport(140, 641)
    #스크롤 내리기
    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 150) \
        .perform()
exit()