import datetime
import sys
import socket

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic
import sqlite3
import usefulwidgets


class Chemist(QDialog):
    def __init__(self):
        super(Chemist, self).__init__()
        uic.loadUi('ui_dir/chemist.ui', self)
        self.show()

    def closeEvent(self, event):
        dlg = usefulwidgets.CustomDialog('quit?', 'R u sure u wanna exit?')
        if dlg.exec():
            event.accept()
        else:
            event.ignore()
            if not dlg.exec():
                dlg = usefulwidgets.OkThen()
                dlg.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Chemist()
    app.exec_()
