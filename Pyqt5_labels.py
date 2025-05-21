# PyQt5 QLabels


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mera phela GUI")
        self.setGeometry(400, 100, 700, 700)         # x, y, width, height

        label = QLabel("Assalamu alaikum", self)
        label.setFont(QFont("Ariel", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: red;"
                            "font-weight: bold;")
        
        # label.setAlignment(Qt.AlignTop)            # Vertically Top
        # label.setAlignment(Qt.AlignBottom)         # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter)        # Vertically Center 

        # label.setAlignment(Qt.AlignHCenter)/       # Horizontally Center            
        # label.setAlignment(Qt.AlignRight)          # Horizontally Right 
        # label.setAlignment(Qt.AlignLeft)           # Horizontally Left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)        # Center & Top
        # label.setAlignment(Qt.AlignTCenter | Qt.AlignBottom)     # Center & Bottom
        # label.setAlignment(Qt.AlignCenter)                       # Center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()