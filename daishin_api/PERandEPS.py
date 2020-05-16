# PER(Price Earning Ratio): 주가 이익 비율으로 주가를 주당순이익(EPS)으로 나눈 값
# MarketEye Class: Request/Reply 방식
import win32com.client
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

# 현재가, PER, EPS, 최근분기년월 데이터 요청
instMarketEye.SetInputValue(0, (4, 67, 70, 111))
instMarketEye.SetInputValue(1, 'A003540')

# BlockRequest
instMarketEye.BlockRequest()

# GetData
print("현재가:", instMarketEye.GetDataValue(0,0))
print("PER:", instMarketEye.GetDataValue(1,0))
print("EPS:", instMarketEye.GetDataValue(2,0))
print("최근분기년월:", instMarketEye.GetDataValue(3,0))