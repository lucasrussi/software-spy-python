from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys

from Templates.administracao import Ui_administracao
from modulos.administracao_cadastro import gerenciamento_main

class administracao(QMainWindow):
    def __init__(self, *args, **argvs):
        super(administracao, self).__init__(*args, **argvs)
        self.ui = Ui_administracao()
        self.ui.setupUi(self)
        self.ui.btn_cadastro(self.cadastro)

    def cadastro(self):
        gerenciamento_main.show()