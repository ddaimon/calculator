import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from calculator_python import Ui_mainWindow

class Calculator(QMainWindow,Ui_mainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setupUi(self)
        self.zeroButton.clicked.connect(self.tiklandi)
        self.oneButton.clicked.connect(self.tiklandi)
        self.twoButton.clicked.connect(self.tiklandi)
        self.threeButton.clicked.connect(self.tiklandi)
        self.fourButton.clicked.connect(self.tiklandi)
        self.fiveButton.clicked.connect(self.tiklandi)
        self.sixButton.clicked.connect(self.tiklandi)
        self.sevenButton.clicked.connect(self.tiklandi)
        self.eightButton.clicked.connect(self.tiklandi)
        self.nineButton.clicked.connect(self.tiklandi)
        self.plusButton.clicked.connect(self.tiklandi)
        self.multipliedButton.clicked.connect(self.tiklandi)
        self.minusButton.clicked.connect(self.tiklandi)
        self.dividedButton.clicked.connect(self.tiklandi)
        self.equalButton.clicked.connect(self.hesapla)
        self.dotButton.clicked.connect(self.tiklandi)
        self.clearButton.clicked.connect(self.tiklandi)
        self.deleteButton.clicked.connect(self.clear)


    def clear(self):
        self.lineEdit.clear()

    def hesapla(self):
        self.lineEdit.setText(str(eval((self.lineEdit.text()))))

    def tiklandi(self):
        sender = self.sender()
        self.lineEdit.setText(self.lineEdit.text() + sender.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    h = Calculator()
    h.show()

    sys.exit(app.exec_())








