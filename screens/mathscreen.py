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
        try:
            try:
                func = functions.math.niceeval(self.function.text()).replace('x', '{}')
            except Exception as e:
                print(e)
                return
            arry = []
            arrx = []
            for x in range(-1000, 1000):
                try:
                    arr = [x / 100 for _ in range(func.count('{}'))]
                    try:
                        y = eval(func.format(*arr))
                        arrx.append(x / 100)
                        arry.append(y)
                    except Exception as e:
                        print(e)
                except:
                    pass
            dlg = usefulwidgets.Chart(arrx, arry)
            dlg.exec()
        except Exception as e:
            print(e)

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