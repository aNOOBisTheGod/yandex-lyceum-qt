import datetime
import sys
import socket

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

from PyQt5 import QtWidgets, uic
import sqlite3
import usefulwidgets
from screens import chemistscreen, mathscreen, itscreen


class Main(QDialog):
    """main window"""
    def __init__(self):
        getdata()
        super(Main, self).__init__()
        uic.loadUi('ui_dir/main.ui', self)
        self.connection = sqlite3.connect("data_db.sqlite")
        header = self.dbviewer.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.exitbutton.clicked.connect(self.exit)
        self.select_data()
        self.chemb.clicked.connect(self.chemist)
        self.mathb.clicked.connect(self.math)
        self.itb.clicked.connect(self.it)
        self.show()

    def select_data(self):
        """function that fill the table view widget with database(data_db.sqlite) data
        1st - column - IP, 2nd - time of entrance"""
        query = "SELECT * FROM entrances"
        res = self.connection.cursor().execute(query).fetchall()
        self.dbviewer.setColumnCount(2)
        self.dbviewer.setRowCount(0)
        for i, row in enumerate(reversed(res)):
            self.dbviewer.setRowCount(
                self.dbviewer.rowCount() + 1)
            for j, elem in enumerate(row):
                self.dbviewer.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def exit(self):
        """no comments in here"""
        dlg = usefulwidgets.CustomDialog('EXIT', 'R u sure u wanna exit?')
        if dlg.exec():
            exit(0)
        else:
            dlg = usefulwidgets.OkThen()
            dlg.exec()

    def closeEvent(self, event):
        """function that calls when user clicks cross button in top of window"""
        usefulwidgets.on_close(event)

    # next functions its a functions that opens definite screens
    def chemist(self):
        self.chemb.setDisabled(True)
        dlg = chemistscreen.Chemist()
        dlg.exec()
        self.chemb.setDisabled(False)

    def math(self):
        self.mathb.setDisabled(True)
        dlg = mathscreen.Math()
        dlg.exec()
        self.mathb.setDisabled(False)

    def it(self):
        self.itb.setDisabled(True)
        dlg = itscreen.It()
        dlg.exec()
        self.itb.setDisabled(False)


def getdata():
    """function that fills database with current time and IP, IP temporary disabled"""
    con = sqlite3.connect('data_db.sqlite')
    cur = con.cursor()
    date_format = "%a, %d %b %Y %I:%M %p"
    t = datetime.datetime.now().strftime(date_format)
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)
    # IP is secret data ↑ function that get ur IP adress
    IP = 'тип тут айпи'
    cur.execute(f"""INSERT INTO entrances (time, ip) VALUES ('{t}', '{IP}');""")
    con.commit()
    con.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec_()
