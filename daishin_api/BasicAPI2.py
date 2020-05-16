# 종목 코드 가져오기
import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

# CpCodeMgr 클래스를 통해 종목명과 종목 코드 구하기
# GetStockListByMarket 메서드는 ETF(Exchange Traded Fund), ETN(Exchange Traded Note) 포함
kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name

# CVS(Comman Separated Values)로 저장
f = open('./kospi.csv', 'w')
for key, value in kospi.items():
    f.write("%s, %s\n" %(key, value))
f.close()

# 유가증권시장에 상장된 종목만 구하기(ETF, ETN 제외)
# CpCodeMgr Class의 GetStockSectionKind 메서드를 통해 구분 코드 반환
# GetStockSectionKind Method(CybosPlus help file 참고) 1: 주권, 10: ETF, 17: ETN

for i, code in enumerate(codeList):
    secondCode = instCpCodeMgr.GetStockSectionKind(code)
    name = instCpCodeMgr.CodeToName(code)
    print(i, code, secondCode, name)