from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication, QComboBox, QLineEdit)
from currency_converter import CurrencyConverter
from currency_list import list
import sys


class Converter(QWidget):
    def __init__(self):
        super().__init__()
        QWidget.__init__(self)

        # display a title at the beginning of the program
        self.lbl = QLabel("Currency Convert", self)
        self.lbl.adjustSize()

        self.activecurrenciesleft = QLabel("", self)
        self.activecurrenciesright = QLabel("", self)

        # create checkbox of currencies and positions
        self.currenciesleft = QComboBox()
        self.currenciesright = QComboBox()
        self.currenciesleft.move(50, 50)
        self.currenciesright.move(200, 50)

        self.firstcurrency = QLineEdit()
        self.secoundcurrency = QLineEdit()

        # front display: display in horizontal
        layout = QHBoxLayout()
        # add widgets needed to displayed
        layout.addWidget(self.activecurrenciesleft)
        layout.addWidget(self.activecurrenciesright)
        layout.addWidget(self.currenciesleft)
        layout.addWidget(self.firstcurrency)
        layout.addWidget(self.currenciesright)
        layout.addWidget(self.secoundcurrency)
        self.setLayout(layout)

        # name of the window program
        self.setWindowTitle('Currency Converter')

        # retrieve
        for key in list.keys():
            # add current currency to checkbox
            self.currenciesleft.addItem(key)
            self.currenciesright.addItem(key)
        self.currenciesleft.setGeometry(50, 50, 50, 50)
        self.currenciesright.setGeometry(50, 50, 50, 50)

        # retrieve text fields
        self.firstcurrency.textChanged[str].connect(self.onchangedfirstcurrency)
        self.secoundcurrency.textChanged[str].connect(self.onchangedsecoundcurrency)

        # retrieve checkbox fields
        self.currenciesleft.activated[str].connect(self.onchangedcurrenciesleft)
        self.currenciesright.activated[str].connect(self.onchangedcurrenciesright)

        # display
        self.setGeometry(500, 300, 500, 300)
        self.show()

    def onchangedcurrenciesleft(self, text):  # c
        self.activecurrenciesleft = text

    def onchangedcurrenciesright(self, text):  # d
        self.activecurrenciesright = text

    def onchangedfirstcurrency(self, text):  # a
        cc = CurrencyConverter()
        self.firstcurrency.setText(text)
        self.firstcurrency.adjustSize()
        # self.firstcurrency.move(50, 50)

        value = str(cc.convert(float(text), str(self.activecurrenciesleft), str(self.activecurrenciesright)))
        self.secoundcurrency.setText(value)
        self.secoundcurrency.adjustSize()

    def onchangedsecoundcurrency(self, text):  # b
        cc = CurrencyConverter()
        self.secoundcurrency.setText(text)
        self.secoundcurrency.adjustSize()
        # self.secoundcurrency.move(200, 50)

        value = str(cc.convert(float(text), str(self.activecurrenciesright), str(self.activecurrenciesleft)))
        self.firstcurrency.setText(value)
        self.firstcurrency.adjustSize()


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
    
    currency = Converter()

    currency.show()

app.exec_()