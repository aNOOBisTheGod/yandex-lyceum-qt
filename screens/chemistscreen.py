import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

from PyQt5 import QtWidgets, uic

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
        self.connection = sqlite3.connect("./data_db.sqlite")
        header = self.chainviewer.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.full.setText('<a href="https://i.ytimg.com/vi/eRnV3qBdRCI/maxresdefault.jpg">FULL IMAGE</a>')
        self.full.setOpenExternalLinks(True)
        self.select_data()
        self.show()

    def solvechain(self):
        """function that solves chemistry chain of reactions(need WI FI enabled)"""
        x = self.chain.text()
        try:
            self.chaintext = '\n'.join(functions.chemistry.chain(x))
        except Exception as e:
            return usefulwidgets.returnalert(self, e)
        self.res2.setPlaceholderText(self.chaintext)
        self.connection.cursor().execute(f"""INSERT INTO chains (chain, res) VALUES ('{x}', '{self.chaintext}');""")
        self.connection.commit()
        self.select_data()

    def solve(self):
        """solves simple chemist reaction equation(need WI FI enabled)"""
        x = self.elem1.text()
        y = self.elem2.text()
        try:
            self.anstext = functions.chemistry.solveequation(x, y)
            with open('chemistsolutions.txt', 'a+', encoding="utf-16") as f:
                f.write('\n' + self.anstext)
        except Exception as e:
            return usefulwidgets.returnalert(self, e)
        self.res1.setText(self.anstext)

    def closeEvent(self, event):
        usefulwidgets.on_close(event)

    def select_data(self):
        try:
            query = "SELECT * FROM chains"
            res = self.connection.cursor().execute(query).fetchall()
            self.chainviewer.setColumnCount(2)
            self.chainviewer.setRowCount(0)
            for i, row in enumerate(reversed(res)):
                self.chainviewer.setRowCount(
                    self.chainviewer.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.chainviewer.setItem(
                        i, j, QTableWidgetItem(str(elem)))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Chemist()
    app.exec_()
