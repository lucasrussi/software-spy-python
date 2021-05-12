# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geraRelatorio.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_geraRelatorio(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(580, 560)
        mainWindow.setMinimumSize(QtCore.QSize(0, 0))
        mainWindow.setMaximumSize(QtCore.QSize(580, 560))
        font = QtGui.QFont()
        font.setPointSize(12)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox_colaborador = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_colaborador.setGeometry(QtCore.QRect(130, 70, 121, 22))
        self.comboBox_colaborador.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_colaborador.setObjectName("comboBox_colaborador")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.calendarWidget_inicial = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_inicial.setGeometry(QtCore.QRect(10, 280, 271, 191))
        self.calendarWidget_inicial.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget_inicial.setObjectName("calendarWidget_inicial")
        self.calendarWidget_final = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_final.setGeometry(QtCore.QRect(300, 280, 271, 191))
        self.calendarWidget_final.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.calendarWidget_final.setObjectName("calendarWidget_final")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.radio_btnDiario = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_btnDiario.setGeometry(QtCore.QRect(40, 160, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btnDiario.setFont(font)
        self.radio_btnDiario.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_btnDiario.setObjectName("radio_btnDiario")
        self.radio_btnSemanal = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_btnSemanal.setGeometry(QtCore.QRect(170, 160, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btnSemanal.setFont(font)
        self.radio_btnSemanal.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_btnSemanal.setObjectName("radio_btnSemanal")
        self.radio_btnQuinzenal = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_btnQuinzenal.setGeometry(QtCore.QRect(310, 160, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btnQuinzenal.setFont(font)
        self.radio_btnQuinzenal.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_btnQuinzenal.setObjectName("radio_btnQuinzenal")
        self.radio_btnMensal = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_btnMensal.setGeometry(QtCore.QRect(470, 160, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_btnMensal.setFont(font)
        self.radio_btnMensal.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_btnMensal.setObjectName("radio_btnMensal")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 220, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(190, 500, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_gerar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gerar.setGeometry(QtCore.QRect(300, 500, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 0);\n"
"}")
        self.btn_gerar.setObjectName("btn_gerar")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Relatorio"))
        self.label.setText(_translate("mainWindow", "Gerador de Relatório"))
        self.label_2.setText(_translate("mainWindow", "Colaboradores"))
        self.label_5.setText(_translate("mainWindow", "Periodo"))
        self.label_6.setText(_translate("mainWindow", "Data inicial"))
        self.label_7.setText(_translate("mainWindow", "Data final"))
        self.radio_btnDiario.setText(_translate("mainWindow", "Diário"))
        self.radio_btnSemanal.setText(_translate("mainWindow", "Semanal"))
        self.radio_btnQuinzenal.setText(_translate("mainWindow", "Quinzenal"))
        self.radio_btnMensal.setText(_translate("mainWindow", "Mensal"))
        self.label_8.setText(_translate("mainWindow", "Personalizado"))
        self.btn_exit.setText(_translate("mainWindow", "Sair"))
        self.btn_gerar.setText(_translate("mainWindow", "Gerar Relatório"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_geraRelatorio()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
