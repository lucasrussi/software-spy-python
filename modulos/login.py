from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import re
import sys
import datetime
import time
import threading
from win32 import win32api
from functools import partial
from Templates.login import Ui_login
from Templates.userColaborador import Ui_userColaborador
from modulos.gerenciamento_client import gerenciamento_client
from modulos.email import emailogin
from modulos.keyboardListenner import keyloger
from modulos.processingData import processingData
# import banco de dados
from db.banco_user import login_username_db
from db.banco_user import login_pass_db
from db.banco_user import loadaplicativos

class login(QMainWindow):
    def __init__(self, *args, **argvs):
        super(login, self).__init__(*args, **argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.button_enter.clicked.connect(self.login)
        self.ui.button_exit.clicked.connect(self.exit)

    def login(self):
        now = datetime.datetime.now()
        hoje22h = now.replace(hour=22, minute=0, second=0, microsecond=0)
        hoje5h = now.replace(hour=5, minute = 0, second=0, microsecond=0)
        user = self.ui.user_input.text()
        senha = self.ui.pass_input.text()
        username = login_username_db()
        if now > hoje5h and now < hoje22h:
            for i in range(0, len(username)):
                if user == username[i][0]:
                    passworld = login_pass_db(user)
                    if senha == passworld[0][0]:
                        emailogin(user)
                        self.load_app(user)
                        self.window = userColaborador()
                        self.window.show()
                        window_login.close()               
        else:
            QMessageBox.warning(
            QMessageBox(), "Horário inadequado", "O software estará disponível entre 05h da manhã até 22h da noite")
        if user == 'admin'and senha == 'admin':
            self.window = gerenciamento_client()
            self.window.show()
            window_login.close()

    def load_app(self, user):
        login.loadapp = loadaplicativos(user)
        login.user = user
        window_login.close()

    def exit(self):
        sys.exit(app.exit)


class userColaborador(QMainWindow):

    def __init__(self, *args, **argvs):
        super(userColaborador, self).__init__(*args, **argvs)
        self.ui = Ui_userColaborador()
        self.ui.setupUi(self)
        user = login.user
        app = login.loadapp

        keyloger(app)
        def exit(app,user,tempoOcioso,timeInicio):

            processingData(app,user,tempoOcioso,timeInicio)
            self.close()

        self.ui.btn_exit.clicked.connect(lambda:exit(app,user,return_value,timeInicio))
        global tempoOcioso
        global return_value
        global timeInicio
        timeInicio = time.monotonic()
        def getIdleTime(tempoOcioso):
            ocioso = (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0
            if ocioso > 600:
                tempoOcioso += 1
            return tempoOcioso

        def startSchedule():
            global tempoOcioso
            global return_value
            while True:
                ocioso = getIdleTime(tempoOcioso)
                return_value += ocioso
                time.sleep(1.0)
        def blokeTime():
            while True:
                now = datetime.datetime.now()
                hoje22h = now.replace(hour=22, minute=0, second=0, microsecond=0)
                hoje5h = now.replace(hour=5, minute = 0, second=0, microsecond=0)
                if now > hoje5h and now < hoje22h:
                    lambda:exit(app,user,return_value,timeInicio)
                time.sleep(2.0)
        def savehoras():
            while True:
                tempoDecorrido = 0
                agora = datetime.datetime.now()
                now = agora.strftime('%d/%m')
                time.sleep(60)
                tempoDecorrido = '60'+' '+now
                with open('logFile.txt', 'a')  as f:
                    f.write(tempoDecorrido + '\n')
        
        #apagando o arquivo txt do dia anterior
        hoje = datetime.datetime.now()
        diaAtual = hoje.strftime('%d/%m')
        diaAnterior = 0
        with open('logFile.txt','r') as file:
            for line in file:
                if re.search(diaAtual,line,re.IGNORECASE):
                    diaAnterior +=1
        if diaAnterior == 0:
            open('logFile.txt','w').close()
        threading.Thread(target=startSchedule, daemon=True).start()
        threading.Thread(target=blokeTime, daemon=True).start()
        threading.Thread(target=savehoras, daemon=True).start()
tempoOcioso = 0
return_value = 0
timeInicio = 0
app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window_login = login()
    window_login.show()
sys.exit(app.exec_())


