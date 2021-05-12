# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_delete(object):
    def setupUi(self, delete_2):
        delete_2.setObjectName("delete_2")
        delete_2.setWindowModality(QtCore.Qt.NonModal)
        delete_2.resize(400, 480)
        delete_2.setMinimumSize(QtCore.QSize(400, 300))
        delete_2.setMaximumSize(QtCore.QSize(640, 480))
        delete_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.comboBox_user = QtWidgets.QComboBox(delete_2)
        self.comboBox_user.setGeometry(QtCore.QRect(130, 190, 171, 22))
        self.comboBox_user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_user.setObjectName("comboBox_user")
        self.label = QtWidgets.QLabel(delete_2)
        self.label.setGeometry(QtCore.QRect(60, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_cancelar = QtWidgets.QPushButton(delete_2)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(70, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cancelar.setFont(font)
        self.pushButton_cancelar.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.pushButton_deletar = QtWidgets.QPushButton(delete_2)
        self.pushButton_deletar.setGeometry(QtCore.QRect(220, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_deletar.setFont(font)
        self.pushButton_deletar.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_deletar.setObjectName("pushButton_deletar")
        self.label_2 = QtWidgets.QLabel(delete_2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(delete_2)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(delete_2)
        QtCore.QMetaObject.connectSlotsByName(delete_2)

    def retranslateUi(self, delete_2):
        _translate = QtCore.QCoreApplication.translate
        delete_2.setWindowTitle(_translate("delete_2", "Office Prime - Delete"))
        self.label.setText(_translate("delete_2", "Usuário:"))
        self.pushButton_cancelar.setText(_translate("delete_2", "Cancelar"))
        self.pushButton_deletar.setText(_translate("delete_2", "Deletar"))
        self.label_2.setText(_translate("delete_2", "Deletar usuário"))
        self.label_3.setText(_translate("delete_2", "Selecione o usuário que deseje deletar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_2 = QtWidgets.QWidget()
    ui = Ui_delete()
    ui.setupUi(delete_2)
    delete_2.show()
    sys.exit(app.exec_())
