# pandas의 Series(1차원) 자료구조
from pandas import Series, DataFrame

# Series 객체 생성: Series 객체에 데이터가 저장되며, 저장된 데이터는 0부터 순서대로 인덱신된다.
kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

# Series 객체에 인덱싱 값 지정
kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)

for date in kakao2.index:
    print(date)

for ending_price in kakao2.values:
    print(ending_price)

# 주식 보유 현황
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
allStocks = mine + friend
print(allStocks)