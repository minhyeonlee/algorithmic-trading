# 이동평균선: 기술적 분석지표의 한 종류로 일정 기간 동안의 주가를 산술 평균한 값인 주가이동평균을 차례로 연결해 만든 선
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
#print(gs.tail())

# 거래량이 없는 날짜 제외
new_gs = gs[gs['Volume'] != 0]

# 수정 종가에 대해 5일, 20일, 60일, 120일 주가 이동평균 계산
ma5 = new_gs['Adj Close'].rolling(window=5).mean()
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

# new_gs에 주가 이동평균 추가
new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)
print(new_gs.tail(5))

# 수정 종가 그래프 그리기
plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")

# 이동평균선 그래프 그리기
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

plt.legend(loc="best")
plt.grid()
plt.show()