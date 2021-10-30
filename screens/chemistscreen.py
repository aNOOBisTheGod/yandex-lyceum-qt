import datetime
import sys
import socket

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic
import sqlite3

import functions.chemistry
import usefulwidgets


class Chemist(QDialog):
    def __init__(self):
        super(Chemist, self).__init__()
        uic.loadUi('ui_dir/chemist.ui', self)
        self.anstext = ''
        self.chaintext = ''
        self.solveeq.clicked.connect(self.solve)
        self.solvec.clicked.connect(self.solvechain)
        self.show()

    def solvechain(self):
        x = self.chain.text()
        self.chaintext = '\n'.join(functions.chemistry.chain(x))
        self.res2.setPlaceholderText(self.chaintext)

    def solve(self):
        x = self.elem1.text()
        y = self.elem2.text()
        self.anstext = functions.chemistry.solveequation(x, y)
        self.res1.setText(self.anstext)

    def closeEvent(self, event):
        usefulwidgets.on_close(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Chemist()
    app.exec_()
