import os
import sys

from PyQt5.QtWidgets import QDialog

from PyQt5 import QtWidgets, uic
import usefulwidgets
from functions.mathematics import *


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
        self.show()

    def buildchart(self):
        """builds chart of given function"""
        try:
            try:
                if '**' in self.function.text():
                    func = niceeval(self.function.text()).replace('x', '{}')
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
        usefulwidgets.on_close(event)

    def solve(self):
        """solves all simple functions"""
        try:
            if self.gcd.text() != '':
                self.gcdres.setText(str(math.gcd(*list(map(int, self.gcd.text().split())))))
            if self.lcm.text() != '':
                self.lcmres.setText(str(math.lcm(*list(map(int, self.gcd.text().split())))))
            if self.median.text() != '':
                self.medianres.setText(median(self.median.text()))
            if self.mean.text() != '':
                self.meanres.setText(mean(self.mean.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def binsolve(self):
        """solves simple equation using binary search"""
        try:
            self.res1.setText(fastequation(self.eq1.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def diophant(self):
        """solves diophantine equation"""
        try:
            self.res3.setText(diophantic(self.eq3.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)

    def quadratic(self):
        """solves quadratic equation"""
        try:
            self.res2.setText(quadratic(self.eq2.text()))
        except Exception as e:
            usefulwidgets.Customalert(self, e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Math()
    app.exec_()
