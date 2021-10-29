import math
import os
import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic

import functions.chemistry
import usefulwidgets
import functions.mathematics


class Math(QDialog):
    def __init__(self):
        super(Math, self).__init__()
        uic.loadUi('ui_dir/math.ui', self)
        self.chartb.clicked.connect(self.buildchart)
        self.solveall.clicked.connect(self.solve)
        self.calcopen.clicked.connect(lambda x, command='calc': os.system(command))
        self.fs1.clicked.connect(self.binsolve)
        self.fs3.clicked.connect(self.diophant)
        self.fs2.clicked.connect(self.quadratic)

    def buildchart(self):
        try:
            try:
                if '**' in self.function.text():
                    func = functions.mathematics.niceeval(self.function.text()).replace('x', '{}')
                else:
                    func = self.function.text()
            except Exception as e:
                usefulwidgets.Customalert(self, e)
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
                    except ZeroDivisionError as e:
                        print(e)
                except Exception as e:
                    usefulwidgets.Customalert(self, e)
            dlg = usefulwidgets.Chart(arrx, arry)
            dlg.exec()
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def closeEvent(self, event):
        dlg = usefulwidgets.CustomDialog('EXIT', 'R u sure u wanna exit?')
        if dlg.exec():
            event.accept()
        else:
            event.ignore()
            dlg = usefulwidgets.OkThen()
            dlg.exec()

    def solve(self):
        try:
            if self.gcd.text() != '':
                self.gcdres.setText(str(math.gcd(*list(map(int, self.gcd.text().split())))))
            if self.lcm.text() != '':
                self.lcmres.setText(str(math.lcm(*list(map(int, self.gcd.text().split())))))
            if self.median.text() != '':
                self.medianres.setText(functions.mathematics.median(self.median.text()))
            if self.mean.text() != '':
                self.meanres.setText(functions.mathematics.mean(self.mean.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def binsolve(self):
        try:
            self.res1.setText(functions.mathematics.fastequation(self.eq1.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def diophant(self):
        try:
            self.res3.setText(functions.mathematics.diophantic(self.eq3.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def quadratic(self):
        try:
            self.res2.setText(functions.mathematics.quadratic(self.eq2.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Math()
    app.exec_()