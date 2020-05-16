# CybosPlus Help File: http://cybosplus.github.io/

import win32com.client

# CybosPlus 연결 상태 확인
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)

print("==============================")
# 주식 코드 조회
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(instCpStockCode.GetCount()) # 종목 개수
print(instCpStockCode.GetData(0,0)) # 종목 코드
print(instCpStockCode.GetData(1,0)) # 종목 이름

print("==============================")
for i in range(0, 10):
    print(instCpStockCode.GetData(1,i))

print("==============================")
# 특정 종목을 찾아 종목 코드 출력
# for문으로 찾기
stockNum = instCpStockCode.GetCount()

for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0, i), end=" ")
        print(instCpStockCode.GetData(1,i))

print("==============================")
# NameToCode, CodeToIndex 메서드 사용
naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode, naverIndex)