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
from db.banco_user import load_app
from Templates.userColaborador import Ui_userColaborador

class userColaborador(QMainWindow):
    def __init__(self, *args, **argvs):
        super(userColaborador, self).__init__(*args, **argvs)
        self.ui = Ui_userColaborador()
        self.ui.setupUi(self)
        self.ui.btn_exit.clicked.connect(self.exit)
        app= login.aplicativos
        print(f'esse é o app do userColaborador {app}')
    def exit(self):
        self.exit()