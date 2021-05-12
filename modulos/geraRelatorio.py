from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from datetime import datetime
from Templates.geraRelatorio import Ui_geraRelatorio
from db.banco_user import geraRelatorioCombo
class geraRelatorio(QMainWindow):
    def __init__(self, *args, **argvs):
        super(geraRelatorio, self).__init__(*args, **argvs)
        self.ui = Ui_geraRelatorio()
        self.ui.setupUi(self)
        self.ui.btn_gerar.clicked.connect(self.gerar)
        #preenche e atualiza o comboBox do painel de gerenciamento
        comboName = geraRelatorioCombo() #pega o nome de todos os usuários
        for string in comboName: #começo do tratamento dos dados
            for i in range(0,len(comboName[0])):
                populateComboBox = string[i] #final do tratamento dos dados
                self.ui.comboBox_colaborador.addItem(populateComboBox) #linha que preenche
        
    def gerar(self):
        #Pegando o item do combox selecionado
        select_comboBox = self.ui.comboBox_colaborador.currentText()
        #Pegando os radios buttons
        if self.ui.radio_btnDiario.isChecked():
            radioButton = "diario"
            start_date =""
        elif self.ui.radio_btnSemanal.isChecked():
            radioButton = "semanal"
        elif self.ui.radio_btnQuinzenal.isChecked():
            radioButton = "quinzenal"
        elif self.ui.radio_btnMensal.isChecked():
            radioButton = "mensal"
        else:
            radioButton = ""

        #calendário
        start_date = ""
        end_date = ""
        start_date = self.ui.calendarWidget_inicial.selectedDate().toString("dd/MM/yyyy")
        end_date = self.ui.calendarWidget_final.selectedDate().toString("dd/MM/yyyy")
        print(f"Esse é o comboBox selecionado o nome: {select_comboBox}")
        print(f"Esse é o radio button selecionado: {radioButton}")
        print(f"Esse é o start_Date {start_date}")
        print(f"Esse é o end_date {end_date}")

        #estado de validação dos inputs preenchidos pelo usuario

        if end_date < start_date: #Data inicial maior que a data final
            QMessageBox.warning(QMessageBox(), "Dados inválidos",
                            "Data inicial maior que Data final")
            
        elif (start_date == end_date) and radioButton == "": #Quando todos os campos não estão selecionados
            QMessageBox.warning(QMessageBox(), "Dados inválidos",
                            "Preencha devidamente os campos, escolha entre data personalizada ou data pré definida")
        elif (start_date == end_date) and radioButton != "": #Quando a data pré definida está ativa
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(f"Irá ser gerado o relatório com o periodo: {radioButton}")
            msgBox.setWindowTitle("Relatório")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok: # Se a pessoa entra com o OK gera o relatório com os devidos tempos
                print(f"printou a mensagem com o periodo de {radioButton}")

        elif (start_date != end_date) and radioButton =="": #Quando a data personalizada é definida
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(f"Irá ser gerado o relatório com o periodo entre: {start_date} a {end_date}")
            msgBox.setWindowTitle("Relatório")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok: # Se a pessoa estra com OK o relatório é gerado
                print(f"Printou a mensagem com o periodo de {start_date}")

        elif (start_date != end_date ) and radioButton != "": #Quando a data pré definido e a data personalizada são escolhidos mutuamente
            QMessageBox.warning(QMessageBox(), "Dados inválidos",
                            "Escolha entre uma data personalizada ou pré definida")
            #Inicio do script para que os radio buttons sejam resetados
            self.group = QtWidgets.QButtonGroup()
            self.group.addButton(self.ui.radio_btnDiario)
            self.group.addButton(self.ui.radio_btnSemanal)
            self.group.addButton(self.ui.radio_btnQuinzenal)
            self.group.addButton(self.ui.radio_btnMensal)
            self.group.setExclusive(False)        
            self.ui.radio_btnDiario.setChecked(False)
            self.ui.radio_btnSemanal.setChecked(False)
            self.ui.radio_btnQuinzenal.setChecked(False)
            self.ui.radio_btnMensal.setChecked(False) 
            self.group.setExclusive(True)          
            #Final do script para que os radios buttons sejam resetados
            
        