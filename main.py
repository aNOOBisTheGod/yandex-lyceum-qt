import datetime
import sys
import socket

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QDialog, QTableView, QTableWidgetItem, QHeaderView

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3
import usefulwidgets


class Example(QDialog):
    def __init__(self):
        getdata()
        super(Example, self).__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("data_db.sqlite")
        header = self.dbviewer.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.exitbutton.clicked.connect(self.exit)
        self.select_data()
        self.show()

    def select_data(self):
        query = "SELECT * FROM entrances"
        res = self.connection.cursor().execute(query).fetchall()
        self.dbviewer.setColumnCount(2)
        self.dbviewer.setRowCount(0)
        for i, row in enumerate(res):
            self.dbviewer.setRowCount(
                self.dbviewer.rowCount() + 1)
            for j, elem in enumerate(row):
                self.dbviewer.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def exit(self):
        dlg = usefulwidgets.CustomDialog('EXIT', 'R u sure u wanna exit?')
        if dlg.exec():
            exit(0)
        else:
            dlg = QDialog(self)
            dlg.setWindowTitle("Ok Then")
            dlg.setGeometry(900, 500, 200, 40)
            dlg.exec()


def getdata():
    con = sqlite3.connect('data_db.sqlite')
    cur = con.cursor()
    date_format = "%a, %d %b %Y %I:%M %p"
    t = datetime.datetime.now().strftime(date_format)
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)
    cur.execute(f"""INSERT INTO entrances (time, ip) VALUES ('{t}', '{IP}');""")
    con.commit()
    con.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Example()
    app.exec_()



