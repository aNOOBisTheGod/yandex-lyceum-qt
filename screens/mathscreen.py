import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic

import functions.chemistry
import usefulwidgets
import functions.math


class Math(QDialog):
    def __init__(self):
        super(Math, self).__init__()
        uic.loadUi('ui_dir/math.ui', self)
        self.chartb.clicked.connect(self.buildchart)

    def buildchart(self):
        func = functions.math.niceeval(self.function.text()).replace('x', '{}')
        arry = []
        arrx = []
        for i in range(-1000, 1000):
            try:
                arr = [i / 100 for _ in range(func.count('{}'))]
                try:
                    x = eval(func.format(*arr))
                    arry.append(i / 100)
                    arrx.append(x)
                except ZeroDivisionError:
                    pass
            except:
                pass
        dlg = usefulwidgets.Chart(arrx, arry)
        dlg.exec()

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
    window = Math()
    app.exec_()
