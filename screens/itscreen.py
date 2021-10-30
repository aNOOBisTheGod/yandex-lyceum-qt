import math
import os
import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic

import usefulwidgets
from functions.it import *


class It(QDialog):
    def __init__(self):
        super(It, self).__init__()
        uic.loadUi('ui_dir/it.ui', self)
        self.solvet.clicked.connect(self.translate)
        self.solveo.clicked.connect(self.operation)
        self.show()

    def translate(self):
        try:
            n1 = self.numt1.text()
            sys1 = int(self.syst1.value())
            sys2 = int(self.syst2.value())
            self.rest.setText(fromtenth(totenth(n1, sys1), sys2))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def operation(self):
        try:
            oper = self.oper.text()
            n1 = self.numo1.text()
            n2 = self.numo2.text()
            sys1 = int(self.syso1.value())
            sys2 = int(self.syso2.value())
            res = eval(f'{totenth(n1, sys1)} {oper} {totenth(n2, sys2)}')
            base = int(self.sysor.value())
            self.reso.setText(fromtenth(str(res), base))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def closeEvent(self, event):
        usefulwidgets.on_close(event)
