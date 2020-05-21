# XASession 클래스를 이용한 서버연결, 로그인(Event 방식)
import win32com.client
import pythoncom

# 이벤트를 처리하기 위해 전용 클래스인 XASessionEventHandler
class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

# XASession 인스턴스 생성(DispatchWithEvents 함수 사용)
instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

id = "id"
passwd = "passwd"
cert_passwd = "cert_passwd"

# 접속할 서버의 기본 주소:'hts.ebestsec.co.kr', 모의투자: 'demo.ebestsec.co.kr'
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

# 이벤트가 발생할 때까지 대기
while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()

# 계좌 정보 확인
num_account = instXASession.GetAccountListCount()
for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print(account)

# 단일 데이터 조회(t1102 TR)
# 이벤트 처리용 클래스 구현
class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1
# XAQuery 인스턴스 생성
instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT1102)

# Res파일을 XAQuery 클래스의 인스턴스에 등록(요청하는 데이터나 작업을 TR 코드를 통해 구분)
instXAQueryT1102.ResFileName = "C:/eBEST/xingAPI/Res/t1102.res"

# 입력 데이터 설정(XAQuery 클래스의 메서드인 SetFieldData 메서드)
instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", "0", "078020")

# Request 메서드를 통해 서버에 요청
instXAQueryT1102.Request(0)

# 이벤트 대기
while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()

# 데이터 받기
name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0)
price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0)
print(name)
print(price)

# 반복 데이터 조회(t8430 TR)
# 이벤트 처리를 위한 클래스 등록
class XAQueryEventHandlerT8430:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8430.query_state = 1

# XAQuery 인스턴스 생성
instXAQueryT8430 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8430)

# XAQuery 인스턴스에 res 파일 등록
instXAQueryT8430.ResFileName = "C:/eBEST/xingAPI/Res/t8430.res"

# 입력 데이터 설정
instXAQueryT8430.SetFieldData("t8430InBlock", "gubun", 0, 1)

# 서버 요청 및 이벤트 대기
instXAQueryT8430.Request(0)
while XAQueryEventHandlerT8430.query_state == 0:
    pythoncom.PumpWaitingMessages()

# 가져올 데이터 개수 구하기
count = instXAQueryT8430.GetBlockCount("t8430OutBlock")

for i in range(5):
    hname = instXAQueryT8430.GetFieldData("t8430OutBlock", "hname", i)
    shcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "shcode", i)
    expcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "expcode", i)
    etfgubun = instXAQueryT8430.GetFieldData("t8430OutBlock", "etfgubun", i)
    print(i, hname, shcode, expcode, etfgubun)



