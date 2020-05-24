# web에서 주식 데이터 가져오기
# pandas_datareader package, data module: 인터넷상에서 제공하는 다양한 데이터를 DataFrame으로 만들어 주는 기능 제공
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 5, 22)

samsung = web.DataReader('005930.KS', 'yahoo',start,end)
# print(samsung)

# DataFrame 객체 요약해서 보기
print(samsung.info())

# DataReader 함수 호출 시, 조회 기간을 입력하지 않으면 2010/1/1 부터 데이터 조회일까지의 데이터를 얻어온다.
samsung = web.DataReader('005930.KS', 'yahoo')

plt.plot(samsung.index, samsung['Adj Close'])
plt.show()
