# radio button

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mera phela GUI")
        self.setGeometry(400, 100, 700, 700)         # x, y, width, height
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Rupay", self)
        self.radio4 = QRadioButton("In Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_grp1 = QButtonGroup(self)
        self.button_grp2 = QButtonGroup(self)
        self.initUI()


    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{" 
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px"
                            "}")
        

        self.button_grp1.addButton(self.radio1)
        self.button_grp1.addButton(self.radio2)
        self.button_grp1.addButton(self.radio3)
        self.button_grp2.addButton(self.radio4)
        self.button_grp2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_ch)
        self.radio2.toggled.connect(self.radio_button_ch)
        self.radio3.toggled.connect(self.radio_button_ch)
        self.radio4.toggled.connect(self.radio_button_ch)
        self.radio5.toggled.connect(self.radio_button_ch)



    def radio_button_ch(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"You Selected {radio_button.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

