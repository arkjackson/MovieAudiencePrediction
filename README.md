# MovieAudiencePrediction

### 💻 프로젝트 소개

구 네이버 영화 사이트 리뷰 데이터를 이용하여 관객수를 예측하는 프로그램입니다.

KoNLPy 한국어 처리 패키지의 [Okt(open-korean-text)](https://github.com/open-korean-text/open-korean-text)를 사용하였습니다.

Okt 사용 예시

    from konlpy.tag import Okt
    okt = Okt()
    print(okt.morphs("아버지가 방에 들어가신다."))
    ['아버지', '가', '방', '에', '들어가신다', '.']

1. 영화별 리뷰 데이터를 수집후 학습 데이터와 테스트 데이터로 분류

2. 형태소 분석 수행

3. 분석 결과를 활용하여 테스트 데이터에 대하여 관객수 예측 수행

### 🖱 프로그램 사용법

release에 포함된 .exe파일을 다운 받아 실행시켜 사용할 수 있습니다.

Ver - 0.3

아래의 화면이 나오면 정상적으로 프로그램이 열렸으며 안내 메시지에 따라 프로그램을 실행시킬 수 있습니다.

<img width="697" alt="화면 캡처 2023-06-18 141304" src="https://github.com/arkjackson/MovieAudiencePrediction/assets/111726392/42fe90f8-a792-4555-a5c6-907203b80e3f">

예측하고 싶은 영화의 번호를 입력하여 예측 결과 화면이 제공됩니다.

<img width="698" alt="화면 캡처 2023-06-18 141541" src="https://github.com/arkjackson/MovieAudiencePrediction/assets/111726392/70a32181-ac19-4674-8de7-037c3aeecb6d">
