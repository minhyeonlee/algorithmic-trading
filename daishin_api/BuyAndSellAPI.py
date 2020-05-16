# 대신증권 모의투자 매수/매도 API
# CpTrade Module의 CpTdUtill 클래스(TradeInit Method)를 사용하여 주문 객체 초기화
# CpTrade Module의 CpTd0311 Class 사용(Request/Reply 통신 방식, GetDataValue 사용 불가)
# 매수/매도 주문에 대한 체결 내역은 CpDib Module의 CpConclusion Class를 통해 구한다.
import win32com.client

instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
instCpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")

# instCpTdUtil 객체 초기화
instCpTdUtil.TradeInit()

# 대신증권 종목 10주를 13,000원에 매수
accountNumber = instCpTdUtil.AccountNumber[0]
instCpTd0311.SetInputValue(0, 2) # 주문 종류 코드(매수)
instCpTd0311.SetInputValue(1, accountNumber) # 계좌 번호 설정
instCpTd0311.SetInputValue(3, 'A003540') # 주문할 종목 코드 설정
instCpTd0311.SetInputValue(4, 10) # 주문 수량 설정
instCpTd0311.SetInputValue(5, 13000) # 주문 단가 설정

# BlockRequest
instCpTd0311.BlockRequest()

