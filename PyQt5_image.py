# blank box interface


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mera phela GUI")
        self.setGeometry(400, 100, 900, 700)         # x, y, width, height

        label = QLabel(self)
        label.setGeometry(0, 0, 900, 700)

        pixmap = QPixmap("C:/Users/laksh/OneDrive/Desktop/Python/projects/imagee.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()