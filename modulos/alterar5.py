from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys

from Templates.alterar5 import Ui_alterar5
from db.banco_user import load_db


class alterar5(QMainWindow,line):
    def __init__(self, *args, **argvs):
        super(alterar5, self).__init__(*args, **argvs)
        self.ui = Ui_alterar5()
        self.ui.setupUi(self)
        self.ui.btn_delete.clicked.connect(self.alterar)
        data_load = load_db()
        for i in range(0, len(data_load)):
            for j in range(1, 2):
                self.ui.comboBox.addItem(data_load[i][j])
                select = self.ui.comboBox.activated[str]
                if data_load[i][j] == select:
                    cargo = self.ui.edit_cargo.textEdited(data_load[i][2])
                    setor = self.ui.edit_setor.textEdited(data_load[i][3])
                    email = self.ui.edit_email.textEdited(data_load[i][4])
                    cpf = self.ui.edit_cpf.textEdited(data_load[i][5])
                    app1 = self.ui.edit_app1.textEdited(data_load[i][6])
                    app2 = self.ui.edit_app2.textEdited(data_load[i][7])
                    app3 = self.ui.edit_app3.textEdited(data_load[i][8])
                    app4 = self.ui.edit_app4.textEdited(data_load[i][9])
                    app5 = self.ui.edit_app5.textEdited(data_load[i][10])
    
    #def alterar(self):
        