from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class OkThen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ok Then")
        self.setGeometry(900, 500, 200, 40)
