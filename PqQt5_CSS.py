# radio button

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mera phela GUI")
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
               QPushButton{
                        font-size: 40px;
                        font-family Ariel;
                        padding: 15px 50px;
                        margin: 25px;
                        border-radius: 15px;
                        border: 3px solid;
                    
                    
                        }
                           QPushButton#button1{
                                background-color: red;
                           }
                            QPushButton#button2{
                                background-color: blue;
                           }
                           QPushButton#button3{
                                background-color: green;
                           } 
                           QPushButton#button1:hover{
                                background-color: yellow;
                           }
                            QPushButton#button2:hover{
                                background-color: pink;
                           }
                           QPushButton#button3:hover{
                                background-color: grey;
                           }              
                           
                           """)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

