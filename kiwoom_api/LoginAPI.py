# GUI 기반의 프로그램을 작성하여 Open API+로 Login
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(500, 500, 500, 500)

        # 키움증권에서 제공하는 클래스를 사용하기 위해 ProgID를 QAxWidget 클래스의 생성자로 전달하여 인스턴스 생성
        self.kiwoom = QAxWidget("KHOPENAPI.KHOPenAPICtrl.1")

        btn1 = QPushButton("Login", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Check state", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")

    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()