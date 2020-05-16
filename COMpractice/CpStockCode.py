# COM : Component Object Model
# 프로그래밍 언어와 상관없이 개발된 객체를 사용할 수 있게 해줌
# 대신증권에서 C/C++로 구현된 CpStockCode 클래스를 파이썬 코드로 구현해본다.
# 2:20
class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self, name):
        return self.stocks[name]

instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))

# 파이썬에서 다른 프로그래밍 언어로 작성된 COM 객체를 생성
# win32com.client모듈의 Dispatch 메서드를 사횽
import win32com.client
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
# Word 실행
word = win32com.client.Dispatch("Word.Application")
word.Visible = True