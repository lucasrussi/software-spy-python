from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import string
from random import choice
import os
import sys
# Banco de dados
from db.banco_user import cadastra_db
from db.banco_user import povoa_db
from db.banco_user import login_username_db
# software
from Templates.cadastro_5 import Ui_cadastro5
from modulos.email import sendemail


class cadastro5(QMainWindow):
    def __init__(self, *args, **argvs):
        super(cadastro5, self).__init__(*args, **argvs)
        self.ui = Ui_cadastro5()
        self.ui.setupUi(self)
        self.ui.btn_ok.clicked.connect(self.cadastra)
        self.ui.btn_cancel.clicked.connect(self.cancel)

    def cadastra(self):
        nome = self.ui.input_name.text()
        cpf = self.ui.input_cpf.text()
        email = self.ui.input_email.text()
        cargo = self.ui.input_cargo.text()
        setor = self.ui.input_setor.text()
        app1 = self.ui.input_app1.text().lower()
        app2 = self.ui.input_app2.text().lower()
        app3 = self.ui.input_app3.text().lower()
        app4 = self.ui.input_app4.text().lower()
        app5 = self.ui.input_app5.text().lower()
        numeroDeCadastro = login_username_db()
        # condição de verificação do cadastro

        # condição dos dados pessoais, todos devem estar preenchidos
        if(nome == "" or cpf == "" or email == "" or cargo == "" or setor == ""):
            QMessageBox.warning(QMessageBox(), "Dados invalidos",
                                "Preencha todos os campos dos dados pessoais.")
        # condição dos dados das aplicações, devesse ter pelo menos 1 campo preenchido

        elif(app1 == "" and app2 == "" and app3 == "" and app4 == "" and app5 == ""):
            QMessageBox.warning(QMessageBox(), "Dados invalidos",
                                "Cadastre pelo menos uma aplicação.")
        elif(len(numeroDeCadastro) > 5): #numero de cadastros possiveis do plano
             QMessageBox.warning(QMessageBox(), "Limite de cadastro atingido",
                                "O limite de colaboradores cadastrados atingido.")
        else:
            #generetor passworld
            value = string.ascii_letters + string.digits
            passworld=''
            for i in range(10):
                passworld += choice(value)
            cadastra_db(cpf) #chama cadastro no banco de dados
            povoa_db(passworld,nome,cpf,email,cargo,setor,app1,app2,app3,app4,app5)
            sendemail(nome,cpf,passworld,email)
            QMessageBox.information(
                QMessageBox(), "Dados validos", "Cadastro concluido com sucesso.")
            self.close()
            


    def cancel(self):
        self.close()
