import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette
from PySide2.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication, QComboBox, QLineEdit)
from currency_converter import CurrencyConverter


class Converter(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.cc = CurrencyConverter(fallback_on_wrong_date=True)

        # display a title at the beginning of the program
        self.lbl = QLabel("Currency Convert", self)
        self.lbl.adjustSize()

        self.activecurrenciesleft = QLabel("", self)
        self.activecurrenciesright = QLabel("", self)

        # create checklist of currencies and positions
        self.currenciesleft = QComboBox()
        self.currenciesright = QComboBox()
        self.currenciesleft.move(50, 50)
        self.currenciesright.move(200, 50)

        self.firstcurrency = QLineEdit("0.0", self)
        self.secoundcurrency = QLineEdit("0.0", self)

        # front display: display in horizontal
        layout = QHBoxLayout()
        # add widgets needed to displayed
        # layout.addWidget(self.activecurrenciesleft)
        # layout.addWidget(self.activecurrenciesright)
        layout.addWidget(self.currenciesleft)
        layout.addWidget(self.firstcurrency)
        layout.addWidget(self.currenciesright)
        layout.addWidget(self.secoundcurrency)
        self.setLayout(layout)

        # name of the window program
        self.setWindowTitle('Currency Converter')

        # retrieve
        for key in sorted(self.cc.currencies):
            # add current currency to checklists
            self.currenciesleft.addItem(key)
            self.currenciesright.addItem(key)

        # set default currencies
        self.currenciesleft.setCurrentIndex(22)
        self.currenciesright.setCurrentIndex(10)

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

    def onchangedcurrenciesleft(self, text):
        self.activecurrenciesleft = text

    def onchangedcurrenciesright(self, text):
        self.activecurrenciesright = text

    def onchangedfirstcurrency(self, text):
        if text == "":
            self.firstcurrency.setText("0.0")
        else:
            self.secoundcurrency.blockSignals(True)
            self.firstcurrency.setText(text)

            value = str(self.cc.convert(
                float(text),
                str(self.currenciesleft.currentText()),
                str(self.currenciesright.currentText())))
            self.secoundcurrency.setText(value)
            self.secoundcurrency.blockSignals(False)

    def onchangedsecoundcurrency(self, text):
        if text != "":
            self.firstcurrency.blockSignals(True)
            self.secoundcurrency.setText(text)

            value = str(self.cc.convert(
                float(text),
                str(self.currenciesleft.currentText()),
                str(self.currenciesright.currentText())))
            self.firstcurrency.setText(value)
            self.firstcurrency.blockSignals(False)
        else:
            self.secoundcurrency.setText("0.0")




app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.gray)
    app.setPalette(palette)
    app.setStyleSheet("QLineEdit, QComboBox  { padding: 5px; }")

    currency = Converter()

    currency.show()

app.exec_()
