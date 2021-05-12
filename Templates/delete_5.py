# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 500)
        MainWindow.setMinimumSize(QtCore.QSize(590, 500))
        MainWindow.setMaximumSize(QtCore.QSize(590, 500))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 60, 181, 21))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(170, 10, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_colab = QtWidgets.QLabel(self.centralwidget)
        self.label_colab.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_colab.setObjectName("label_colab")
        self.label_cpf = QtWidgets.QLabel(self.centralwidget)
        self.label_cpf.setGeometry(QtCore.QRect(10, 110, 31, 16))
        self.label_cpf.setObjectName("label_cpf")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(250, 110, 41, 16))
        self.label_email.setObjectName("label_email")
        self.label_app1 = QtWidgets.QLabel(self.centralwidget)
        self.label_app1.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_app1.setObjectName("label_app1")
        self.label_cargo = QtWidgets.QLabel(self.centralwidget)
        self.label_cargo.setGeometry(QtCore.QRect(10, 160, 41, 16))
        self.label_cargo.setObjectName("label_cargo")
        self.label_setor = QtWidgets.QLabel(self.centralwidget)
        self.label_setor.setGeometry(QtCore.QRect(250, 160, 31, 16))
        self.label_setor.setObjectName("label_setor")
        self.label_app3 = QtWidgets.QLabel(self.centralwidget)
        self.label_app3.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.label_app3.setObjectName("label_app3")
        self.label_app2 = QtWidgets.QLabel(self.centralwidget)
        self.label_app2.setGeometry(QtCore.QRect(10, 250, 61, 16))
        self.label_app2.setObjectName("label_app2")
        self.label_app4 = QtWidgets.QLabel(self.centralwidget)
        self.label_app4.setGeometry(QtCore.QRect(10, 310, 61, 16))
        self.label_app4.setObjectName("label_app4")
        self.label_app5 = QtWidgets.QLabel(self.centralwidget)
        self.label_app5.setGeometry(QtCore.QRect(10, 340, 61, 16))
        self.label_app5.setObjectName("label_app5")
        self.output_cpf = QtWidgets.QLabel(self.centralwidget)
        self.output_cpf.setGeometry(QtCore.QRect(40, 110, 201, 16))
        self.output_cpf.setText("")
        self.output_cpf.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_cpf.setObjectName("output_cpf")
        self.output_cargo = QtWidgets.QLabel(self.centralwidget)
        self.output_cargo.setGeometry(QtCore.QRect(50, 160, 191, 20))
        self.output_cargo.setText("")
        self.output_cargo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_cargo.setObjectName("output_cargo")
        self.output_setor = QtWidgets.QLabel(self.centralwidget)
        self.output_setor.setGeometry(QtCore.QRect(290, 160, 191, 20))
        self.output_setor.setText("")
        self.output_setor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_setor.setObjectName("output_setor")
        self.output_app1 = QtWidgets.QLabel(self.centralwidget)
        self.output_app1.setGeometry(QtCore.QRect(80, 220, 201, 16))
        self.output_app1.setText("")
        self.output_app1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_app1.setObjectName("output_app1")
        self.output_app2 = QtWidgets.QLabel(self.centralwidget)
        self.output_app2.setGeometry(QtCore.QRect(80, 250, 201, 16))
        self.output_app2.setText("")
        self.output_app2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_app2.setObjectName("output_app2")
        self.output_app3 = QtWidgets.QLabel(self.centralwidget)
        self.output_app3.setGeometry(QtCore.QRect(80, 280, 201, 16))
        self.output_app3.setText("")
        self.output_app3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_app3.setObjectName("output_app3")
        self.output_app4 = QtWidgets.QLabel(self.centralwidget)
        self.output_app4.setGeometry(QtCore.QRect(80, 310, 201, 16))
        self.output_app4.setText("")
        self.output_app4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_app4.setObjectName("output_app4")
        self.output_app5 = QtWidgets.QLabel(self.centralwidget)
        self.output_app5.setGeometry(QtCore.QRect(80, 340, 201, 16))
        self.output_app5.setText("")
        self.output_app5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_app5.setObjectName("output_app5")
        self.output_email = QtWidgets.QLabel(self.centralwidget)
        self.output_email.setGeometry(QtCore.QRect(290, 110, 281, 20))
        self.output_email.setText("")
        self.output_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output_email.setObjectName("output_email")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(180, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(300, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.btn_delete.setObjectName("btn_delete")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deletar"))
        self.label_title.setText(_translate("MainWindow", "Deletar dados do Colaborador"))
        self.label_colab.setText(_translate("MainWindow", "Colaborador:"))
        self.label_cpf.setText(_translate("MainWindow", "CPF:"))
        self.label_email.setText(_translate("MainWindow", "E-mail:"))
        self.label_app1.setText(_translate("MainWindow", "Aplicativo 1:"))
        self.label_cargo.setText(_translate("MainWindow", "Cargo:"))
        self.label_setor.setText(_translate("MainWindow", "Setor:"))
        self.label_app3.setText(_translate("MainWindow", "Aplicativo 3:"))
        self.label_app2.setText(_translate("MainWindow", "Aplicativo 2:"))
        self.label_app4.setText(_translate("MainWindow", "Aplicativo 4:"))
        self.label_app5.setText(_translate("MainWindow", "Aplicativo 5:"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))
        self.btn_delete.setText(_translate("MainWindow", "Deletar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_delete5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
