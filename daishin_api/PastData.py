# 최근 10일간 종가 데이터 구하기
# StockChart Class : Request/Reply 방식
import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# 어떤 데이터를 원하는지 알려준다(Data Type, Data Value)
# Data Type 0: 종목코드, 1: 요청구분, 4: 요청개수, 5: 필드 값(5는 종가), 6: 차트구분 9: 수정주가 반영여부
instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 10)
instStockChart.SetInputValue(5, 5)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# 데이터 처리 요청
instStockChart.BlockRequest()
numData = instStockChart.GetHeaderValue(3) # 수신한 데이터 개수 확인
for i in range(numData):
    print(instStockChart.GetDataValue(0, i))

print("=====================================")
# 일자별로 시가, 고가, 저가, 종가, 거래량 구하기
instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 10)
instStockChart.SetInputValue(5, (0,2,3,4,5,8))
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

instStockChart.BlockRequest()

# 반환된 데이터 개수 확인
numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)
print(numData, numField)

# 일자별 시가, 고가, 저가, 종가, 거래량 출력
for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print()