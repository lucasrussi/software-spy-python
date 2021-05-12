from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import re
import os
import sys
#banco de dados
from db.banco_adm import cadastroEmpresa
#software
from Templates.administracao_cadastro import Ui_cadastroClientes


class administracao_cliente(QMainWindow):
    def __init__(self, *args, **argvs):
        super(administracao_cliente, self).__init__(*args, **argvs)
        self.ui = Ui_cadastroClientes()
        self.ui.setupUi(self)
        self.ui.btn_cadastro.clicked.connect(self.cadastro)
        self.ui.btn_cancel.clicked.conenct(self.cancel)

        def cadastro(self):
            # captação dos valores da tela

            # variaveis dados empresa
            atividade = self.ui.line_atividade
            fantasia = self.ui.line_fantasia
            razaoSocial = self.ui.line_razao
            cnpj = self.ui.line_cnpj

            # variaveis localizacão empresa
            bairro = self.ui.line_bairro
            cep = self.ui.line_cep
            estadual = self.ui.line_estadual
            municipal = self.ui.line_municipal
            rua = self.ui.line_rua
            uf = self.ui.line_uf
            cidade = self.ui.line_cidade

            # variaveis comunicacão
            email = self.ui.line_email
            tel = self.ui.line_tel

            # variaveis contrato
            numTela = self.ui.line_ntela
            planos = self.ui.comboBox_planos.text()
            formapag = self.ui.comboBox_formpag.text()

            if (atividade == '' or fantasia == '' or razaoSocial == '' or cnpj == '' or bairro == '' 
                or cep == '' or estadual == '' or municipal == '' or rua == '' or uf == '' or cidade == ''
                or email == '' or tel == '' or numTela == '' or planos == '' or formapag == ''):

                QMessageBox.warning(QMessageBox(), "Dados invalidos","Preencha todos os campos.")
            else:
                cadastroEmpresa(atividade,fantasia,razaoSocial,cnpj,bairro,cep,estadual,municipal,rua,uf,cidade,email,tel,numTela,planos,formapag)
        def cancel(self):
            self.close()                  
