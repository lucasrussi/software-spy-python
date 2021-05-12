from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from db.banco_user import geraRelatorioCombo
from db.banco_user import delete_db
from Templates.deletar import Ui_delete

class delete(QMainWindow):
    def __init__(self, *args, **argvs):
        super(delete, self).__init__(*args, **argvs)
        self.ui = Ui_delete()
        self.ui.setupUi(self)
        self.ui.pushButton_cancelar.clicked.connect(self.cancel)
        self.ui.pushButton_deletar.clicked.connect(self.deletar)
        #preenche e atualiza o comboBox do painel de gerenciamento
        comboName = geraRelatorioCombo() #pega o nome de todos os usuários
        for string in comboName: #começo do tratamento dos dados
            for i in range(0,len(comboName[0])):
                populateComboBox = string[i] #final do tratamento dos dados
                self.ui.comboBox_user.addItem(populateComboBox) #linha que preenche
    def cancel(self):
        self.close()
    def deletar(self):
        select_comboBox = self.ui.comboBox_user.currentText()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(f"Irá ser deletado o usuário {select_comboBox}")
        msgBox.setWindowTitle("Deletar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok: # Se a pessoa estra com OK 
            delete_db(select_comboBox)
            self.close()

        
        
