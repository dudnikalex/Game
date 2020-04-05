import sys
from Unit import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 617)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 821, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 150, 141, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 320, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.hide()

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(80, 20, 681, 211))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(100, 260, 67, 17))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 280, 113, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(640, 280, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Паладин")
        self.comboBox.addItem("Жрец")
        self.comboBox.addItem("Чернокнижник")


        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(640, 260, 67, 17))
        self.label_3.setObjectName("label_3")

        self.dateEdit = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(370, 380, 110, 26))
        self.dateEdit.setObjectName("dateEdit")

        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(210, 340, 451, 31))
        self.label_4.setObjectName("label_4")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 470, 131, 21))
        self.pushButton_3.setObjectName("pushButton_3")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.hide()

        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(100, 50, 631, 141))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(100, 260, 67, 17))
        self.label_6.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(380, 260, 67, 17))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(650, 260, 67, 17))
        self.label_9.setObjectName("label_9")

        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(100, 280, 48, 26))
        self.spinBox.setObjectName("spinBox")

        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_2.setGeometry(QtCore.QRect(370, 280, 48, 26))
        self.spinBox_2.setObjectName("spinBox_2")

        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_3.setGeometry(QtCore.QRect(650, 280, 48, 26))
        self.spinBox_3.setObjectName("spinBox_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 410, 131, 25))
        self.pushButton_4.setObjectName("pushButton_4")

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 841, 571))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.hide()

        self.listwidget = QtWidgets.QListWidget(self.frame_4)
        self.listwidget.setGeometry(QtCore.QRect(80, 40, 691, 481))
        self.listwidget.setObjectName("listView")
        

        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(350, 10, 141, 31))
        self.label_7.setObjectName("label_7")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Heroes (Game)"))
        self.pushButton.setText(_translate("MainWindow", "Начать игру"))
        self.pushButton_2.setText(_translate("MainWindow", "Где здесь выход"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Приветствую тебя, путник</p><p align=\"center\"><br/><br/></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Тебе выпала честь стать героем, поэтому давай выбирай класс</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Твое имя"))
        self.label_3.setText(_translate("MainWindow", "Класс"))
        self.label_4.setText(_translate("MainWindow", "Ну и дату рождения, чтобы составить ваш гороскоп на сегодня"))
        self.pushButton_3.setText(_translate("MainWindow", "Создать героя"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Так, персонажа создали.</p><p align=\"center\">Теперь самое время набрать свою команду</p><p align=\"center\"><br/></p><p align=\"center\">Ты можешь выбрать до пяти персонажей, юниты не могут быть одного типа</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Воины"))
        self.label_8.setText(_translate("MainWindow", "Маги"))
        self.label_9.setText(_translate("MainWindow", "Лучники"))
        self.pushButton_4.setText(_translate("MainWindow", "Создать команду"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\"> Твоя команда</span></p></body></html>"))
        self.pushButton.clicked.connect(self.func)
        self.pushButton_3.clicked.connect(self.func1)
        self.pushButton_4.clicked.connect(self.func2)
        self.pushButton_2.clicked.connect(sys.exit)

    def func(self):
        #changing frames
        self.frame.hide()
        self.frame_2.show()

    def func1(self):
        #getting info from form
        self.textbox_val = self.lineEdit.text()
        self.combobox_val = self.comboBox.currentText()

        #changing frames
        self.frame_2.hide()
        self.frame_3.show()    

    #generating team
    def generate_team(self):
        self.a = []

        for i in range(self.num_of_wars):
            self.a.append(Generator.gen_war())
        
        for i in range(self.num_of_mages):
            self.a.append(Generator.gen_mage())

        for i in range(self.num_of_archers):
            self.a.append(Generator.gen_arch())
        
        

    def func2(self):
        #getting data and generating team

        self.num_of_wars = self.spinBox.value()
        self.num_of_mages = self.spinBox_2.value()
        self.num_of_archers = self.spinBox_3.value()

        summary = self.num_of_wars + self.num_of_archers + self.num_of_mages

        self.generate_team()

        for i in self.a:
            self.listwidget.addItem(i.to_string())

        if summary <= 5:
            #changing frames
            self.frame_3.hide()
            self.frame_4.show()    


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
