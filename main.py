import datetime
import sys
import socket

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

from PyQt5 import QtWidgets, uic
import sqlite3
import usefulwidgets
import chemistscreen


class Main(QDialog):
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
            dlg = usefulwidgets.OkThen()
            dlg.exec()

    def chemist(self):
        self.chemb.setDisabled(True)
        dlg = chemistscreen.Chemist()
        dlg.exec()
        self.chemb.setDisabled(False)


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
    window = Main()
    app.exec_()



