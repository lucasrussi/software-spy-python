# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastro5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(370, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_subtitle = QtWidgets.QLabel(self.centralwidget)
        self.label_subtitle.setGeometry(QtCore.QRect(10, 50, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setObjectName("label_subtitle")
        self.label_subtitle2 = QtWidgets.QLabel(self.centralwidget)
        self.label_subtitle2.setGeometry(QtCore.QRect(10, 250, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_subtitle2.setFont(font)
        self.label_subtitle2.setObjectName("label_subtitle2")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 90, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_cpf = QtWidgets.QLabel(self.centralwidget)
        self.label_cpf.setGeometry(QtCore.QRect(410, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cpf.setFont(font)
        self.label_cpf.setObjectName("label_cpf")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(20, 150, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_cargo = QtWidgets.QLabel(self.centralwidget)
        self.label_cargo.setGeometry(QtCore.QRect(410, 150, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cargo.setFont(font)
        self.label_cargo.setObjectName("label_cargo")
        self.label_setor = QtWidgets.QLabel(self.centralwidget)
        self.label_setor.setGeometry(QtCore.QRect(20, 210, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_setor.setFont(font)
        self.label_setor.setObjectName("label_setor")
        self.label_app1 = QtWidgets.QLabel(self.centralwidget)
        self.label_app1.setGeometry(QtCore.QRect(20, 300, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app1.setFont(font)
        self.label_app1.setObjectName("label_app1")
        self.label_app4 = QtWidgets.QLabel(self.centralwidget)
        self.label_app4.setGeometry(QtCore.QRect(20, 420, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app4.setFont(font)
        self.label_app4.setObjectName("label_app4")
        self.label_app2 = QtWidgets.QLabel(self.centralwidget)
        self.label_app2.setGeometry(QtCore.QRect(20, 340, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app2.setFont(font)
        self.label_app2.setObjectName("label_app2")
        self.label_app5 = QtWidgets.QLabel(self.centralwidget)
        self.label_app5.setGeometry(QtCore.QRect(20, 460, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app5.setFont(font)
        self.label_app5.setObjectName("label_app5")
        self.label_app3 = QtWidgets.QLabel(self.centralwidget)
        self.label_app3.setGeometry(QtCore.QRect(20, 380, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app3.setFont(font)
        self.label_app3.setObjectName("label_app3")
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(70, 90, 331, 20))
        self.input_name.setObjectName("input_name")
        self.input_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cpf.setGeometry(QtCore.QRect(440, 90, 331, 20))
        self.input_cpf.setObjectName("input_cpf")
        self.input_cargo = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cargo.setGeometry(QtCore.QRect(450, 150, 331, 20))
        self.input_cargo.setObjectName("input_cargo")
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(70, 150, 331, 20))
        self.input_email.setObjectName("input_email")
        self.input_setor = QtWidgets.QLineEdit(self.centralwidget)
        self.input_setor.setGeometry(QtCore.QRect(70, 210, 331, 20))
        self.input_setor.setObjectName("input_setor")
        self.input_app1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_app1.setGeometry(QtCore.QRect(90, 300, 331, 20))
        self.input_app1.setObjectName("input_app1")
        self.input_app2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_app2.setGeometry(QtCore.QRect(90, 340, 331, 20))
        self.input_app2.setObjectName("input_app2")
        self.input_app3 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_app3.setGeometry(QtCore.QRect(90, 380, 331, 20))
        self.input_app3.setObjectName("input_app3")
        self.input_app4 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_app4.setGeometry(QtCore.QRect(90, 420, 331, 20))
        self.input_app4.setObjectName("input_app4")
        self.input_app5 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_app5.setGeometry(QtCore.QRect(90, 460, 331, 20))
        self.input_app5.setObjectName("input_app5")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(300, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(420, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ok.setFont(font)
        self.btn_ok.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.btn_ok.setObjectName("btn_ok")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro"))
        self.label_title.setText(_translate("MainWindow", "Cadastro"))
        self.label_subtitle.setText(_translate("MainWindow", "Dados do colaborador"))
        self.label_subtitle2.setText(_translate("MainWindow", "Aplicativos a serem monitorados"))
        self.label_name.setText(_translate("MainWindow", "Nome:"))
        self.label_cpf.setText(_translate("MainWindow", "CPF:"))
        self.label_email.setText(_translate("MainWindow", "E-mail:"))
        self.label_cargo.setText(_translate("MainWindow", "Cargo:"))
        self.label_setor.setText(_translate("MainWindow", "Setor:"))
        self.label_app1.setText(_translate("MainWindow", "Aplicativo 1:"))
        self.label_app4.setText(_translate("MainWindow", "Aplicativo 4:"))
        self.label_app2.setText(_translate("MainWindow", "Aplicativo 2:"))
        self.label_app5.setText(_translate("MainWindow", "Aplicativo 5:"))
        self.label_app3.setText(_translate("MainWindow", "Aplicativo 3:"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))
        self.btn_ok.setText(_translate("MainWindow", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_cadastro5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
