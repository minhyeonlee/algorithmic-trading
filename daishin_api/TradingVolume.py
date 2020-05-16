# 거래량 분석
# 1) 대량 거래(거래량이 1,000% 이상 급증) 종목
# 2) 대량 거래 시점에서 PBR(Price to Book Ratio)이 4보다 작아야 함
import win32com.client

instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# 한 종목에 대한 거래량 분석
# SetInputValue
instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 60)
instStockChart.SetInputValue(5, 8)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetData
volumes = []
numData = instStockChart.GetHeaderValue(3)
for i in range(numData):
    volume = instStockChart.GetDataValue(0, i)
    volumes.append(volume)
print(volumes)

# volumens[0] : 최근 거래일의 거래량
# Calculate average volume
averageVolume =  (sum(volumes) - volumes[0]) / (len(volumes) -1)
print(averageVolume)

# 평균 거래량을 최근 거래일의 거래량과 비교
if volumes[0] > averageVolume * 10:
    print("대박 주")
else:
    print("일반 주", volumes[0]/averageVolume)
