# 유가증권시장의 전 종목에 대한 거래량 급증 여부 체크
# 1. 유가증권시장 전 종목에 대한 코드 목록 생성
import time
import random
import win32com.client

# 2. 거래량 급증 체크 함수(CheckVolume) 구현
def CheckVolume(instStockChart, code):
    # SetInputValue
    instStockChart.SetInputValue(0, code)
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

    # Caclulate average volume
    averageVolume =  (sum(volumes) - volumes[0]) / (len(volumes) -1)

    if volumes[0] > averageVolume * 10:
        return 1
    else:
        return 0

if __name__ == "__main__":
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codeList = instCpCodeMgr.GetStockListByMarket(1)
    buyList = []
    for code in codeList:
        if CheckVolume(instStockChart, code) == 1:
            buyList.append(code)
            print(code)
            time.sleep(random.randint(1, 3))