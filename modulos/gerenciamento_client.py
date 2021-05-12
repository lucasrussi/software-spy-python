from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.QtPrintSupport import *
import os
import io
import sys
import time

#modulos de gráficos dashboard
#modulos diario
from modulos.grafico import grafico_pizza
from modulos.grafico import grafico_pizza1
from modulos.grafico import grafico_pizza2
from modulos.grafico import grafico_pizza3
from modulos.grafico import grafico_pizza4
#modulos semanal
from modulos.grafico import grafico_periodoSemanal1
from modulos.grafico import grafico_periodoSemanal2
from modulos.grafico import grafico_periodoSemanal3
from modulos.grafico import grafico_periodoSemanal4
from modulos.grafico import grafico_periodoSemanal5

from db.banco_user import preencheDash
from Templates.gerenciamento_cliente import Ui_gerenciamentoCliente
from modulos.cadastro import cadastro5
from db.banco_user import login_username_db
from db.banco_user import load_db
from db.banco_user import delete_db
from modulos.delete import delete


class gerenciamento_client(QMainWindow):
    def __init__(self, *args, **argvs):
        super(gerenciamento_client, self).__init__(*args, **argvs)
        self.ui = Ui_gerenciamentoCliente()
        self.ui.setupUi(self)
        # funcionalidade dos botões
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.btn_delet.clicked.connect(self.delete)
        self.ui.btn_exit.clicked.connect(self.exit)
        
        #Mensagem de quantidade de cadastro disponiveis
        numeroDeCadastro = login_username_db()
        uso = len(numeroDeCadastro)
        disponivel = 5 - uso
        usoString = str(uso)
        disponivelString = str(disponivel)
        self.ui.label_disponivel.setText(disponivelString)
        self.ui.label_used.setText(usoString)
        
        #Função para preenchimento da tela com os gráficos para 5 clientes
        grafico1 = grafico_pizza()
        grafico2 = grafico_pizza1()
        grafico3 = grafico_pizza2()
        grafico4 = grafico_pizza3()
        grafico5 = grafico_pizza4()
        #grafico_mediaMensal = grafico_periodo()
        grafico_mediaSemanal = grafico_periodoSemanal1()
        grafico_mediaSemanal1 = grafico_periodoSemanal2()
        grafico_mediaSemanal2 = grafico_periodoSemanal3()
        grafico_mediaSemanal3 = grafico_periodoSemanal4()
        grafico_mediaSemanal4 = grafico_periodoSemanal5()
        #pixmap
        #pixmap diario
        try: #usuário 1
            f = io.BytesIO()
            grafico1.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.grafig_1.setPixmap(pixmap)
        except:
            None
        
        try: #usuário 2
            f = io.BytesIO()
            grafico2.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.grafig_2.setPixmap(pixmap)
        except:
            None

        try: #usuário 3
            f = io.BytesIO()
            grafico3.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.grafig_3.setPixmap(pixmap)
        except:
            None

        try: #usuário 4
            f = io.BytesIO()
            grafico4.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.grafig_4.setPixmap(pixmap)
        except:
            None

        try: #usuário 5
            f = io.BytesIO()
            grafico5.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.grafig_5.setPixmap(pixmap)
        except:
            None 
        #pixmap semanal
        try: #usuário 1
            f = io.BytesIO()
            grafico_mediaSemanal.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.graficSemanal_1.setPixmap(pixmap)
        except:
            None 
        try: #usuário 2
            f = io.BytesIO()
            grafico_mediaSemanal1.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.graficSemanal_2.setPixmap(pixmap)
        except:
            None 
        try: #usuário 3
            f = io.BytesIO()
            grafico_mediaSemanal2.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.graficSemanal_3.setPixmap(pixmap)
        except:
            None
        try: #usuário 4
            f = io.BytesIO()
            grafico_mediaSemanal3.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.graficSemanal_4.setPixmap(pixmap)
        except:
            None 
        try: #usuário 5
            f = io.BytesIO()
            grafico_mediaSemanal4.savefig(f)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(f.getvalue())
            self.ui.graficSemanal_5.setPixmap(pixmap)
        except:
            None                                   
    # função cadastrar colaborador
    def add(self):
        self.window = cadastro5()
        self.window.show()

    def delete(self):
        self.window = delete()
        self.window.show()

    def exit(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Tem certeza que deseja sair?")
        msgBox.setWindowTitle("Sair")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            app = QApplication(sys.argv)
            sys.exit(app.exit)
