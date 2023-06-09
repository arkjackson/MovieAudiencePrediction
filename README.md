# MovieAudiencePrediction

* MovieAudiencePrediction
    * [Introduction](#Introduction)
      * [Description](#Description)
      * [Train data of movie](#Train-data-of-movie)
      * [Test data of movie](#Test-data-of-movie)
    * [Requirements](#Requirements)
    * [How to use](#How-to-use)
    * [Release](#Release)
    * [Contacts](#Contacts)
    * [License](#License)

-----

## Introduction

구 네이버 영화 사이트 리뷰 데이터를 이용하여 관객수를 예측하는 프로그램입니다.

KoNLPy 한국어 처리 패키지의 [Okt(open-korean-text)](https://github.com/open-korean-text/open-korean-text)를 사용하였습니다.

### Example

    from konlpy.tag import Okt
    okt = Okt()
    print(okt.morphs("아버지가 방에 들어가신다."))
    ['아버지', '가', '방', '에', '들어가신다', '.']

### Description

1. 영화별 리뷰 데이터를 수집후 [학습 데이터](#학습-데이터-영화)와 [테스트 데이터](#테스트-데이터-영화)로 분류

2. 수집한 리뷰에 대하여 형태소 분석 수행

3. 분석 결과를 활용하여 테스트 데이터 영화에 대하여 관객수 예측 수행

#### Train data of movie

- 1987

- pmc: 더 벙커

- 강철비

- 겨울왕국2

- 공조

- 기생충

- 나우유씨미 마술사기단

- 담보

- 대호

- 더 배트맨

- 돈

- 럭키

- 마녀 Part2

- 미션임파서블 로그네이션

- 백두산

- 보스베이비

- 보헤미안 랩소디

- 샹치와 텐 링즈의 전설

- 신비한 동물사전

- 아쿠아맨

- 인질

- 인크레더블2

- 주토피아

- 청년경철

- 크루엘라

- 토이스토리4

- 트랜스포머 최후의 기사

- 형

- 히트맨

#### Test data of movie

- 소울

- 모가디슈

- 남산의 부장들

- 블랙위도우

- 닥터두리틀

- 외계인

- 탑건:메버릭

- 극한직업

## Requirements

pandas == 1.4.4

PyMySQL = 1.0.2

selenium == 4.10.0

konlpy == 0.6.0

## How to use

release에 포함된 .exe파일을 다운 받아 실행시켜 사용할 수 있습니다.

아래의 화면이 나오면 정상적으로 프로그램이 열렸으며 안내 메시지에 따라 프로그램을 실행시킬 수 있습니다.

<img width="697" alt="화면 캡처 2023-06-18 141304" src="https://github.com/arkjackson/MovieAudiencePrediction/assets/111726392/42fe90f8-a792-4555-a5c6-907203b80e3f">


예측하고 싶은 영화의 번호를 입력하면 예측 결과 화면이 제공됩니다.

<img width="713" alt="화면 캡처 2023-06-18 195340" src="https://github.com/arkjackson/MovieAudiencePrediction/assets/111726392/c9fef10d-249c-493b-a80c-4fa123138d22">

## Release

* [v0.4](https://github.com/arkjackson/MovieAudiencePrediction/releases/tag/v0.4)
    
    - 긍정 명사, 부정 명사를 바탕으로 관객수 예측

* [v0.3](https://github.com/arkjackson/MovieAudiencePrediction/releases/tag/v0.3)

    - 명사, 동사, 형용사 총 합의 평균값으로 관객수 예측

* [v0.2](https://github.com/arkjackson/MovieAudiencePrediction/releases/tag/v0.2)

    - 테스트 데이터 영화 3개 추가

* [v0.1](https://github.com/arkjackson/MovieAudiencePrediction/releases/tag/0.1)
    
    - 초기 모델 릴리즈

## Contacts

MovieAudiencePrediction 관련 이슈는 [이곳](https://github.com/arkjackson/MovieAudiencePrediction/issues)에 등록해주시기 바랍니다.

## License

라이센스가 필요시 기입
