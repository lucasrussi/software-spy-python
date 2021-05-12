# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administracao.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_administracao(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 610)
        MainWindow.setMinimumSize(QtCore.QSize(980, 610))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 610))
        MainWindow.setStyleSheet("background-color: rgb(225, 225, 225)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(155, 10, 1130, 580))
        self.tableWidget.setMinimumSize(QtCore.QSize(812, 580))
        self.tableWidget.setMaximumSize(QtCore.QSize(1130, 580))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.btn_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastro.setGeometry(QtCore.QRect(10, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setStyleSheet("QPushButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 182, 182);\n"
"}")
        self.btn_cadastro.setObjectName("btn_cadastro")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(10, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("QPushButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 182, 182);\n"
"}")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_gerar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gerar.setGeometry(QtCore.QRect(10, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 182, 182);\n"
"}")
        self.btn_gerar.setObjectName("btn_gerar")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(10, 330, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setStyleSheet("QPushButton{\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(182, 182, 182);\n"
"}")
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(10, 510, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(10, 0, 141, 131))
        self.label_logo.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../../../../Downloads/logoM&C (1).png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M&C - Admistração"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Empresa"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CNPJ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Plano"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Plano de pagamento"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status de pagamento"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Quantidade de telas"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cidade"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Estado"))
        self.btn_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.btn_delete.setText(_translate("MainWindow", "Deletar"))
        self.btn_gerar.setText(_translate("MainWindow", "Gerar Relatório"))
        self.btn_refresh.setText(_translate("MainWindow", "Recarregar"))
        self.btn_exit.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_administracao()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
