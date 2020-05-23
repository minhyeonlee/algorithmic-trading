# 종목 코드 가져오기(GetCodeListByMarket), 종목 코드로부터 한글 종목명 구하기(GetMasterCodeName)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("KHOPENAPI.KHOPenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.setWindowTitle("종목 코드")
        self.setGeometry(1000, 1000, 1000, 1000)

        btn1 = QPushButton("종목 코드 얻기", self)
        btn1.setGeometry(10, 10, 200, 70)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 150, 400, 400)

    def btn1_clicked(self):
        # 유가증권시장의 종목 코드 목록 가져오기
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString", [x])
            kospi_code_name_list.append(x + " : " + name)

        self.listWidget.addItems(kospi_code_name_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())