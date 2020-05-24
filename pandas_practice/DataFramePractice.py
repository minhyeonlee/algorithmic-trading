# DataFrame(2차원 형태) 자료구조
from pandas import Series, DataFrame

raw_data = {'col0':[1, 2, 3, 4],
            'col1':[10, 20, 30, 40],
            'col2':[100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)
print(data['col1'])

# 주가 데이터 저장
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index = date)
print(daeshin_day)

# 객체 접근
close = daeshin_day['close']
print(close)

# 객체의 로우에 접근
day_data = daeshin_day.loc['16.02.24']
print(day_data)

# DataFrame 객체의 칼럼 이름과 인덱스 값 확인
print(daeshin_day.columns)
print(daeshin_day.index)