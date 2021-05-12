# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(591, 713)
        mainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imagen_logo = QtWidgets.QFrame(self.centralwidget)
        self.imagen_logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.imagen_logo.setStyleSheet("\n"
"background-position:center;\n"
"background-repeat:none;\n"
"background-color: rgb(0, 0, 0);")
        self.imagen_logo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.imagen_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imagen_logo.setLineWidth(0)
        self.imagen_logo.setObjectName("imagen_logo")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.imagen_logo)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.imagen_logo)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("LogoMC.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.imagen_logo)
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.top_bar)
        self.conteiner = QtWidgets.QFrame(self.centralwidget)
        self.conteiner.setBaseSize(QtCore.QSize(560, 530))
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.conteiner.setFont(font)
        self.conteiner.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.conteiner.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner.setObjectName("conteiner")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteiner)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.conteiner)
        self.login_area.setMaximumSize(QtCore.QSize(450, 16777215))
        self.login_area.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"\n"
"\n"
"")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_area.setLineWidth(0)
        self.login_area.setObjectName("login_area")
        self.user_input = QtWidgets.QLineEdit(self.login_area)
        self.user_input.setGeometry(QtCore.QRect(80, 100, 301, 41))
        self.user_input.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    border:2px solid rgb(0,0,255);\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(0, 0, 255);\n"
"}")
        self.user_input.setObjectName("user_input")
        self.pass_input = QtWidgets.QLineEdit(self.login_area)
        self.pass_input.setGeometry(QtCore.QRect(80, 240, 301, 41))
        self.pass_input.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"    border:2px solid rgb(0,0,255);\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(0, 0, 255);\n"
"}")
        self.pass_input.setText("")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pass_input.setClearButtonEnabled(True)
        self.pass_input.setObjectName("pass_input")
        self.label_user = QtWidgets.QLabel(self.login_area)
        self.label_user.setGeometry(QtCore.QRect(110, 70, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setObjectName("label_user")
        self.label_2 = QtWidgets.QLabel(self.login_area)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.button_enter = QtWidgets.QPushButton(self.login_area)
        self.button_enter.setGeometry(QtCore.QRect(100, 360, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_enter.setFont(font)
        self.button_enter.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color:rgb(0, 126, 0);\n"
"\n"
"}")
        self.button_enter.setObjectName("button_enter")
        self.button_exit = QtWidgets.QPushButton(self.login_area)
        self.button_exit.setGeometry(QtCore.QRect(260, 370, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(212, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.button_exit.setObjectName("button_exit")
        self.pushButton_3 = QtWidgets.QPushButton(self.login_area)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 450, 201, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(223, 223, 0);\n"
"\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_error = QtWidgets.QFrame(self.login_area)
        self.frame_error.setGeometry(QtCore.QRect(0, 310, 450, 30))
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius:10px;\n"
"")
        self.frame_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.conteiner)
        self.botton = QtWidgets.QFrame(self.centralwidget)
        self.botton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.botton.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.botton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botton.setObjectName("botton")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.botton)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_botton = QtWidgets.QLabel(self.botton)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_botton.setFont(font)
        self.label_botton.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_botton.setAlignment(QtCore.Qt.AlignCenter)
        self.label_botton.setObjectName("label_botton")
        self.verticalLayout_2.addWidget(self.label_botton)
        self.verticalLayout.addWidget(self.botton)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Office Prime"))
        self.user_input.setPlaceholderText(_translate("mainWindow", "Usuário"))
        self.pass_input.setPlaceholderText(_translate("mainWindow", "Senha"))
        self.label_user.setText(_translate("mainWindow", "Usuário"))
        self.label_2.setText(_translate("mainWindow", "Senha"))
        self.button_enter.setText(_translate("mainWindow", "Entrar"))
        self.button_exit.setText(_translate("mainWindow", "Sair"))
        self.pushButton_3.setText(_translate("mainWindow", "Suporte de Atendimento"))
        self.label_botton.setText(_translate("mainWindow", "Office Prime made by Coderpro - All right reserved - 2021     Alfa version: 1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
