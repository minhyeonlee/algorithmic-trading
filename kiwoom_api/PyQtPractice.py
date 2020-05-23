# Kiwoom Open API+는 OCX(Object Linking and Embedding Custom Control) 방식을 사용
# PyQt 패키지의 QAxContainer 모듈을 통해 OCX 사용
import sys
from PyQt5.QtWidgets import *

# QMainWindow를 이용한 윈도우 생성
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()