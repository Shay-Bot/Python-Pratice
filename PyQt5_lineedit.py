# radio button

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mera phela GUI")
        self.setGeometry(400, 100, 700, 700)         # x, y, width, height
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()


    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        
        self.button.clicked.connect(self.submit)
        
    def submit(self):
        print("You Clicked button")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

