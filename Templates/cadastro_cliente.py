# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_cliente.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastroCliente(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 461)
        Form.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(150, 400, 121, 41))
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
        self.btn_cadastro = QtWidgets.QPushButton(Form)
        self.btn_cadastro.setGeometry(QtCore.QRect(330, 400, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(62, 186, 0);\n"
"}")
        self.btn_cadastro.setObjectName("btn_cadastro")
        self.label_nome = QtWidgets.QLabel(Form)
        self.label_nome.setGeometry(QtCore.QRect(20, 70, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nome.setFont(font)
        self.label_nome.setTextFormat(QtCore.Qt.AutoText)
        self.label_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nome.setObjectName("label_nome")
        self.label_cargo = QtWidgets.QLabel(Form)
        self.label_cargo.setGeometry(QtCore.QRect(20, 350, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cargo.setFont(font)
        self.label_cargo.setTextFormat(QtCore.Qt.AutoText)
        self.label_cargo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cargo.setObjectName("label_cargo")
        self.label_email = QtWidgets.QLabel(Form)
        self.label_email.setGeometry(QtCore.QRect(20, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setTextFormat(QtCore.Qt.AutoText)
        self.label_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_email.setObjectName("label_email")
        self.label_setor = QtWidgets.QLabel(Form)
        self.label_setor.setGeometry(QtCore.QRect(20, 300, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_setor.setFont(font)
        self.label_setor.setTextFormat(QtCore.Qt.AutoText)
        self.label_setor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setor.setObjectName("label_setor")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(170, 20, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_titleEm = QtWidgets.QLabel(Form)
        self.label_titleEm.setGeometry(QtCore.QRect(150, 240, 310, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titleEm.setFont(font)
        self.label_titleEm.setTextFormat(QtCore.Qt.AutoText)
        self.label_titleEm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titleEm.setObjectName("label_titleEm")
        self.label_cpf = QtWidgets.QLabel(Form)
        self.label_cpf.setGeometry(QtCore.QRect(20, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cpf.setFont(font)
        self.label_cpf.setTextFormat(QtCore.Qt.AutoText)
        self.label_cpf.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpf.setObjectName("label_cpf")
        self.input_nome = QtWidgets.QLineEdit(Form)
        self.input_nome.setGeometry(QtCore.QRect(90, 70, 410, 20))
        self.input_nome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_nome.setObjectName("input_nome")
        self.input_cpf = QtWidgets.QLineEdit(Form)
        self.input_cpf.setGeometry(QtCore.QRect(90, 120, 410, 20))
        self.input_cpf.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_cpf.setObjectName("input_cpf")
        self.input_email = QtWidgets.QLineEdit(Form)
        self.input_email.setGeometry(QtCore.QRect(90, 170, 410, 20))
        self.input_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_email.setObjectName("input_email")
        self.input_setor = QtWidgets.QLineEdit(Form)
        self.input_setor.setGeometry(QtCore.QRect(90, 300, 410, 20))
        self.input_setor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_setor.setObjectName("input_setor")
        self.input_cargo = QtWidgets.QLineEdit(Form)
        self.input_cargo.setGeometry(QtCore.QRect(90, 350, 410, 20))
        self.input_cargo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_cargo.setObjectName("input_cargo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastro"))
        self.btn_cancel.setText(_translate("Form", "Cancelar"))
        self.btn_cadastro.setText(_translate("Form", "Cadastrar"))
        self.label_nome.setText(_translate("Form", "Nome:"))
        self.label_cargo.setText(_translate("Form", "Cargo:"))
        self.label_email.setText(_translate("Form", "E-mail:"))
        self.label_setor.setText(_translate("Form", "Setor:"))
        self.label_title.setText(_translate("Form", "Dados pessoais do colaborador"))
        self.label_titleEm.setText(_translate("Form", "Dados empresariais do colaborador"))
        self.label_cpf.setText(_translate("Form", "CPF:"))
        self.input_nome.setPlaceholderText(_translate("Form", "Insira o nome"))
        self.input_cpf.setPlaceholderText(_translate("Form", "Insira o CPF"))
        self.input_email.setPlaceholderText(_translate("Form", "Insira o e-mail"))
        self.input_setor.setPlaceholderText(_translate("Form", "Insira o setor"))
        self.input_cargo.setPlaceholderText(_translate("Form", "Insira o cargo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_cadastroCliente()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
