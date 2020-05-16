# 업종별 PER 분석을 통한 유망 종목 찾기
import win32com.client

# 업종별 코드 리스트
instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
industryCodeList = instCpCodeMgr.GetIndustryList()
# 업종명 구하기
for industryCode in industryCodeList:
    print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))

print("============================")
# GetGroupCodeList Method를 통해 '음식료품' 업종에 속하는 종목의 종목 코드 반환
targetCodeList = instCpCodeMgr.GetGroupCodeList(5)
for code in targetCodeList:
    print(code, instCpCodeMgr.CodeToName(code))

print("============================")
# CpSyDib Module의 MarketEye Class를 통한 PER 값 구하기 (Request/Reply)
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
# Get PER
instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, targetCodeList)

# Block Request
instMarketEye.BlockRequest()

# GetHeaderValue
numStock = instMarketEye.GetHeaderValue(2)

# GetData
sumPer = 0
for i in range(numStock):
    sumPer += instMarketEye.GetDataValue(0, i)

print("Average PER", sumPer / numStock)

