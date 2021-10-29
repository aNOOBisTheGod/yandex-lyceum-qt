import math
import os
import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QMessageBox

from PyQt5 import QtWidgets, uic

import functions.chemistry
import usefulwidgets
import functions.mathematics


class It(QDialog):
    def __init__(self):
        super(It, self).__init__()
        uic.loadUi('ui_dir/it.ui', self)