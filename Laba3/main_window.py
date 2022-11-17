from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget, QLabel
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import QCoreApplication, QSize, Qt
import sys
from PyQt6 import QtWidgets
from Laba2 import csv_file_first
from Laba2 import csv_file_second
from Laba2 import csv_file_third
from Laba2 import Iterator




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        btn_font_main = QFont('Impact', 20)
        btn_StyleSheet_main = 'background-color: #171982; color: 000000; border :1px solid;'

        # параметры окна
        self.setGeometry(50, 50, 1200, 675)
        self.setWindowTitle('Application programing laba 3')
        self.setFixedSize(self.size())
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setStyleSheet("background-image: url(./671076_main.jpg);")

        # Запрос пути
        self.folder_path_dataset = ""
        while self.folder_path_dataset == "":
            self.folder_path_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Стандартный csv")
        self.button1.setGeometry(150, 30, 300, 50)
        self.button1.setFixedWidth(300)
        self.button1.setFont(btn_font_main)
        self.button1.setStyleSheet(btn_StyleSheet_main)
        self.button1.clicked.connect(self.click_button_1)
        self.button1.clicked.connect(self.buttonClicked)
        self.button1.enterEvent = lambda event: self.button1.setStyleSheet(
            'background-color: #171982; color: #D2691E; border :1px solid; border-color: #D2691E;')
        self.button1.leaveEvent = lambda event: self.button1.setStyleSheet(
            'background-color: #171982; color: 000000; border :1px solid;')

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("Сsv c рандомными числами")
        self.button2.setGeometry(450, 30, 300, 50)
        self.button2.setFixedWidth(300)
        self.button2.setFont(btn_font_main)
        self.button2.setStyleSheet(btn_StyleSheet_main)
        self.button2.clicked.connect(self.click_button_2)
        self.button2.clicked.connect(self.buttonClicked)

        self.button2.enterEvent = lambda event: self.button2.setStyleSheet(
            'background-color: #171982; color: #D2691E; border :1px solid; border-color: #D2691E;')
        self.button2.leaveEvent = lambda event: self.button2.setStyleSheet(
            'background-color: #171982; color: 000000; border :1px solid;')

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText("Csv  'метка_номер'")
        self.button3.setGeometry(750, 30, 300, 50)
        self.button3.setFixedWidth(300)
        self.button3.setFont(btn_font_main)
        self.button3.setStyleSheet(btn_StyleSheet_main)
        self.button3.clicked.connect(self.click_button_3)
        self.button3.clicked.connect(self.buttonClicked)
        self.button3.enterEvent = lambda event: self.button3.setStyleSheet(
            'background-color: #171982; color: #D2691E; border :1px solid; border-color: #D2691E;')
        self.button3.leaveEvent = lambda event: self.button3.setStyleSheet(
            'background-color: #171982; color: 000000; border :1px solid;')

        self.btn_next_tiger = QtWidgets.QPushButton(self)
        self.btn_next_tiger.setText("Следующий тигр")
        self.btn_next_tiger.setGeometry(300, 580, 200, 40)
        self.btn_next_tiger.setFont(btn_font_main)
        self.btn_next_tiger.setStyleSheet(btn_StyleSheet_main)
        self.btn_next_tiger.clicked.connect(self.next_tiger)

        self.btn_next_leo = QtWidgets.QPushButton(self)
        self.btn_next_leo.setText("Следующий леопард")
        self.btn_next_leo.setGeometry(700, 580, 200, 40)
        self.btn_next_leo.setFont(btn_font_main)
        self.btn_next_leo.setStyleSheet(btn_StyleSheet_main)
        self.btn_next_leo.clicked.connect(self.next_leo)

        self.image_leo = QLabel(self)
        self.image_tiger = QLabel(self)
        self.tiger_iterator = Iterator.SimpleIterator('tiger', 'dataset_csv_first')
        self.leo_iterator = Iterator.SimpleIterator('leopard', 'dataset_csv_first')


    def click_button_1(self):
        csv_file_first.main()

    def click_button_2(self):
        csv_file_third.main()

    def click_button_3(self):
        csv_file_second.main()

    def buttonClicked(self):
        msg = 'Button was pressed'
        self.statusBar().showMessage(msg, 2000)
        self.statusBar().setStyleSheet("background-color: #171982; color: #000000;")

    def next_leo(self):
        self.image_leo.setPixmap(QPixmap(next(self.leo_iterator)))
        self.image_leo.setGeometry(620, 100, 400, 400)
        self.image_leo.show()

    def next_tiger(self):
        self.image_tiger.setPixmap(QPixmap(next(self.tiger_iterator)))
        self.image_tiger.setGeometry(160, 100, 400, 400)
        self.image_tiger.show()






app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
