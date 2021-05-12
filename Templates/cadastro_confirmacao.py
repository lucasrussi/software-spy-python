# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_confirmacao.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastroConfirmacao(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 305)
        Form.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_confirm = QtWidgets.QPushButton(Form)
        self.btn_confirm.setGeometry(QtCore.QRect(270, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(62, 186, 0);\n"
"}")
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(130, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(189, 0, 0);\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 171, 21))
        self.label_title.setObjectName("label_title")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(20, 50, 61, 16))
        self.label_name.setObjectName("label_name")
        self.label_cpf = QtWidgets.QLabel(Form)
        self.label_cpf.setGeometry(QtCore.QRect(20, 70, 31, 16))
        self.label_cpf.setObjectName("label_cpf")
        self.label_cargo = QtWidgets.QLabel(Form)
        self.label_cargo.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.label_cargo.setObjectName("label_cargo")
        self.label_setor = QtWidgets.QLabel(Form)
        self.label_setor.setGeometry(QtCore.QRect(20, 110, 61, 16))
        self.label_setor.setObjectName("label_setor")
        self.label_email = QtWidgets.QLabel(Form)
        self.label_email.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_email.setObjectName("label_email")
        self.output_name = QtWidgets.QLabel(Form)
        self.output_name.setGeometry(QtCore.QRect(60, 50, 471, 21))
        self.output_name.setText("")
        self.output_name.setObjectName("output_name")
        self.output_cpf = QtWidgets.QLabel(Form)
        self.output_cpf.setGeometry(QtCore.QRect(60, 70, 471, 21))
        self.output_cpf.setText("")
        self.output_cpf.setObjectName("output_cpf")
        self.output_email = QtWidgets.QLabel(Form)
        self.output_email.setGeometry(QtCore.QRect(60, 90, 471, 21))
        self.output_email.setText("")
        self.output_email.setObjectName("output_email")
        self.output_setor = QtWidgets.QLabel(Form)
        self.output_setor.setGeometry(QtCore.QRect(60, 110, 471, 21))
        self.output_setor.setText("")
        self.output_setor.setObjectName("output_setor")
        self.output_cargo = QtWidgets.QLabel(Form)
        self.output_cargo.setGeometry(QtCore.QRect(60, 130, 471, 21))
        self.output_cargo.setText("")
        self.output_cargo.setObjectName("output_cargo")
        self.title2 = QtWidgets.QLabel(Form)
        self.title2.setGeometry(QtCore.QRect(20, 190, 491, 16))
        self.title2.setObjectName("title2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Confirmação"))
        self.btn_confirm.setText(_translate("Form", "Sim"))
        self.btn_cancel.setText(_translate("Form", "Não"))
        self.label_title.setText(_translate("Form", "Os dados a seguir estão corretos?"))
        self.label_name.setText(_translate("Form", "Nome:"))
        self.label_cpf.setText(_translate("Form", "CPF:"))
        self.label_cargo.setText(_translate("Form", "Cargo:"))
        self.label_setor.setText(_translate("Form", "Setor:"))
        self.label_email.setText(_translate("Form", "E-mail:"))
        self.title2.setText(_translate("Form", "Se todos os dados estiverem corretos clique em SIM, caso tenha alguma divergência clique em NÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_cadastroConfirmacao()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
